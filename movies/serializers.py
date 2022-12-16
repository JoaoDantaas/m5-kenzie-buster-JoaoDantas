from rest_framework import serializers
from .models import Movie, RatingMovie, MovieOrder

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(allow_null=True, default=None)
    rating = serializers.ChoiceField(allow_null=True, choices=RatingMovie.choices, default=RatingMovie.G )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField(read_only=True)

    def get_added_by(self, request):
        return request.user.email
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj: MovieOrder) -> str:
        return obj.movie.title

    def get_buyed_by(self, obj: MovieOrder) -> str:
        return obj.order.email

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)