from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quote
from .serializers import QuoteSerializer
import random

@api_view(["GET"])
def get_random_quote(request):
    quotes = list(Quote.objects.all())
    if not quotes:
        return Response({"Error": "No quotes found"}, status=404)
    random_quote = random.choice(quotes)
    serializer = QuoteSerializer(random_quote)
    return Response(serializer.data)


