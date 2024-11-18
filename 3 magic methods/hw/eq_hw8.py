class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass


class Box:
    def __init__(self):
        self.box = []

    def add_thing(self, obj):
        self.box.append(obj)

    def get_things(self):
        return self.box

    def __eq__(self, other):
        a = sorted(self.get_things(), key=lambda x: x.name)
        b = sorted(other.get_things(), key=lambda x: x.name)

        if len(a) != len(b):
            return False

        for i in a:
            step = []
            for j in b:
                if i.name == j.name and i.mass == j.mass:
                    step.append((a.index(i), b.index(j)))
            if len(step):
                print(step[0])
                x, y = step[0]
                a.pop(x)
                b.pop(y)
            else:
                return False

        return a[0].name == b[0].name and a[0].mass == b[0].mass  if len(a) > 0 else True





b1 = Box()
b2 = Box()

# b1.add_thing(Thing('тряпка', 100))
b1.add_thing(Thing('тряпка', 200))
# b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
# b2.add_thing(Thing('доска', 2000))
# b2.add_thing(Thing('тряпка', 100))


res = b1 == b2
print(res)