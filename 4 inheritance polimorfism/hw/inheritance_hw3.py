class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


# здесь объявляйте остальные классы
class DetailView(GenericView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render_request(self, request, method):
        if not (method in self.methods):
            raise TypeError('данный запрос не может быть выполнен')

        return getattr(self, method.lower())(request)
        # return self.__getattribute__(method.lower())(request)

    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if request.get('url') is None:
            raise TypeError('request не содержит обязательного ключа url')

        return f"url: {request['url']}"


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')

print(html)