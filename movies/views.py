from rest_framework.views import APIView, Response, Request
from rest_framework.pagination import PageNumberPagination
from .permissions import PermissionIsSuper, PermissionToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from django.shortcuts import get_object_or_404

class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionIsSuper]

    def post(self, request: Request) -> Response:

        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, 201)
    
    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request, view=self)
        movie_serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(movie_serializer.data)

class MovieViewId(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionIsSuper]

    def get(self, request:Request, movie_id: int ) -> Response:
        movies = get_object_or_404(Movie, id=movie_id)

        movie_serializer = MovieSerializer(movies)

        return Response(movie_serializer.data, 200)

    def delete(self, request: Request, movie_id: int) -> Response:
        movies = get_object_or_404(Movie, id=movie_id)

        movies.delete()

        return Response(status=204)

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionToken]

    def post(self, request: Request, movie_id: int) -> Response:
        
        movie_obj = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie_obj, order=request.user)

        return Response(serializer.data, 201)