class SoftList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __getitem__(self, item):

        return super().__getitem__(item) if item < len(self) else False



sl = SoftList('python')
print(sl[3])
print(sl[25])