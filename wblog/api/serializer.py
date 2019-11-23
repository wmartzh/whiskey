from rest_framework import serializers

from .models import User, Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]
    ## convert data to JSON
    # validate the data passed, has a form behavior 
    
    def validate_title(self, value):
        vd = Post.objects.filter(title__iexact=value) ## instance
        #exclude itself when update the field
        if self.instance:
            vd = vd.exclude(pk = self.instance.pk)

        #check if exist
        if vd.exists():
            raise serializers.ValidationError("The title is alredy in use")
        return value