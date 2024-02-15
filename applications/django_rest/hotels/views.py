from typing import Self
from rest_framework import status
from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotels
from .serializer import HotelsSerializer


class HotelsApiView(APIView):
    """View for the hotel model."""

    # permission_classes = [permissions.IsAuthenticated]

    def get(self: Self, _request: HttpRequest) -> Response:
        """Return a list of all hotels."""
        hotels = Hotels.objects.all()
        serializer = HotelsSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self: Self, request: HttpRequest, *args, **kwargs) -> HttpResponse:  # noqa: ANN002, ARG002, ANN003
        """Create a new hotel."""
        data = {
            "name": request.data.get("name"),
            "address": request.data.get("address"),
            "phone": request.data.get("phone"),
        }
        serializer = HotelsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
