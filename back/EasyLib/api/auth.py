from .serializers import UserSerializer,UserProfileSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token,created = Token.objects.get_or_create(user=user)

    # userprof = UserProfile.objects.get(user=user)
    # ser2 = UserProfileSerializer(userprof)
    return Response({'token':token.key})


@api_view(['POST'])
def logout(request):
    # print(request.auth)
    request.auth.delete()
    return Response('Successfully deleted')
