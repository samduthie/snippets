from django.db import connection

'''
https://docs.djangoproject.com/en/dev/faq/models/#how-can-i-see-the-raw-sql-queries-django-is-running
'''

print(connection.queries)

model_query = MyModel.objects.all().query

set_query = MyModel.objects.filter(type__name=='').query

set_query = model.type_set().query

print(connection.queries)

