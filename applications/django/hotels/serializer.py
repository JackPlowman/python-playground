from typing import ClassVar

from rest_framework.serializers import ModelSerializer

from .models import Hotels


class HotelsSerializer(ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Hotels
        fields: ClassVar[list] = ["id", "name", "address", "phone"]
