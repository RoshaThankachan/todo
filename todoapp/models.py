from django.db import models

# Create your models here.


class AppUser(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.username


class Task(models.Model):
    user=models.ForeignKey(AppUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


