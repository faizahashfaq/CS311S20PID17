from django.db import models


# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=20)
    sections = models.SmallIntegerField()
    dwk = models.SmallIntegerField(default=7, editable=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=35)
    crtHours = models.SmallIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Class = models.ManyToManyField(Class, default=None)
    count = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    rooms: int = models.IntegerField()


class Users(models.Model):
    organization = models.CharField(max_length=130)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    @property
    def __str__(self):
        return self.username


class Timetable(models.Model):
    Class = models.ForeignKey(Class, default=None, on_delete=models.CASCADE)


class TimeSlot(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    teacher = models.CharField(max_length=50,null=True)
    room = models.SmallIntegerField(null=True)
    section = models.SmallIntegerField(null=True)
    day = models.SmallIntegerField(null=True)
    period = models.SmallIntegerField(null=True)
    Timetable = models.ForeignKey(Timetable,null=True, default=None, on_delete=models.CASCADE)

    def addFree(self, FreeRooms, i, j):
        self.FreeRooms = FreeRooms
        self.i = i
        self.j = j

    def getTime(self):
        z = self.i
        y = self.j
        return z, y

