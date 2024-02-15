from typing import Self

from django.http import HttpRequest, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotels
from .serializer import HotelsSerializer

HOTEL_NOT_FOUND = "Object with hotel id does not exists"


class HotelsListApiView(APIView):
    """View for the hotel model."""

    # permission_classes = [permissions.IsAuthenticated]  # noqa: ERA001

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


class HotelsDetailApiView(APIView):
    """View for the hotel model."""

    # permission_classes = [permissions.IsAuthenticated]  # noqa: ERA001

    def get_object(self: Self, hotel_id: int) -> Hotels | None:
        """Helper method to get the object with given hotel_id."""
        try:
            return Hotels.objects.get(id=hotel_id)
        except Hotels.DoesNotExist:
            return None

    def get(self: Self, request: HttpRequest, hotel_id: int, *args, **kwargs) -> HttpResponse:  # noqa: ANN002, ARG002, ANN003
        """Retrieves the Hotel with given hotel_id if exists."""
        hotel_instance = self.get_object(hotel_id)
        if not hotel_instance:
            return Response({"response": HOTEL_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)

        serializer = HotelsSerializer(hotel_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self: Self, request: HttpRequest, hotel_id: int, *args, **kwargs) -> HttpResponse:  # noqa: ANN002, ARG002, ANN003
        """Updates the hotel item with given hotel_id if exists."""
        hotel_instance = self.get_object(hotel_id)
        if not hotel_instance:
            return Response({"response": HOTEL_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            "name": request.data.get("name"),
            "address": request.data.get("address"),
            "phone": request.data.get("phone"),
        }
        serializer = HotelsSerializer(instance=hotel_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self: Self, request: HttpRequest, hotel_id: int, *args, **kwargs) -> HttpResponse:  # noqa: ANN002, ARG002, ANN003
        """Deletes the hotel item with given hotel_id if exists."""
        hotel_instance = self.get_object(hotel_id)
        if not hotel_instance:
            return Response({"response": HOTEL_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
        hotel_instance.delete()
        return Response({"response": "Object deleted!"}, status=status.HTTP_200_OK)
