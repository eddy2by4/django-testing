from django.http import JsonResponse, HttpResponse
import ujson

from testapp.models import Book
from testapp.serializers import BookSerializer


def db(request):
    book = Book.objects.filter(pk=1)
    serializer = BookSerializer(book, many=True)

    return HttpResponse(ujson.dumps(serializer.data), content_type="application/json")


def index(request):
    return HttpResponse(ujson.dumps({"test": "1"}), content_type="application/json")
