from .serializers import UserSerializer,UserProfileSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from rest_framework import status
from .models import UserProfile


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()



@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token,created = Token.objects.get_or_create(user=user)
    is_staff = user.is_staff
    # if user.is_staff:
    #     return Response('is staff')

    return Response({'token':token.key,'is_staff':is_staff})


@api_view(['POST'])
def logout(request):
    # print(request.auth)
    request.auth.delete()
    return Response('Successfully deleted')

@api_view(['POST'])
def signup(request):
    serilizer = UserSerializer(data=request.data)
    if serilizer.is_valid():
        user = User.objects.create_user(
            username=serilizer.data['username'],
            email=serilizer.data['email'],
            password=serilizer.data['password']
        )
        userProfile = UserProfile.objects.create_user_profile(
            # website=serilizer.data['website'],
            user = user,
            # mobile=serilizer.data['mobile']
        )
        return Response(serilizer.data, status=status.HTTP_200_OK)
    return Response(serilizer.errors)
#
# class ThisUser(generics.ListAPIView):
#     serializer_class = UserProfileSerializer
#     permission_classes = (IsAuthenticated,)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def this_user(request):
    print(request.user)
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data)