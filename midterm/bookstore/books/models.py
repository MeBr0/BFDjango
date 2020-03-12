from django.db import models
from django.utils import timezone


# Abstract base for both books and journal
class BookJournalBase(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    GENRES = (
        (1, 'HORROR'),
        (2, 'CLASSIC'),
        (3, 'DRAMA'),
    )

    num_pages = models.IntegerField()
    genre = models.IntegerField(choices=GENRES)


class Journal(BookJournalBase):
    TYPES = (
        (1, 'Bullet'),
        (2, 'Food'),
        (3, 'Travel'),
        (4, 'Sport'),
    )

    type = models.IntegerField(choices=TYPES)
    publisher = models.CharField(max_length=60)
