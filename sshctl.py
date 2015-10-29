#!/usr/bin/env python

from os import system
import curses

def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def execute_cmd(cmd_string):
	system("clear")
	a = system(cmd_string)
	print ""
	if a == 0:
		print "Command executed correctly"
	else:
		print "Command terminated with error"
	raw_input("Press enter")
	print ""

x = 0

while x != ord('4'):
	screen = curses.initscr()

	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Please enter a number...")
	screen.addstr(4, 4, "1 - Mac Mini (VNC :1)")
	screen.addstr(5, 4, "2 - Restart Apache")
	screen.addstr(6, 4, "3 - Show disk space")
	screen.addstr(7, 4, "4 - Exit")
	screen.refresh()

	x = screen.getch()

	if x == ord('1'):
		print "Connecting..."
		curses.endwin()
		execute_cmd("ssh -L 5901:localhost:5901 toor@mini")
	if x == ord('2'):
		curses.endwin()
		execute_cmd("echo 'That was just a joke!!!'")
	if x == ord('3'):
		curses.endwin()
		execute_cmd("df -h")

curses.endwin()

