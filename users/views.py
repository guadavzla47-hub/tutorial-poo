from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

user = {
    "name": "Daniel",
    "password": "123"
}

@api_view(["GET"])
def get_user(request):
    return Response(UserSerializer(user).data)
