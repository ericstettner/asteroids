# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  Shot.containers = (shots, updatable, drawable)

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    dt = clock.tick(60) / 1000
      
    screen.fill(000)
    updatable.update(dt)

    for item in drawable:
      item.draw(screen)

    for asteroid in asteroids:
      if asteroid.is_colliding(player):
        print("Game over!")
        sys.exit()

    pygame.display.flip()

if __name__ == "__main__":
  main()