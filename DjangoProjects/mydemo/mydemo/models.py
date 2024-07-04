from django.db import models

class User(models.Model):
    title = models.CharField(max_length=50, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='Mr')
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=250)


class Student(User):
    st_class=models.CharField( max_length=50, default='I')
    class Meta:
        db_table = 'student'
