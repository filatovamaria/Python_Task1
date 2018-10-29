# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:33:30 2018

@author: Masha
"""
import math
        
class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def Module(self, position):
        return math.sqrt((self.x - position.x)**2 + (self.y - position.y)**2 + (self.z - position.z)**2)
        
    def __add__(self, p):
        return Position(self.x + p.x, self.y + p.y, self.z + p.z)
    
    def __sub__(self, p):
        return Position(self.x - p.x, self.y - p.y, self.z - p.z)
    
    def __mul__(self, alpha):
        return Position(self.x * alpha, self.y * alpha, self.z * alpha)
        
class Velocity:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
        
    def __add__(self, vel):
        return Velocity(self.u + vel.u, self.v + vel.v, self.w + vel.w)
    
    def __sub__(self, vel):
        return Velocity(self.u - vel.u, self.v - vel.v, self.w - vel.w)
    
    def __mul__(self, alpha):
        return Velocity(self.u * alpha, self.v * alpha, self.w * alpha)
    
    
    
class Particle:
    def __init__(self, position, velocity, m, color):
        self.x = position.x
        self.y = position.y
        self.z = position.z
        self.u = velocity.u
        self.v = velocity.v
        self.w = velocity.w
        self.m = m
        self.color = color 
        self.position = position
        self.velocity = velocity
        self.alive = True
        
    
        
    
        
        
    
    