import pygame
import keyboard
import time 
import sys
from config import *

if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.music.load("turbo_trooper_theme.wav")

    print("Controls:")
    print("\t<ctrl + c>: Quit program")
    print("\t<enter>: Dismiss alarm")

    is_working = True
    is_alarming = False

    while True:
        if is_alarming:
            if keyboard.is_pressed("enter"):
                pygame.mixer.music.stop()
                is_alarming = False
                is_working = not is_working
                if is_working:
                    sys.stdout.flush()
                    sys.stdout.write(f"\rWorking {WORK_TIME_MIN} mins.                ")
                else:
                    sys.stdout.flush()
                    sys.stdout.write(f"\rOn break for {BREAK_TIME_MIN} mins.                ")
            continue
        
        if is_working:
            time.sleep(WORK_TIME_MIN * MIN)
            is_alarming = True
            pygame.mixer.music.play()
        else:
            time.sleep(BREAK_TIME_MIN * MIN)
            is_alarming = True
            pygame.mixer.music.play()
        
        sys.stdout.flush()
        sys.stdout.write(f"\rALARM!!!                      ")
