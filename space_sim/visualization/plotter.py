# space_simulation/space_sim/visualization/plotter.py

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_orbit(celestial_body, history):
    # Plot the orbit of a celestial body from its history of positions
    x = [pos[0] for pos in history]
    y = [pos[1] for pos in history]
    z = [pos[2] for pos in history]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label=celestial_body.name)
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.set_title(f'Orbit of {celestial_body.name}')
    ax.legend()
    plt.show()
