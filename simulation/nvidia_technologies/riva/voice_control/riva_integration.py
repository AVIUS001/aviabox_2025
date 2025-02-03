#!/usr/bin/env python3
"""
riva_integration.py

Stub for integrating NVIDIA Riva voice control.
"""
import json

def load_commands():
    with open("commands.json", "r") as f:
        commands = json.load(f)
    return commands

if __name__ == "__main__":
    cmds = load_commands()
    print("Loaded commands:", cmds)
