from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, null=True, blank=True)
    enterprise = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title