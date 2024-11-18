class BookStudy:
    def __init__(self,  name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name, self.author))


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021'
]

lst_bs = [BookStudy(*i) for i in [map(str.strip, j.split(';')) for j in lst_in]]

unique_books = len(set(hash(i) for i in lst_bs))

print(unique_books)