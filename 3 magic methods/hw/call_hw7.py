class Handler:
    def __init__(self, methods=('GET', )):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request, *args, **kwargs):
            r = request.get('method', 'GET')
            if r in self.methods:
                return self.__getattribute__(r.lower())(func, request)



        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


res = contact({'meth1od': 'PUT', "url": "https"})

print(res)
