from django.db import models

class post(models.Model):
    userid = models.IntegerField()
    content = models.TextField()
    datetime = models.TextField()

    def __str__(self):
        return f"{self.content}"

    class Meta:
        db_table = 'post'
