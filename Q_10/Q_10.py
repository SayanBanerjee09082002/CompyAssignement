import numpy as np
import matplotlib.pyplot as plt

 # Boltzmann constant
kB = 1.380649 * 10**-23 
# Mass of the particle
mass = 1.0  

# Parameters
num_particles = 1000
steps = 1000
dt = 0.1

# Initial conditions
velocities = np.ones(num_particles)

#Distribution array
speed_distribution_data = []

for step in range(steps):
    velocities += np.sqrt(kB*dt / mass) * np.random.normal(size=num_particles)
    if step % 10 == 0:
        speed_distribution_data.append(np.copy(velocities))

# Plotting the speed distribution
bins = np.linspace(0, 4, 50)
plt.hist(speed_distribution_data[-1], bins=bins, density=True, label='Simulation')
plt.xlabel('Speed')
plt.ylabel('Probability Density')
plt.title('Speed Distribution of a Dilute Gas')
plt.legend()
plt.show()