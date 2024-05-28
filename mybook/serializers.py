from rest_framework import serializers
from .models import Author, mybook

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class mybookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = mybook
        fields = ['id', 'title', 'published_date', 'description', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = Author.objects.create(**author_data)
        book = mybook.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author = instance.author
        instance.title = validated_data.get('title', instance.title)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.description = validated_data.get('description', instance.description)
        author.name = author_data.get('name', author.name)
        author.bio = author_data.get('bio', author.bio)
        instance.save()
        author.save()
        return instance
