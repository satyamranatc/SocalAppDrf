from rest_framework.decorators import api_view
from rest_framework.response import Response
# Models:
from .models import Post
# Serializers:
from .serializers import PostSerializer



@api_view(['GET'])
def Blank(request):
    return Response({"message": "Hello, World!"})



# Get All Post
@api_view(['GET'])
def PostList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# create a new Post
@api_view(['POST'])
def PostCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



# Update a Post:
@api_view(['PUT'])
def PostUpdate(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# Delete a Post:
@api_view(['DELETE'])
def PostDelete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(status=204)



