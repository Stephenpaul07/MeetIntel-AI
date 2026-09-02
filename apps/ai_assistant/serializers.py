from rest_framework import serializers


class AskQuestionSerializer(serializers.Serializer):
    question = serializers.CharField(
        max_length=1000,
        allow_blank=False,
    )