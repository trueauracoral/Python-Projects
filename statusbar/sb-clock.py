#!/usr/bin/env python
from datetime import datetime

def main():
    now = datetime.now()

    clock = now.strftime("%I")
    print(clock)
    icons = {
        "00": "🕛",
        "01": "🕐",
        "02": "🕑",
        "03": "🕒",
        "04": "🕓",
        "05": "🕔",
        "06": "🕕",
        "07": "🕖",
        "08": "🕗",
        "09": "🕘",
        "10": "🕙",
        "11": "🕚",
        "12": "🕛",
    }

    icon = icons[clock]
    formatted = now.strftime("%Y %b %d (%a) %I:%M%p")
    print(f"{icon} {formatted}")

if __name__ == '__main__':
    main()
