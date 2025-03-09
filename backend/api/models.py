from django.db import models

# Create your models here.


class Task(models.Model):
    CATRGORY_FIELS = [
        ('work', 'work'),
        ('personal','personal'),
        ('study','study'),
        ('other','other')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=20,choices=CATRGORY_FIELS)
    due_date = models.DateField(auto_now=True)