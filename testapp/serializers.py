from rest_framework import serializers
from django.contrib.postgres.fields import ArrayField


# Simple serializer much faster: https://hakibenita.com/django-rest-framework-slow
# In my test using this serializer gave me 1560 req/s vs 1100 req/s using the model serializer
# Classic serializer was 1600 req/s
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
