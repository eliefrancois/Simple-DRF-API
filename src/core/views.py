from django.http import JsonResponse
from django.shortcuts import render

# Third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from .serializers import PostSerializer
from .models import Post


#All Methods below have same functionality but is abstracted to save time

# Method 1 of how to use

# class postView(APIView):

#     permission_classes = (IsAuthenticated, )
#     # GET: Will return all posts
#     def get(self,request,*args,**kwargs):
#         qs = Post.objects.all() #
#         serializer = PostSerializer(qs, many=True) #
#         return Response(serializer.data) #

#     def post(self,request,*args,**kwargs):
#         # POST: Will add new post to database
#         serializer = PostSerializer(data=request.data) #Passing in the data to the model

#         if serializer.is_valid(): #Checking to see that the fields in the model passed in matches what was defined in the serializer
#             serializer.save() #If vaild it will be able to save
#             return Response(serializer.data) #Returning the data after it has been posted
#         return Response(serializer.errors) #if serializer is not valid it will return the error thrown




#Method 2 
# class PostView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    # def perform_create(self,serializer)
    # # This is being overriden to do a process before saving the data passed in by the serializer
    # serializer.save()

#Method 3
# class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
    
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#Method 4
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


#Method 5 - My implementation
# class PostListCreateDeleteView(mixins.DestroyModelMixin, generics.RetrieveUpdateDestroyAPIView):
#      serializer_class = PostSerializer
#      queryset = Post.objects.all()
#      lookup_fields = ['title']

#Method 6 
# class PostDelete(generics.DestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     lookup_field = 'id'



