from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def Login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(username, password)

    if username is None or password is None:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(UserName=username).first()

    if user is None:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_404_NOT_FOUND)

    if user.Password != password:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user)
    return Response(serializer.data)

   



@api_view(['POST'])
def Register(request):
    serializer = UserSerializer(data=request.data)
    print(
        request.data.get('FullName'),
        request.data.get('ProfilePic'),
        request.data.get('UserName'),
        request.data.get('Password')
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)