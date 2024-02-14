from typing import Self

from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotels
from .serializer import HotelsSerializer


class HotelsApiView(APIView):
    """View for the hotel model."""

    def get(self: Self, _request: HttpRequest) -> Response:
        """Return a list of all hotels."""
        hotels = Hotels.objects.all()
        serializer = HotelsSerializer(hotels, many=True)
        return Response(serializer.data)
