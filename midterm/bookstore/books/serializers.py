from rest_framework import serializers

from bookstore.books.models import Book, Journal


def negative_number_validator(value):
    if value < 0:
        raise serializers.ValidationError('Number of pages cannot be negative')


# Indeed not necessary because Django's native validator
def wrong_type_validator(value):
    result = False

    for el in Journal.TYPES:
        if value == el[0]:
            result = True
            break

    if not result:
        raise serializers.ValidationError('Wrong type of journal')


class BookSerializer(serializers.ModelSerializer):

    num_pages = serializers.IntegerField(validators=[negative_number_validator])

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'description', 'created_at', 'genre', 'num_pages',)


class JournalSerializer(serializers.ModelSerializer):

    type = serializers.IntegerField(validators=[wrong_type_validator])

    class Meta:
        model = Journal
        fields = ('id', 'name', 'price', 'description', 'created_at', 'type', 'publisher',)



