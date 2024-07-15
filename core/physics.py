# core/physics.py
from astropy import units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit

class OrbitalMechanics:
    @staticmethod
    def create_orbit(position, velocity):
        pos_vector = position * u.km
        vel_vector = velocity * u.km / u.s
        return Orbit.from_vectors(Earth, pos_vector, vel_vector)
