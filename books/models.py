from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.IntegerField()
    category = models.ForeignKey(
        to='categories.Category',
        related_name='books',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
