class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        _ = args[0] + ' '
        for j in self.extensions:
            if _.count('.' + j + ' '):
                return True




filenames = ['boat.jpg.jpg', 'web.png', 'txt.html', 'python.doc', 'ava.8.jpeg', 'eq_1.png', 'my.html', 'data.shtml']

acceptor = ImageFileAcceptor(('png', 'txt', 'jpg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))