#angband client

import sys, curses
import Angband    #trying to keep python system includes and game includes seperate

stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(1)
curses.cbreak()
curses.curs_set(0)

#handle special keys, just in case key codes are different between systems
#Angband has it's own keys for special things like arrows and whatnot
KeyMap = { curses.KEY_UP: Angband.KEY_UP,
           curses.KEY_DOWN: Angband.KEY_DOWN,
           curses.KEY_LEFT: Angband.KEY_LEFT,
           curses.KEY_RIGHT: Angband.KEY_RIGHT
         }

go = True

game = Angband.CreateGameSession()

while go:
	#fix this so it talks to Angband game session
	stdscr.clear()
	stdscr.addch(y, x, "@")
	stdscr.refresh()
	ch = stdscr.getch()
	if(ch == 27): go = False
	elif(ch in KeyMap): game.add_key(KeyMap[ch])
	else: game.add_key(ch)

curses.curs_set(1)
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

print "Press any key to continue"
