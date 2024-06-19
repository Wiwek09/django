from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializer import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse 
from .models import User
import hashlib
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import gridfs

# authentication
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@api_view(['POST'])
@csrf_exempt
def signup_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Hash the password
        password = serializer.validated_data['password']
        hashed_password = hash_password(password)
        serializer.validated_data['password'] = hashed_password
        # Save the user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'}, status=400)
    
    try:
        user = User.objects.get(email=email)
        if hash_password(password) == user.password:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@csrf_exempt
def logout_view(request):
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    

# file upload

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES['file']
            fs = gridfs.GridFS(settings.MONGO_DB)
            file_id = fs.put(file.read(), filename=file.name)

            # Save file metadata in MongoDB
            settings.FILES_COLLECTION.insert_one({
                'filename': file.name,
                'file_id': file_id
            })

            return Response({'message': 'File uploaded successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)