#!/usr/bin/env python3
"""
Shared logging utility for demo-agents.
Usage: python3 scripts/log.py <agent-name> <event> <message>
Events: START END REJECT FAIL INFO
Output appended to output/agent-log.txt and printed to stdout.
"""
import sys, os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "output", "agent-log.txt")
VALID_EVENTS = {"START", "END", "REJECT", "FAIL", "INFO"}

def main():
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <agent-name> <event> <message>", file=sys.stderr)
        sys.exit(1)
    agent   = sys.argv[1]
    event   = sys.argv[2].upper()
    message = " ".join(sys.argv[3:])
    if event not in VALID_EVENTS:
        print(f"Unknown event '{event}'. Valid: {', '.join(sorted(VALID_EVENTS))}", file=sys.stderr)
        sys.exit(1)
    timestamp  = datetime.now().strftime("%H:%M:%S")
    agent_col  = f"[{agent}]".ljust(20)
    event_col  = event.ljust(6)
    line = f"[{timestamp}] {agent_col} {event_col} — {message}\n"
    os.makedirs(os.path.dirname(os.path.abspath(LOG_FILE)), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line)
    print(line, end="")

if __name__ == "__main__":
    main()
