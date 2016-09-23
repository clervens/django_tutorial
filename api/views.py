from rest_framework import status, viewsets
from .serializers import QuestionSerializer, ChoiceSerializer

from polls.models import Question, Choice

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
