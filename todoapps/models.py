from django.db import models

# Create your models here.
class Todo(models.Model):
    # title-string
    title = models.CharField(max_length=255)
    # description-string
    description = models.TextField()
    # completed-bool
    completed = models.BooleanField(default=False)
    # created-int
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title
        # return  f'created-{self.title}'


  