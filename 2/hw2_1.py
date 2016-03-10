from sys import stdin

EMPTY = 0
ROCK = 1
FISH = 2
SHRIMP = 3


class Entity:

    def evolve(self, _):
        raise Exception("This is an abstract entity")

    def create(entity_type):
        if entity_type == 0:
            return Empty()
        if entity_type == 1:
            return Rock()
        if entity_type == 2:
            return Fish()
        if entity_type == 3:
            return Shrimp()
        raise Exception("Unrecognized etype - {}".format(entity_type))
    create = staticmethod(create)


class Empty(Entity):

    def __init__(self):
        self.etype = EMPTY

    def evolve(self, neighbors):
        if neighbors[FISH] == 3:
            return Fish()
        if neighbors[SHRIMP] == 3:
            return Shrimp()
        return self


class Rock(Entity):

    def __init__(self):
        self.etype = ROCK

    def evolve(self, _):
        return self


class Fish(Entity):

    def __init__(self):
        self.etype = FISH

    def evolve(self, neighbors):
        if neighbors[FISH] in {2, 3}:
            return self
        return Empty()


class Shrimp(Entity):

    def __init__(self):
        self.etype = SHRIMP

    def evolve(self, neighbors):
        if neighbors[SHRIMP] in {2, 3}:
            return self
        else:
            return Empty()


def main():

    simcount = int(stdin.readline())
    height, width = map(int, stdin.readline().split())

    field = {}
    new_field = {}

    for i, line in enumerate(stdin):
        for j, el in enumerate(line.split()):
            field[i, j] = Entity.create(int(el))
    for iteration in range(0, simcount):
        for x, y in field.iterkeys():
            types = [0] * 4
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if (i, j) in field and (i, j) != (x, y):
                        types[field[i, j].etype] += 1
            new_field[x, y] = field[x, y].evolve(types)
        field, new_field = new_field, field

    output(field, width, height)


def output(field, width, height):
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(str(field[i, j].etype))
        print(' '.join(line))

if __name__ == '__main__':
    main()
