class FileAcceptor:
    def __init__(self, *args):
        self.ext = list(args)
        print(self.ext)

    def __call__(self, filename, *args, **kwargs):
        return filename[filename.rfind('.') + 1:] in self.ext

    def __add__(self, other):
        x = set(self.ext) | set(other.ext)
        return FileAcceptor(*x)



acceptor1 = FileAcceptor('jpg', 'jpeg', 'png')
acceptor2 = FileAcceptor('png', 'html')
filenames = ['agagag.jpg', 'adgag.html', 'afafasas.png', 'sss.txt']

print(list(filter(acceptor1 + acceptor2, filenames)))
