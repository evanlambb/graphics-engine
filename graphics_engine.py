class Shape:
        def rotate(self, rad):
            center_x, center_y = self.center
            for i, vertex in enumerate(self.corners):
                x, y = vertex
                new_x = (x - center_x) * math.cos(rad) - (y - center_y) * math.sin(rad) + center_x
                new_y = (x - center_x) * math.sin(rad) + (y - center_y) * math.cos(rad) + center_y
                self.corners[i] = (new_x, new_y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return (self.x, self.y)
    

class Rectangle(Shape): 
    def __init__(self, x, y, width, height):
        # x and y are only used at the very beginning to initialize the starting positions
        ## they are the top left corner...
        self.x = x
        self.y = y
        self.center = (x + width / 2, y + height / 2)
        self.width = width
        self.height = height
        top_left = Point(self.x, self.y)
        top_right = Point(self.x + self.width, self.y)
        bottom_left = Point(self.x, self.y + self.height)
        bottom_right = Point(self.x + self.width, self.y + self.height)
        self.corners = [top_left.to_tuple(), top_right.to_tuple(), bottom_right.to_tuple(), bottom_left.to_tuple()]



    def draw_rect(self, screen): 
        ## i want to define 4 points for the corners. Should I just use another class and define a point? 
        pygame.draw.polygon(screen, (255, 255, 255), self.corners, width=4)

        for corner in self.corners:
            pygame.draw.line(screen, (255, 0, 0), corner, self.center, 3)
        #pygame.draw.line(screen, (255, 255, 255), top_left.to_tuple(), top_right.to_tuple(), 3)
        #pygame.draw.line(screen, (255, 255, 255), top_right.to_tuple(), bottom_right.to_tuple(), 3)
        #pygame.draw.line(screen, (255, 255, 255), bottom_right.to_tuple(), bottom_left.to_tuple(), 3)
        #pygame.draw.line(screen, (255, 255, 255), bottom_left.to_tuple(), top_left.to_tuple(), 3)
    
    



    

import pygame
import math

pygame.init()

dragging = False

#create the game window
size_x = 800
size_y = 600
screen = pygame.display.set_mode((size_x, size_y))

#player = pygame.Rect((300, 250, 50, 50))

run = True
rect = Rectangle(200, 200, 80, 60)
while run:
    
    screen.fill((0, 0, 0))

    #pygame.draw.rect(screen, (255, 0, 0), player)
    #pygame.draw.line(screen, (255, 255, 255), (0, 0), (100, 100), 10)

    
    rect.draw_rect(screen)
    pygame.time.delay(250)
    rect.rotate(1/16 * math.pi)
    #rect.draw_rect(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not dragging:
                    pygame.mouse.get_pos


                dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
    pygame.display.update()

pygame.quit()


## to draw the rectangle on the screen, I will get the corners, then draw lines between the corners 

