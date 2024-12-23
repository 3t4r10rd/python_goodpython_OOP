class Clock:
    def __init__(self, time=0):
        if self.__check_time(time):
            self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time
    @classmethod
    def __check_time(self, tm):
        if type(tm) is int and 0 <= tm < 100000:
            return True
        else:
            return False



clock = Clock(4530)
clock.set_time(150)
print(clock.get_time())