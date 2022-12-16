from rest_framework.views import APIView, Response, Request
from .serializers import UserSerializer
from .permissions import PermissionIsSuper
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .models import User


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, 201)

class RetrieveUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionIsSuper]

    def get(self, request, user_id: int):
        users = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, users)

        serializer = UserSerializer(users)

        return Response(serializer.data)