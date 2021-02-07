from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    tasks = models.OneToManyField('Task')
    isTeacher = models.BooleanField(default=False)


class Task(models.Model):
    professor = models.ForeignKey(User)

    subject = models.CharField(max_length=50)
    taskContents = models.CharField()

    releaseDate = models.DateField()

    timePeriod = models.IntegerField()
    grade = models.IntegerField()
    penalty = models.IntegerField()


# class Ownership(models.Model):
#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     buy_date = models.DateField(blank=True, null=True)
#     sell_date = models.DateField(blank=True, null=True)
#
# class Licence(models.Model):
#     TYPES = (
#         ('A', 'Motocycle'),
#         ('B', 'Car'),
#         ('C', 'Truck'),
#         ('D', 'Bus')
#     )
#     licence_id = models.IntegerField()
#     licence_date = models.DateField()
#     type = models.CharField(max_length=1, choices=TYPES)
#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


