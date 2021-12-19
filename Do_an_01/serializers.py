from Do_an_01.models import Story
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response


# https://restfulapi.net/http-status-codes/
# https://www.django-rest-framework.org/api-guide/serializers/
class StorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source='category_id')

    class Meta:
        model = Story
        fields = '__all__'

    def create(self, validated_data):
        return Story.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.url = validated_data.get('url', instance.url)
        instance.content = validated_data.get('content', instance.content)
        instance.public_day = validated_data.get('public_day', instance.public_day)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
