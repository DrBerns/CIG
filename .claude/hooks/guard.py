#!/usr/bin/env python3
"""
PreToolUse guard hook — the machine-enforced RED tier.

This runs BEFORE every Bash / PowerShell command the agent tries to execute.
It does not depend on the agent remembering any rule. Its only job is to
HARD-BLOCK the small set of catastrophic, data-destroying commands that have
burned this practice before (robocopy nuked EMR data once) or that would be
unrecoverable.

Design invariants:
  * FAIL OPEN. Any parse error, unknown shape, or unexpected exception -> allow
    (exit 0). This hook may only ever ADD blocks for KNOWN-bad patterns; it must
    never block benign or unrecognized commands. A buggy guard that blocks real
    work is worse than no guard.
  * It mirrors the `deny` list in .claude/settings.json. The two layers agree on
    purpose so that RED is enforced even if one layer is edited or bypassed.

Block signal: exit code 2 + reason on stderr (Claude Code treats a PreToolUse
exit 2 as "deny this tool call" and shows stderr to the model).
"""
import sys, json, re

def _command_from_stdin():
    raw = sys.stdin.read()
    if not raw.strip():
        return None
    data = json.loads(raw)
    ti = data.get("tool_input") or {}
    # Bash and PowerShell tools both carry the command under "command".
    return ti.get("command")

def _strip_quoted(c):
    # Remove double- then single-quoted spans BEFORE matching, so a trigger word
    # inside a commit message / echo string (e.g. git commit -m "... robocopy ...")
    # does not false-positive. A real destructive invocation never hides its own
    # command name inside quotes; detection only needs the bare command token.
    c = re.sub(r'"[^"]*"', ' ', c)
    c = re.sub(r"'[^']*'", ' ', c)
    return c

def _rm_recursive_force(c):
    # rm with BOTH a recursive flag and a force flag, in any order / combined.
    if not re.search(r'\brm\b', c):
        return False
    has_r = bool(re.search(r'-[a-z]*r', c) or re.search(r'--recursive', c))
    has_f = bool(re.search(r'-[a-z]*f', c) or re.search(r'--force', c))
    return has_r and has_f

def _remove_item_recursive_force(c):
    # PowerShell Remove-Item (or ri/rd/rmdir alias) with -Recurse AND -Force.
    if not re.search(r'\b(remove-item|rmdir|\bri\b|\brd\b)\b', c):
        return False
    return ('-recurse' in c) and ('-force' in c)

# (regex, human reason) — matched case-insensitively against the whole command.
RULES = [
    (r'\brobocopy\b',
     "robocopy is BLOCKED (a robocopy mirror previously destroyed EMR data). "
     "If a copy/mirror is genuinely needed, do it by hand and confirm the flags."),
    (r'\bdel\b[^\n]*\s/s\b',
     "recursive `del /s` is BLOCKED (bulk delete)."),
    (r'\brmdir\b[^\n]*\s/s\b',
     "recursive `rmdir /s` is BLOCKED (bulk directory delete)."),
    (r'\bformat\s+[a-z]:',
     "disk `format` is BLOCKED."),
    (r'\bformat-volume\b',
     "`Format-Volume` is BLOCKED."),
    (r'\bdiskpart\b',
     "`diskpart` is BLOCKED (partition/volume destruction)."),
    (r'\bcipher\b[^\n]*\s/w\b',
     "`cipher /w` secure-wipe is BLOCKED."),
    (r'\bgit\s+push\b[^|;&]*(\s-f\b|--force)',
     "`git push --force` is BLOCKED (can erase remote history)."),
    (r'\bgit\s+clean\b[^|;&]*-[a-z]*f',
     "`git clean -f` is BLOCKED (deletes untracked files irrecoverably)."),
]

def main():
    try:
        cmd = _command_from_stdin()
    except Exception:
        sys.exit(0)          # fail open
    if not cmd:
        sys.exit(0)
    c = _strip_quoted(cmd.lower())
    try:
        for pattern, reason in RULES:
            if re.search(pattern, c):
                sys.stderr.write("BLOCKED by .claude/hooks/guard.py (RED tier): " + reason + "\n")
                sys.exit(2)
        if _rm_recursive_force(c):
            sys.stderr.write("BLOCKED by .claude/hooks/guard.py (RED tier): recursive-force `rm` is not allowed.\n")
            sys.exit(2)
        if _remove_item_recursive_force(c):
            sys.stderr.write("BLOCKED by .claude/hooks/guard.py (RED tier): recursive-force `Remove-Item` is not allowed.\n")
            sys.exit(2)
    except Exception:
        sys.exit(0)          # fail open on any matching error
    sys.exit(0)

if __name__ == "__main__":
    main()
