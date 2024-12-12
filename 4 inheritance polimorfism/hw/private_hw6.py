CURRENT_OS = 'linux'   # 'windows', 'linux'

class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов

class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    CURRENT_OS = 'lol'
    def __new__(cls, title, path, exts, *args, **kwargs):
        global CURRENT_OS
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(title, path, exts)
        elif CURRENT_OS == 'linux':
            return cls.create_linux_filedialog(title, path, exts)

        return None

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)
    
    
    


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
print(type(dlg))