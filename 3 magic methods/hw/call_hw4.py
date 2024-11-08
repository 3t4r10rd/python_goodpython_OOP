class DigitRetrieve:

    def __call__(self, *args, **kwargs):
        return int(args[0]) if args[0].isdigit() or (len(args[0].split('-')) == 2 and args[0].split('-')[1].isdigit()) else None


dg = DigitRetrieve()

st = ['123', 'abc', '-55.4', '0', '5']
digits = list(map(dg, st))

print(digits)