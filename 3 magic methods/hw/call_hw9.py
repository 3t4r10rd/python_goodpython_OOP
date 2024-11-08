class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))

        return wrapper


class RenderDigit:
    def __call__(self, *args, **kwargs):
        value = args[0]
        if value[0] == '-' and value[1::].isdigit() or value.isdigit():
            return int(value)


render = RenderDigit()

input_dg = InputValues(RenderDigit())
input_dg = input_dg(input)
res = input_dg()
print(res)
