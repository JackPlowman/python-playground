from typing import Self

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotels
from .serializer import HotelsSerializer


class HotelsApiView(APIView):
    """View for the hotel model."""

    # permissions_classes = [permissions.IsAuthenticated]

    def get(self: Self, request) -> Response:
        """Return a list of all hotels."""
        hotels = Hotels.objects.all()
        serializer = HotelsSerializer(hotels, many=True)
        return Response(serializer.data)
