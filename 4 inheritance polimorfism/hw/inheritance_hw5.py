class Validator:
    def __init__(self, data):
        self.data = data

    def _is_valid(self, data):
        return True

    def __call__(self, data, *args, **kwargs):
        if not self._is_valid(data):
            raise ValueError('Данные не прошли валидацию')
        print('Валидация пройдена успешно!')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return type(data) == int and self.min_value <= data <= self.max_value


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return type(data) == float and self.min_value <= data <= self.max_value


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)

res1 = integer_validator(10)
res2 = float_validator(1.1)