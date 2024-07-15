# space_simulation/space_sim/core/celestial.py

import numpy as np

class CelestialBody:
    def __init__(self, name, mass, radius):
        self.name = name
        self.mass = mass  # in kg
        self.radius = radius  # in meters
        self.position = np.zeros(3)  # Initial position vector
        self.velocity = np.zeros(3)  # Initial velocity vector

    def update_position(self, dt):
        # Update position based on current velocity and dt (time step)
        self.position += self.velocity * dt

    def update_velocity(self, acceleration, dt):
        # Update velocity based on current acceleration and dt (time step)
        self.velocity += acceleration * dt

    def gravitational_pull(self, other_body):
        # Calculate gravitational force between this body and another body
        G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
        r_vector = other_body.position - self.position
        r_mag = np.linalg.norm(r_vector)
        force_mag = G * self.mass * other_body.mass / r_mag**2
        force_vector = force_mag * r_vector / r_mag
        return force_vector
