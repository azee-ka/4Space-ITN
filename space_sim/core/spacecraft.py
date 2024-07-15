# space_simulation/space_sim/core/spacecraft.py

import numpy as np

class Spacecraft:
    def __init__(self, name, mass, max_thrust):
        self.name = name
        self.mass = mass  # in kg
        self.max_thrust = max_thrust  # in Newtons (N)
        self.position = np.zeros(3)  # Initial position vector
        self.velocity = np.zeros(3)  # Initial velocity vector

    def update_position(self, dt):
        # Update position based on current velocity and dt (time step)
        self.position += self.velocity * dt

    def update_velocity(self, acceleration, dt):
        # Update velocity based on current acceleration and dt (time step)
        self.velocity += acceleration * dt

    def apply_thrust(self, thrust_vector, dt):
        # Apply thrust to change velocity
        thrust = np.linalg.norm(thrust_vector)
        if thrust > self.max_thrust:
            raise ValueError("Thrust exceeds spacecraft's maximum capability.")
        acceleration = thrust_vector / self.mass
        self.velocity += acceleration * dt
