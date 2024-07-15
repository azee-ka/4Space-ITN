# graphics/renderer.py
from vpython import sphere, vector, rate

class Renderer:
    def __init__(self):
        self.entities = []

    def add_entity(self, position, radius=1):
        entity = sphere(pos=vector(*position), radius=radius)
        self.entities.append(entity)

    def update(self, positions):
        for entity, pos in zip(self.entities, positions):
            entity.pos = vector(*pos)

    def render(self, positions):
        rate(50)
        self.update(positions)
