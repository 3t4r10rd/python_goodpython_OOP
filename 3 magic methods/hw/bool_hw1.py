class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0

lst_in = [
    'Балакирев; 34; 2048',
    'Mediel; 27; 0',
    'Влад; 18; 9012',
    'Nina; 33; 0'
]

players = [Player(i.split(';')[0], int(i.split(';')[1]), int(i.split(';')[2])) for i in lst_in]

players_filtered = list(filter(bool, players))

print(players_filtered)