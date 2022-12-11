from django.urls import path

from . import views

urlpatterns = [
    path("create", views.TicketCreateView.as_view()),
    path("<pk>", views.TicketDetailView.as_view()),
    path("list", views.TicketListView.as_view()),
    path("comment/create", views.TicketCommentCreateView.as_view()),
    path("comment/list", views.TicketCommentListView.as_view()),
    path("goal_comment/<pk>", views.TicketCommentView.as_view()),
]
