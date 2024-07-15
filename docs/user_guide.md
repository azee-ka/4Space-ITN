# User Guide

## Setting Up

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run example scripts from the `examples/` directory to see the package in action.

## Examples

### Orbital Mechanics

```python
from space_sim.core.celestial import CelestialBody
from space_sim.visualization.plotter import plot_orbit

earth = CelestialBody("Earth", 5.972e24, 6371e3)
moon = CelestialBody("Moon", 7.342e22, 1737e3)
moon.position = np.array([3844e5, 0, 0])
moon.velocity = np.array([0, 1022, 0])

history = []

for _ in range(1000):
    dt = 60  # One minute time step
    force = moon.gravitational_pull(earth)
    acceleration = force / moon.mass
    moon.update_velocity(acceleration, dt)
    moon.update_position(dt)
    history.append(moon.position.copy())

plot_orbit(moon, history)
