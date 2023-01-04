from rest_framework import serializers
from models import Post
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only = True)
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )