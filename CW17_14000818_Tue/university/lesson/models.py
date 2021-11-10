from django.db import models

# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=120)
    unit = models.IntegerField()
    description = models.TextField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    


class College(models.Model):
    title = models.CharField(max_length=30)
    student = models.ForeignKey('person.Student', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('person.Teacher', on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
