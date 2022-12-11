from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView


from users.serializers import UserSerializer, UserCreateSerializer

USER_MODEL = get_user_model()


class UserCreateView(CreateAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserCreateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserSerializer

