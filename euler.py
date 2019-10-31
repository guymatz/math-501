# Written by Chris McCarthy July 2019 SIMIODE DEMARC
# Drag = 0 Student Version 
# Drag = 0 Student Version 
#===========================================  for online compilers
import matplotlib as mpl
mpl.use('Agg')
#===========================================  usual packages
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})
#============================================ constants
g = 9.8    # gravitation
m = 0.058  # mass tennis ball in kg
#============================================
class Ball:
    def __init__(self, x,y,vx,vy,t):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.t = t
        C_d = .5 # drag coefficient for tennis ball
        density_of_air = 1.21 #  kg/m^3 at 20 degrees Centigrade (68◦ F) 
        tennis_ball_radius = 0.0265 # meters;
        self.drag = (C_d * density_of_air * np.pi * tennis_ball_radius**2)/2
    def update_ball(self, delta_t,g):
        self.x = self.x + delta_t*self.vx
        self.y = self.y + delta_t*self.vy
        self.vx = self.vx + (-self.drag) * (np.sqrt(self.x**2 + self.y**2) * self.x / m) * delta_t
        self.vy = self.vy + (-g - self.drag) * (np.sqrt(self.x**2 + self.y**2) * self.y ) * delta_t
        self.t = self.t + delta_t
#============================================ initial conditions
x0 = 0      # initial x position in meters
y0 = 2      # initial y position in meters
t0 = 0      # initial time in seconds
speed = 12  # initial speed of the ball in meters/sec        
#============================================ Delta t
dt = .001 # Delta t
#============================================ Delta t
xDistance = []   # store the horizontal distance ball travelled
Theta = []       # store the angle the ball is thrown at
#============================================ run Euler for theta in [0, 90]
for theta in range(0, 91):
    vx0 = speed*np.cos(theta * np.pi/180) # initial vx
    vy0 = speed*np.sin(theta * np.pi/180) # initial vy
    ball = Ball(x0 , y0,  vx0, vy0, t0)   # initialize ball object
    while 0 <= ball.y:                    # Euler Method applied to that ball
        ball.update_ball(dt, g)
    xDistance.append(ball.x)             # collect x value when ball hits ground 
    Theta.append(theta)                  # collect theta 
#============================================ find max x distance over theta, print it
maxpos = xDistance.index(max(xDistance))
#============================================= run Euler (again) for best theta
best_theta = Theta[maxpos]
best_vx0 = speed*np.cos(best_theta * np.pi/180) # initial vx
best_vy0 = speed*np.sin(best_theta * np.pi/180) # initial vy
best_ball = Ball(x0 , y0,  best_vx0, best_vy0, t0)   # initialize ball object
xvalues = [x0]
yvalues = [y0]
times =   [t0]
while 0 <= best_ball.y:                    # Euler Method applied to that ball
    best_ball.update_ball(dt, g)
    xvalues.append(best_ball.x)
    yvalues.append(best_ball.y)
    times.append(best_ball.t)
#============================================= 
print(' ')
print(f'''
       Assuming drag = {ball.drag:.5f}. If when you throw a tennis ball you release it at
       a height of {y0}, meters and a speed of {speed} meters/second, and
       you want it to land furthest from you, you should throw the ball at an
       angle of {Theta[maxpos]} degrees: it will land about
       {np.round(max(xDistance),1)} meters away.
''')
#============================================= plot best trajectory
plt.plot(xvalues, yvalues, 'r-',linewidth=7.0)
plt.grid(linewidth='3', color='black')
plt.title('Guy Matz. Ball Trajectory. Drag=%.5f' % ball.drag, fontsize = 18)
plt.savefig('WithDragGraph.png')
