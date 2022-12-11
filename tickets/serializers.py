from rest_framework import serializers, generics, permissions

from tickets.models import Ticket, TicketComment


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketCommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, source="user.username")

    class Meta:
        model = TicketComment
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    message = TicketCommentSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ["id", "question_name", "description", "answer", "status", "message"]


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = "__all__"
