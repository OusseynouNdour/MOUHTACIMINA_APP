# profils/views.py

<<<<<<< HEAD
# Create your views here.

=======
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
>>>>>>> 2cc3dc8 (deuxieme commit sur le projet django)
