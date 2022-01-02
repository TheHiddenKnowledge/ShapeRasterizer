import pygame
import pygame.gfxdraw
import random
import math
pygame.init()
field = pygame.display.set_mode((800,400))
finished = False
class Polygon:
    def __init__(self,x,y,l,n):
        self.x=x
        self.y=y
        self.l=l
        self.n=n
        self.off=0
        self.startpoints = [0]*n
        self.edgepoints = []
        self.insidepoints = []
    def createpoints(self):
        for r in range(self.n):
            self.startpoints[r]=([int(self.x+self.l*math.cos(r*math.pi*2/self.n+self.off)), int(self.y+self.l*math.sin(r*math.pi*2/self.n+self.off))])
    def createlines(self,p2,p1):
            temp = []
            dx = 0
            dy = 0 
            for n in range(int(abs(p2[0]-p1[0]))):
                slope = (p2[1]-p1[1])/(p2[0]-p1[0])
                if p2[0]-p1[0]>0:
                    dx = p1[0]+n
                    dy = int(p1[1]+slope*n)
                elif p2[0]-p1[0]<0:
                    dx = p1[0]-n
                    dy = int(p1[1]-slope*n)
                temp.append([dx,dy])
                pygame.gfxdraw.pixel(field,dx,dy,(255,0,255))
            for n in range(int(abs(p2[1]-p1[1]))):
                slope = (p2[0]-p1[0])/(p2[1]-p1[1])
                if p2[1]-p1[1]>0:
                    dy = p1[1]+n
                    dx = int(p1[0]+slope*n)
                elif p2[1]-p1[1]<0:
                    dy = p1[1]-n
                    dx = int(p1[0]-slope*n)
                temp.append([dx,dy])
                pygame.gfxdraw.pixel(field,dx,dy,(255,0,255))
            return temp
    def load(self):
        self.createpoints()
        for k in range(self.n):
            self.edgepoints.append(self.createlines(self.startpoints[k],self.startpoints[k-1]))
            for j in range(len(self.edgepoints[k])):
                if j%1 == 0:
                    self.createlines(self.edgepoints[k][j],self.edgepoints[0][0])
        self.edgepoints.clear()
        self.insidepoints.clear()
shape = Polygon(200,200,50,4)
shape1 = Polygon(400,200,50,7)
shape2 = Polygon(600,200,50,11)
clock = pygame.time.Clock()
while not finished:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                finished = True
                field.fill((0,0,0))
                shape.load()
                shape.off += math.pi/250
                shape1.load()
                shape1.off += math.pi/250
                shape2.load()
                shape2.off += math.pi/250
                pygame.display.flip()


