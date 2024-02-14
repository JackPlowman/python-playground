from typing import ClassVar

from django.db import migrations, models


class Migration(migrations.Migration):
    """Auto-generated migration for the hotels app."""

    initial: ClassVar[bool] = True

    dependencies: ClassVar[list] = []

    operations: ClassVar[list] = [
        migrations.CreateModel(
            name="Hotels",
            fields=[
                (
                    "id",
                    models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
            ],
        ),
    ]
