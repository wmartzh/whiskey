from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import User, Post
from .serializer import UserSerializer, PostSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostView(generics.RetrieveUpdateAPIView):
   
    lookup_field = 'pk'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
    
