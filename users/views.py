from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializers

user = {
    "username": "gpe",
    "name": "Guadalupe",
    "email": "guadavzla47@gmail.com",
    "password": "123",
    "birth_day": "2000-12-12",
    "phone": "6981170810"
}

@api_view(["GET"])
def get_user(request):
    data = UserSerializers(user).data
    birth = data['birth_day']
    return Response(data)


@api_view(["POST"])
def create_user(request):
    serialized_data = UserSerializers(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

from users.models import Users

@api_view(["GET"])
def get_users(request):
    users = Users.objects.all()
    serialized_users = UserSerializers(users, many=True)
    return Response(serialized_users.data)