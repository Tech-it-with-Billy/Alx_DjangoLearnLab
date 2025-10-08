from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user, context={'request': request}).data
        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        header = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=header)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        userdata = UserSerializer(user, context={'request': request}).data
        return Response({'token': token.key, 'user': userdata}, status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_object(self):
        return self.request.user

class FollowUnfollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, username, *args, **kwargs):
        try:
            target_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if target_user == request.user:
            return Response({'detail': 'You cannot follow/unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user in target_user.followers.all():
            target_user.followers.remove(request.user)
            action = 'unfollowed'
        else:
            target_user.followers.add(request.user)
            action = 'followed'
        
        return Response({'detail': f'You have {action} {target_user.username}.'}, status=status.HTTP_200_OK)