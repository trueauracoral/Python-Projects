#!/usr/bin/env python
from curses import wrapper
import time

def main(scr):
    scr.box()

    scr.addstr("skibidi dib dib dom dom y es yes")
    scr.refresh()
    c = scr.getch()

wrapper(main)
