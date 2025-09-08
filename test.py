import numpy as np
import matplotlib.pyplot as plt

def initial_con():
    c= float(input("Constant"))
    m= 1000
    g=9.8
    t0=0
    x0= 0
    y0 = float(input("initial height"))
    v0 = float(input("initial velocity"))
    theta = float(input("angle"))
    return c,g,t0,x0,m,y0,v0,theta
initial_con()

#A function that takes in the cow’s current position and velocity vector and returns the total 
#force vector. Assume only gravity (near the earth’s surface) and wind resistance act on the cow. 
#You may assume the magnitude of the wind resistance takes the form constant * v^2, where 
#the constantshould be selectable. 
#Assume the gravitational acceleration is 9.8 m/s/s and that all units are SI.



def F(c, v, x, y):
    m= 1000
    g=9.8
    F_g= -1* m*g
    F_d= c * ( v* x**2 + v * y**2)
    
    F= F_g + F_d 
    return F

print(F(x=))

    




