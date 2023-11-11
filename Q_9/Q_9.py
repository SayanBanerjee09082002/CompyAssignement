import numpy as np
import matplotlib.pyplot as plt

# Constants
a = 10
c = 8 / 3

# ODE Functions
def fx(x, y, t):
    return a * (y - x)

def fy(x, y, z, t, b):
    return -x * z + b * x - y

def fz(x, y, z, t):
    return x * y - c * z

# Plot points
x = []
y = []
z = []
t = []

# RK-4 Solver Method
def rk4(x0, y0, z0, t0, tn, h, b):
    x.append(x0)
    y.append(y0)
    z.append(z0)
    t.append(t0)
    while t0 <= tn:
        k1x = h * fx(x0, y0, t0)
        k1y = h * fy(x0, y0, z0, t0, b)
        k1z = h * fz(x0, y0, z0, t0)

        k2x = h * fx(x0 + h/2, y0 + h/2, t0 + k1x/2)
        k2y = h * fy(x0 + h/2, y0 + h/2, z0 + h/2, t0 + k1y/2, b)
        k2z = h * fz(x0 + h/2, y0 + h/2, z0 + h/2, t0 + k1z/2)

        k3x = h * fx(x0 + h/2, y0 + h/2, t0 + k2x/2)
        k3y = h * fy(x0 + h/2, y0 + h/2, z0 + h/2, t0 + k2y/2, b)
        k3z = h * fz(x0 + h/2, y0 + h/2, z0 + h/2, t0 + k2z/2)

        k4x = h * fx(x0 + h, y0 + h, t0 + k3x)
        k4y = h * fy(x0 + h, y0 + h, z0 + h, t0 + k3y, b)
        k4z = h * fz(x0 + h, y0 + h, z0 + h, t0 + k3z)

        x0 = x0 + (k1x + k2x + k3x + k4x) / 6
        y0 = y0 + (k1y + k2y + k3y + k4y) / 6
        z0 = z0 + (k1z + k2z + k3z + k4z) / 6
        t0 = t0 + h

        x.append(x0)
        y.append(y0)
        z.append(z0)
        t.append(t0)

# Plotting (a) b = 5
rk4(1, 0, 0, 0, 50, 0.01, 5)
plt.figure(figsize=(8, 6))
plt.plot(t, z, label='Solution (a) for b = 5', color='red')
plt.xlabel('Time')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.show()

x.clear()
y.clear()
z.clear()
t.clear()

# Plotting (a) b = 10
rk4(1, 0, 0, 0, 50, 0.01, 10)
plt.figure(figsize=(8, 6))
plt.plot(t, z, label='Solution (a) for b = 15', color='red')
plt.xlabel('Time')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.show()

x.clear()
y.clear()
z.clear()
t.clear()

# Plotting (a) b = 25
rk4(1, 0, 0, 0, 50, 0.01, 25)
plt.figure(figsize=(8, 6))
plt.plot(t, z, label='Solution (a) for b = 25', color='red')
plt.xlabel('Time')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.show()

#Plotting (b)
plt.figure(figsize=(8, 6))
plt.plot(x, z, label='Solution (b)', color='red')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.show()

x.clear()
y.clear()
z.clear()
t.clear()

#Plotting (c)
rk4(0, 0, 0, 0, 50, 0.01, 25)
plt.figure(figsize=(8, 6))
plt.plot(y, z, label='Solution (c)', color='red')
plt.xlabel('y')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.show()

#Plotting (d)
plt.figure(figsize=(8, 6))
plt.plot(x, z, label='Solution (c)', color='red')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.show()