from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    publication_date = models.CharField(max_length=30)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title