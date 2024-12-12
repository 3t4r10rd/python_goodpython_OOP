class Vertex:
    def __init__(self):
        self.__links = list()

    @property
    def links(self):
        return self.__links


class Link:
    def __init__(self, v1, v2):
        self.__v1 = v1
        self.__v2 = v2
        self.dist = 1

    def __setitem__(self, key, value):
        if key in ('__v1', '__v2') and type(key) != Vertex:
            raise TypeError('вершины графа должны иметь формат Vertex')
        object.__setattr__(self, key, value)

    # def __hash__(self):
    #     return (hash(self.v1) + hash(self.v2))

    def __eq__(self, other):
        return {self.v1, self.v2} == {other.v1, other.v2}

    @property
    def v1(self):
        return self.__v1

    @property
    def v2(self):
        return self.__v2

    @property
    def dist(self):
        return self.__dist

    @dist.setter
    def dist(self, value):
        self.__dist = value

class LinkedGraph:
    def __init__(self):
        self._links = list()
        self._vertex = list()

    def __check_link(self, link):
        return link not in self._links

    def add_vertex(self, v):
        if isinstance(v, Vertex) and self._vertex.count(v) == 0:
            self._vertex.append(v)

    def add_link(self, link):
        if isinstance(link, Link) and self.__check_link(link):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def _check_near_vertex(self, v):
        res = list()
        for i in self._links:
            if i.v1 == v:
                res.append(i.v2)
            elif i.v2 == v:
                res.append(i.v1)

        return res

    def _find_link(self, v1, v2):
        for i in self._links:
            if (i in v1.links) and (i in v2.links):
                return i

        return None

    def _search_link(self, links, v1, v2):

        for link in links:
            if v1 in (link.v1, link.v2) and v2 in (link.v1, link.v2):
                return link
        return None


    def _get_path(self, v, stop_v, vs = None):

        nears = self._check_near_vertex(v)
        vs.remove(v)
        if stop_v not in nears:
            for n in nears:
                if vs.count(n):
                    path, path_link = self._get_path(n, stop_v, vs)
                    if path:
                        x = [v] + path
                        y = [self._search_link(self._links, n, v)] + path_link
                        return x, y
            return [], []

        else:
            return [v, stop_v], [self._search_link(self._links, v, stop_v)]





    def find_path(self, start_v, stop_v):

        if start_v not in self._vertex or stop_v not in self._vertex:
            raise ValueError("Точки не найдены в графе.")

        if start_v == stop_v:
            return [start_v], []

        vs = self._vertex[:]

        return self._get_path(start_v, stop_v, vs)

class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self.dist = dist


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))
map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))
map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v3, v5)  # от сретенского бульвара до китай-город 1
print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7
