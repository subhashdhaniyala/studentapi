from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['course','is_active']
    search_fields=['name','email']
    ordering_fields=['enrolled_on','name']

