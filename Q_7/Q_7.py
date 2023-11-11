import numpy as np
import matplotlib.pyplot as plt
import random

nucleus = []
time = []

def nuclear_decay_simulation(N0, p, tmax):
    t = 0
    nucleus.append(N0) 
    time.append(t)
    while t <= tmax :
        for i in range(N0) :
            if random.random() <= p :
                N0 -= 1
        nucleus.append(N0) 
        time.append(t)
        t += 1

    
# Parameters
p = 0.01
tmax = 100

# Plotting N0 = 100
nuclear_decay_simulation(100, p, tmax)
plt.figure(figsize=(10, 6))
plt.plot(time, nucleus, label='Nuclear Decay Simulation, N0 = 100', color='red')
plt.xlabel('Time')
plt.ylabel('Number of Unstable Nuclei')
plt.legend()
plt.grid(True)
plt.show()

nucleus.clear()
time.clear()

# Plotting N0 = 500
nuclear_decay_simulation(500, p, tmax)
plt.figure(figsize=(10, 6))
plt.plot(time, nucleus, label='Nuclear Decay Simulation, N0 = 500', color='red')
plt.xlabel('Time')
plt.ylabel('Number of Unstable Nuclei')
plt.legend()
plt.grid(True)
plt.show()
