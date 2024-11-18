class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ["Системный блок: 1500 75890.56", "Монитор Samsung: 2000 34000",
       "Клавиратура: 200.44 545", "Монитор Samsung: 2000 34000"]

def get_item(x):
    a = str(x[:x.rfind(':')])
    b = x[x.rfind(':')+2:x.rfind(' ')]
    c = x[x.rfind(' ')+1:]

    b = float(b) if b.count('.') else int(b)
    c = float(c) if c.count('.') else int(c)

    return [a, b, c]

def get_hashes(val, lst):
    res = 0
    for i in lst:
        res += 1 if hash(val) == hash(i) else 0
    return res


# shop_items = list(map(lambda x: ShopItem(*x), list(map(get_item, lst_in))))

lst = list(map(lambda x: ShopItem(*x), list(map(get_item, lst_in))))
shop_items = dict((i, [i, get_hashes(i, lst)]) for i in lst)

# for i in range(len(shop_items)):
#     d.setdefault(shop_items[i], [shop_items[i], get_hashes(shop_items[i], shop_items)])

print(shop_items)