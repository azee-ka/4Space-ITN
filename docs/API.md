
#### 2. `API.md`

```markdown
# API Documentation

## Modules

### `space_sim.core`

#### `CelestialBody`

- `__init__(name, mass, radius)`: Initialize a celestial body.
- `update_position(dt)`: Update the position based on velocity and time step.
- `update_velocity(acceleration, dt)`: Update the velocity based on acceleration and time step.
- `gravitational_pull(other_body)`: Calculate the gravitational force between this body and another body.

#### `Spacecraft`

- `__init__(name, mass, max_thrust)`: Initialize a spacecraft.
- `update_position(dt)`: Update the position based on velocity and time step.
- `update_velocity(acceleration, dt)`: Update the velocity based on acceleration and time step.
- `apply_thrust(thrust_vector, dt)`: Apply thrust to change velocity.

### `space_sim.visualization`

#### `plot_orbit(celestial_body, history)`

- Plot the orbit of a celestial body from its history of positions.

### `space_sim.data`

#### `SpiceInterface`

- `__init__(kernel_path)`: Initialize the SPICE interface with a kernel file.
- `load_kernel()`: Load the SPICE kernel.
- `get_orbital_elements(body_name, time)`: Retrieve orbital elements from the SPICE kernel.
- `calculate_position(body_name, time)`: Calculate the position of a celestial body.

### `space_sim.optimization`

#### `GeneticAlgorithm`

- `__init__(population_size, mutation_rate)`: Initialize the genetic algorithm.
- `initialize_population()`: Initialize the population with random solutions.
- `select_parents()`: Select parents based on fitness for crossover.
- `crossover(parent1, parent2)`: Perform crossover to create new solutions.
- `mutate(offspring)`: Mutate offspring to maintain diversity.
- `evolve()`: Evolve the population using selection, crossover, and mutation.
