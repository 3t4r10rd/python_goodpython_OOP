# 1----------------------------------------------
class TravelBlog:
    total_blogs = 0

tb1 = TravelBlog()

tb1.name = 'Франция'
tb1.days = 6

TravelBlog.total_blogs += 1

tb2 = TravelBlog()

tb2.name = 'Италия'
tb2.days = 5

TravelBlog.total_blogs += 1

print(getattr(TravelBlog,'total_blogs'))

# 2--------------------------------------------------

class Figure:
    type_fig = 'ellipse'
    color = 'red'


fg1 = Figure()
fg1.start_pt = (10, 5)
fg1.end_pt = (100, 20)
fg1.color = 'blue'

delattr(fg1, 'color')

print(*fg1.__dict__)

# 3----------------------------------------------------

class Person:
    name = "Имя"
    job = 'Программист'
    city = 'Москва'

p1 = Person()

print('job' in p1.__dict__)
print(hasattr(p1, 'job'))
