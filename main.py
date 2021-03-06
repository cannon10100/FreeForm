#!/usr/bin/python
import pygame
import sys

import event_handler
import gui
import entity_pool
import text_box


def run(width=1920, height=1080):
    """Main run method"""

    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.toggle_fullscreen()

    clock = pygame.time.Clock()
    pool = entity_pool.EntityPool()
    box = text_box.TextBox(screen, pool)
    handler = event_handler.EventHandler(pool, box)
    outer_gui = gui.Gui(width, height)

    #Main logic loop
    while 1:
        screen.fill((137, 207, 255))
        handler.handle(pygame.event.get())
        delta = clock.tick()

        pool.update(delta)
        pool.render(screen)
        box.render()
        outer_gui.render(screen)

        pygame.display.flip()


def clean_exit():
    """Method to do final cleanup (if needed) before exiting"""
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        run(int(sys.argv[1]), int(sys.argv[2]))
    else:
        run()