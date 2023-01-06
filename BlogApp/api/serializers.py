from rest_framework import serializers
from BlogApp.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )

class UserSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    # Post는 현재 User와 역참조 관계다. serializer에서 자동으로 추가되지 않아!
    # 따라서 명백히 선언해줄 필요가 있다! >> model의 owner필드에서 설정한 related_name 속성으로 찾을 수 있다.
    class Meta:
        model = User
        fields = ('id', 'username', 'post')
