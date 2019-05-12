from django.db import models


class Purchaser(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    purchaser = models.ForeignKey(
        to='purchasers.Purchaser',
        related_name='purchase',
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        to='books.Book',
        related_name='purchase',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.book.name
