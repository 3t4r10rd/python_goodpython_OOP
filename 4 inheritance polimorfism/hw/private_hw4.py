class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._check_data((str,), model)
        self._model = model
        self._check_data((int, float), mass)
        self._mass = mass
        self._check_data((int, float), speed)
        self._speed = speed
        self._check_data((int, float), top)
        self._top = top

    @staticmethod
    def _check_data(tp, value):
        if (type(value) not in tp) or \
                (type(value) in (int, float) and value <= 0):
            raise TypeError('неверный тип аргумента')


class PassangerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._check_data((int, float), chairs)
        self._chairs = chairs

class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._check_data((dict,), weapons)
        self._weapons = weapons


planes = [PassangerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassangerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('М', 7, 25, 2, {"а": 4, "б": 7}),
          WarPlane("С", 1, 2, 3, {"а": 4, "б": 8})]

