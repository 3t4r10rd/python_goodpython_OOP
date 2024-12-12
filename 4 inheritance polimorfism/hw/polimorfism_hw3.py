class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid()')

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value


    def _is_valid(self, data):
        return type(data) == float and self.min_value <= data <= self.max_value


    def __call__(self, data, *args, **kwargs):
        return self._is_valid(data)

float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)
res_2 = float_validator(1.0)
res_3 = float_validator(-1.0)

print(res_1, res_2, res_3)