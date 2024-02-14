from typing import Self

from django.db import models


class Hotels(models.Model):
    """This class represents the hotel model."""

    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self: Self) -> str:
        """Return a human readable representation of the model instance."""
        return f"Hotel: {self.name} Address: {self.address[:20] if len(self.address) > 20 else self.address}"
