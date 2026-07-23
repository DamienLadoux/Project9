from django.urls import path
from . import views

urlpatterns = [
    path("", views.feed, name="feed"),
    path("ticket/create/", views.create_ticket, name="create_ticket"),
    path(
        "review/create/<int:ticket_id>/",
        views.create_review,
        name="create_review",
    ),
]
