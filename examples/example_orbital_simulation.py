# example_orbital_simulation.py
from ..core.physics import OrbitalMechanics
from ..graphics.renderer import Renderer
from astropy import units as u
import numpy as np

def simulate_orbit():
    # Initial conditions
    position = np.array([7000, 0, 0])  # km
    velocity = np.array([0, 7.8, 0])   # km/s

    # Create orbit and renderer
    orbit = OrbitalMechanics.create_orbit(position, velocity)
    renderer = Renderer()
    renderer.add_entity(position)

    # Simulation loop
    for i in range(1000):
        pos = orbit.sample(i * 10 * u.s).xyz.to(u.km).value
        renderer.render([pos])

if __name__ == '__main__':
    simulate_orbit()
