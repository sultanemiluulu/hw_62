from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    release_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='movies',
                                      verbose_name="Category")

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='seats', verbose_name="Hall")
    row = models.IntegerField()
    seat = models.IntegerField()


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='shows', verbose_name="Show")
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='hshows', verbose_name="Hall")
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
