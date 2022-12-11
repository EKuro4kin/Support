from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, filters
from rest_framework.generics import CreateAPIView, ListAPIView

from tickets.models import Ticket, TicketComment
from tickets.serializers import TicketListSerializer, TicketCreateSerializer, TicketSerializer, \
    TicketCommentCreateSerializer, TicketCommentSerializer


class TicketCreateView(CreateAPIView):
    model = Ticket
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketCreateSerializer


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    model = Ticket
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]


class TicketListView(ListAPIView):
    queryset = Ticket.objects.all()
    model = Ticket
    serializer_class = TicketListSerializer
    permission_classes = [permissions.IsAuthenticated]


class TicketCommentCreateView(CreateAPIView):
    model = TicketComment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketCommentCreateSerializer


class TicketCommentListView(generics.ListAPIView):
    queryset = TicketComment.objects.all()
    model = TicketComment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketCommentSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]


class TicketCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketComment.objects.all()
    model = TicketComment
    serializer_class = TicketCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return TicketComment.objects.filter(user=self.request.user)

