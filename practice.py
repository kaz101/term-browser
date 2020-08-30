#!/usr/bin/env python3
'''This module is for practice using the curses module '''

import curses
import time

def main(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.addstr(0,0,'This is a string')
    stdscr.refresh()
    stdscr.erase()
    while True:
        max_y, max_x = stdscr.getmaxyx()
        stdscr.addstr(str(max_y) + '\n')
        stdscr.addstr(str(max_x))
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('b'):
            stdscr.addstr('\n b key was pressed \n')
            stdscr.refresh()


        pass
curses.wrapper(main)
