from matplotlib import pyplot as plt

#Constants
m = 1.0
k = 10.0

#Equation of motion
def f(x) :
    return -(k/m)*x

#Plotting points
euler_x = []
euler_v = []
euler_t = []
rk4_x = []
rk4_v = []
rk4_t = []

#Eulers method
def eulers_method (x0, v0, t0, tn, h) :
    #Plotting initial points
    euler_x.append(x0)
    euler_v.append(v0)
    euler_t.append(t0)
    
    #Itterating until t = 1 second
    while (t0 < tn) :
       #Calculating new points
       xn = x0 + h*v0
       vn = v0 + h*f(x0)
       t0 = t0 + h
       x0 = xn
       v0 = vn
       #Plotting new points
       euler_x.append(x0)
       euler_v.append(v0)
       euler_t.append(t0)
    
    return x0, v0

#RK-4 method
def rk4_method (x0, v0, t0, tn, h) :
    #Plotting initial points
    rk4_x.append(x0)
    rk4_v.append(v0)
    rk4_t.append(t0)
    
    #Itterating until t = 1 second
    while (t0 < tn) :
        k1 = h*v0
        l1 = h*f(x0)
        k2 = h*(v0 + 0.5*l1)
        l2 = h*f(x0 + 0.5*k1)
        k3 = h*(v0 + 0.5*l2)
        l3 = h*f(x0 + 0.5*k2)
        k4 = h*(v0 + l3)
        l4 = h*f(x0 + k3)
        x0 = x0 + ((k1 + 2*k2 + 2*k3 + k4) / 6)
        v0 = v0 + ((l1 + 2*l2 + 2*l3 + l4) / 6)
        t0 = t0 + h
        #Plotting new points
        rk4_x.append(x0)
        rk4_v.append(v0)
        rk4_t.append(t0)
    
    return x0, v0


eulers_position, eulers_velocity = eulers_method(1, 0, 0, 1, 0.02)
rk4_position, rk4_velocity = rk4_method(1, 0, 0, 1, 0.02)

print("Euleres Method : ")
print("x(1) = ", eulers_position, "\tv(1) = ", eulers_velocity)
print("RK4 Method : ")
print("x(1) = ", rk4_position, "\tv(1) = ", rk4_velocity)

plt.figure(figsize=(8, 6))
plt.plot(euler_t, euler_x, label='Position (x)', color='blue')
plt.plot(euler_t, euler_v, label='Velocity (v)', color='red')
plt.xlabel('Time')
plt.ylabel('Position / Velocity')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(rk4_t, rk4_x, label='Position (x)', color='blue')
plt.plot(rk4_t, rk4_v, label='Velocity (v)', color='red')
plt.xlabel('Time')
plt.ylabel('Position / Velocity')
plt.legend()
plt.grid(True)
plt.show()



       