from webapp.models import Movie
from webapp.models import Show
from webapp.models import Seat
from webapp.models import Category
from webapp.models import Hall
from rest_framework import viewsets
from api_v1.serializers import MovieSerializer
from api_v1.serializers import ShowSerializer
from api_v1.serializers import SeatSerializer
from api_v1.serializers import CategorySerializer
from api_v1.serializers import HallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-release_date')
    serializer_class = MovieSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all().order_by('name')
    serializer_class = HallSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all().order_by('row')
    serializer_class = SeatSerializer


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all().order_by('price')
    serializer_class = ShowSerializer

