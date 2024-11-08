class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list


    def __call__(self, x, *args, **kwargs):
        s = 'ol' if self.type_list == 'ol' else 'ul'
        res = ['<' + s + '>']
        for i in x:
            res.append('<li>' + i + '</li>')
        res.append('</' + s + '>')

        return '\n'.join(res)



lst = ['Пункт1', 'Пункт2', 'Пункт3']
render = RenderList('ol')
html = render(lst)
print(html)