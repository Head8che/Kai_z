import pygame, time, random,
from pygame.locals import*

class snake:
  def __init__(self, point, speed):
    self.point = point
    self.speed = speed
    self.head = point[-1]
    self.tail = point[0]
  
  def move(self):
    if self.speed = 'right':
      new_point = self.head[0] + 1, self.head[1]
    elif self.speed = 'left':
      new_point = self.head[0] -1, self.head[1]
    elif self.speed = 'up':
      new_point = self.head[0], self.head[1] - 1
    elif self.speed = 'down':
      new_point = self.head[0], self.head[1] + 1
    else:
      new_point = self.head
    new_point = self.point[1] + [new_point]
    new_speed = self.speed
    return (new_point, new_speed)
    
  def direct(self):
  
    
    
    
    
    
      
      
