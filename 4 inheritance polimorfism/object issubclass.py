class Geom:
    pass

# то же самое, что

class Geom(object):
    pass



class new_list(list):
    def __str__(self):
        return " ".join(map(str, self))

v = new_list([1, 2, 3])
print(v)