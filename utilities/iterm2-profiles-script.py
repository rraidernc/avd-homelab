#!/usr/bin/env python3
"""
generate-iterm2-profiles.py
Generates iTerm2 saved profiles for all AVD homelab fabric devices.
Profiles are written directly to iTerm2's plist and are immediately
available in iTerm2 → Profiles menu and New Tab/Window dialogs.

Usage: python3 generate-iterm2-profiles.py
Then restart iTerm2 (or Profiles → Other Actions → Refresh)
"""

import json
import subprocess
import uuid
import os

# ─── Configuration ────────────────────────────────────────────────────────────

SSH_USER = "cvpadmin"

DEVICES = {
    "DC1": [
        {"name": "dc1-spine1",        "ip": "192.168.4.120", "tag": "spine"},
        {"name": "dc1-spine2",        "ip": "192.168.4.121", "tag": "spine"},
        {"name": "dc1-leaf1a",        "ip": "192.168.4.122", "tag": "leaf"},
        {"name": "dc1-leaf1b",        "ip": "192.168.4.123", "tag": "leaf"},
        {"name": "dc1-leaf1c",        "ip": "192.168.4.124", "tag": "leaf"},
        {"name": "dc1-leaf2a",        "ip": "192.168.4.126", "tag": "leaf"},
        {"name": "dc1-leaf2b",        "ip": "192.168.4.127", "tag": "leaf"},
        {"name": "dc1-leaf2c",        "ip": "192.168.4.128", "tag": "leaf"},
        {"name": "dc1-border-leaf1a", "ip": "192.168.4.140", "tag": "border"},
        {"name": "dc1-border-leaf1b", "ip": "192.168.4.141", "tag": "border"},
    ],
    "DC2": [
        {"name": "dc2-spine1",        "ip": "192.168.4.130", "tag": "spine"},
        {"name": "dc2-spine2",        "ip": "192.168.4.131", "tag": "spine"},
        {"name": "dc2-leaf1a",        "ip": "192.168.4.132", "tag": "leaf"},
        {"name": "dc2-leaf1b",        "ip": "192.168.4.133", "tag": "leaf"},
        {"name": "dc2-leaf1c",        "ip": "192.168.4.134", "tag": "leaf"},
        {"name": "dc2-leaf2a",        "ip": "192.168.4.136", "tag": "leaf"},
        {"name": "dc2-leaf2b",        "ip": "192.168.4.137", "tag": "leaf"},
        {"name": "dc2-leaf2c",        "ip": "192.168.4.138", "tag": "leaf"},
        {"name": "dc2-border-leaf1a", "ip": "192.168.4.142", "tag": "border"},
        {"name": "dc2-border-leaf1b", "ip": "192.168.4.143", "tag": "border"},
    ],
}

# ─── Color Schemes per role ────────────────────────────────────────────────────
# Each color is [Red, Green, Blue] 0.0-1.0

COLORS = {
    "spine":  {"r": 0.08, "g": 0.18, "b": 0.35},  # Dark blue
    "leaf":   {"r": 0.05, "g": 0.25, "b": 0.12},  # Dark green
    "border": {"r": 0.30, "g": 0.12, "b": 0.05},  # Dark orange/brown
}

def make_color(r, g, b):
    return {
        "Red Component":   r,
        "Green Component": g,
        "Blue Component":  b,
        "Alpha Component": 1.0,
        "Color Space":     "sRGB"
    }

def make_profile(device, dc):
    role = device["tag"]
    color = COLORS[role]
    bg = make_color(color["r"], color["g"], color["b"])

    return {
        "Guid":                        str(uuid.uuid4()),
        "Name":                        device["name"],
        "Custom Command":              "Yes",
        "Command":                     f"ssh {SSH_USER}@{device['ip']}",
        "Tags":                        [dc, role, "avd-homelab"],
        "Background Color":            bg,
        "Foreground Color":            make_color(0.9, 0.9, 0.9),
        "Bold Color":                  make_color(1.0, 1.0, 1.0),
        "Cursor Color":                make_color(0.7, 0.9, 0.7),
        "Selection Color":             make_color(0.2, 0.4, 0.2),
        "Badge Text":                  device["name"],
        "Show Mark Indicators":        True,
        "Terminal Type":               "xterm-256color",
        "Use Bold Font":               True,
        "Scrollback Lines":            5000,
        "Mouse Reporting":             True,
        "Allow Title Setting":         True,
        "Title Components":            32,  # show profile name
        "Initial Text":                "",
    }

# ─── Main ─────────────────────────────────────────────────────────────────────

PLIST_PATH = os.path.expanduser(
    "~/Library/Application Support/iTerm2/DynamicProfiles/avd-homelab.json"
)

def main():
    os.makedirs(os.path.dirname(PLIST_PATH), exist_ok=True)

    profiles = []
    for dc, devices in DEVICES.items():
        for device in devices:
            profiles.append(make_profile(device, dc))
        print(f"✅ Generated {len(devices)} profiles for {dc}")

    payload = {"Profiles": profiles}

    with open(PLIST_PATH, "w") as f:
        json.dump(payload, f, indent=2)

    print(f"\n✅ {len(profiles)} profiles written to:")
    print(f"   {PLIST_PATH}")
    print("\n📋 How to use:")
    print("   • iTerm2 picks up Dynamic Profiles automatically — no restart needed")
    print("   • Open a device:  iTerm2 → Profiles → <device-name>")
    print("   • Open multiple:  Profiles window → hold ⌘ → click devices → Open")
    print("   • Filter by tag:  Profiles window → type 'DC1', 'spine', 'leaf', or 'border'")
    print("\n🎨 Color coding:")
    print("   • Dark blue   = spines")
    print("   • Dark green  = leaves")
    print("   • Dark orange = border leafs")

if __name__ == "__main__":
    main()
