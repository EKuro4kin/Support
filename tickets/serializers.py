from rest_framework import serializers, generics, permissions

from tickets.models import Ticket, TicketComment


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        # read_only_fields = ("id", "question_name")


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = "__all__"


class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = "__all__"
