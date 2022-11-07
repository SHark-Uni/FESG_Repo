from django.db import models
from common.models import CommonModel

# Create your models here.
class Review(CommonModel):

    """Review From a User to a Room or Experiences"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    payload = models.TextField()
    stars = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user}/{self.stars}⭐"
