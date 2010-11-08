#WindowsClient.py
import os, sys
import pygame
from pygame.locals import *

from Angband import *

class WindowsClient:
    def __init__(self):
        window_size = (800, 600)
        pygame.init()
        self._screen = pygame.display.set_mode(window_size, 0, 8)
        pygame.display.set_caption('pyAngband Alpha 0.1 Win-pyGame')
        self._bgcolor = (100, 100, 100)
        self._screen.fill(self._bgcolor)
        self._running = True
        self._font_size = 30
        
        self._font = pygame.font.Font('VeraMoBd.ttf', self._font_size)
        if(not self._font):
            print("Font not loaded!")
            exit()
        metric = self._font.metrics('@')[0]
        self._font_w = metric[4]
        self._font_h = self._font_size
        
    def putch_at(self, char, x, y, color):
        drawme = self._font.render(char, True, color, self._bgcolor)
        self._screen.blit(drawme, (x * self._font_w, y * self._font_h))
    
    def puts_at(self, str, x, y, color):
        drawme = self._font.render(str, True, color, self._bgcolor)
        self._screen.blit(drawme, (x * self._font_w, y * self._font_h))
    
    def erase_at(self, len, x, y, color = None):
        erase_me = pygame.Surface((len * self._font_w, self._font_h), 0, 8)
        if not color:
            erase_me.fill(self._bgcolor)
        else:
            erase_me.fill(color)
        self._screen.blit(erase_me, (x * self._font_w, y * self._font_h))
        
    def run(self):
        game = Angband()
        while(self._running):
            game.process_world()
            if(not game.running()):
                self._running = False
            else:
                disp = game.get_current_display()
                self._screen.fill(self._bgcolor, Rect(0, 0, 800, 600))
                self.putch_at(disp[0], disp[1], disp[2], (0, 0, 0))
                
                pygame.display.update()
                
                events = pygame.event.get()
                for e in events:
                    if(e.type == QUIT):
                        game.shutdown()
                        self._running = False
                        break
                    elif(e.type == KEYDOWN):
                        sh = (e.mod & KMOD_SHIFT == KMOD_SHIFT)
                        alt = (e.mod & KMOD_ALT == KMOD_ALT)
                        ctrl = (e.mod & KMOD_CTRL == KMOD_CTRL)
                        if(e.key == K_ESCAPE):
                            game.add_key((AKEY_ESCAPE, sh, ctrl, alt))
                        elif(e.key == K_UP):
                            game.add_key((AKEY_UP, sh, ctrl, alt))
                        elif(e.key == K_DOWN):
                            game.add_key((AKEY_DOWN, sh, ctrl, alt))
                        elif(e.key == K_LEFT):
                            game.add_key((AKEY_LEFT, sh, ctrl, alt))
                        elif(e.key == K_RIGHT):
                            game.add_key((AKEY_RIGHT, sh, ctrl, alt))
                        elif(e.key == K_KP0):
                            game.add_key(('0', sh, ctrl, alt))
                        elif(e.key == K_KP1):
                            game.add_key(('1', sh, ctrl, alt))
                        elif(e.key == K_KP2):
                            game.add_key(('2', sh, ctrl, alt))
                        elif(e.key == K_KP3):
                            game.add_key(('3', sh, ctrl, alt))
                        elif(e.key == K_KP4):
                            game.add_key(('4', sh, ctrl, alt))
                        elif(e.key == K_KP5):
                            game.add_key(('5', sh, ctrl, alt))
                        elif(e.key == K_KP6):
                            game.add_key(('6', sh, ctrl, alt))
                        elif(e.key == K_KP7):
                            game.add_key(('7', sh, ctrl, alt))
                        elif(e.key == K_KP8):
                            game.add_key(('8', sh, ctrl, alt))
                        elif(e.key == K_KP9):
                            game.add_key(('9', sh, ctrl, alt))
                        
                        
if(__name__ == '__main__'):
    client = WindowsClient()
    client.run()