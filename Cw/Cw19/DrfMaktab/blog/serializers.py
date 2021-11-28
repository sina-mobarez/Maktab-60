from rest_framework import serializers

from blog.models import Post, User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id' ,'username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_on', 'creator']


class PostDetailSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_on', 'creator']


class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        print(validated_data)
        return Post(**validated_data)

