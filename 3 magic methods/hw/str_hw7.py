class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2


    def __len__(self):
        return max(self.clock1.get_time() - self.clock2.get_time(), 0)

    def __str__(self):
        dx = self.__len__()
        if dx <= 0:
            return 0
        h = dx // 3600
        m = dx % 3600 // 60
        s = dx % 3600 % 60
        return f"{h:02}:{m:02}:{s:02}"


dt = DeltaClock(Clock(2, 45, 0), Clock (1, 15, 0))
print(dt)
print(len(dt))
