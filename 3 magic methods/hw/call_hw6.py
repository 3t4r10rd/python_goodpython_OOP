class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def __call__(self, request, *args, **kwargs):
        res = request.get('method', 'GET')
        if res == 'GET':
            return self.get(self.__fn, request)


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({'method': 'GET', "url": "https"})

print(res)
