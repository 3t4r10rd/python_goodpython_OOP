class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView
class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if type(request) == dict and 'url' in request and 'method' in request:
            if not (request['method'] in self.allowed_methods):
                raise TypeError(f"Метод {request.get('method')} не разрешен.")
            method_request = request.get('method').lower()
        return self.__getattribute__(method_request)(request)


class DetailView(RetriveMixin, UpdateMixin, CreateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', )


view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'POST'})
print(html)   # GET: https://stepik.org/course/116336/

# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})