from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    icon = serializers.CharField(max_length=150)
    color = serializers.CharField(max_length=100)
    # author_id = serializers.IntegerField()


    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.color = validated_data.get('color', instance.color)
        # instance.author = validated_data.get('author_id', instance.author)

        instance.save()
        return instance
