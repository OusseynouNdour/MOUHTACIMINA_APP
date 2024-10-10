from rest_framework import serializers
from .models import Payment
from profils.serializers import MemberSerializer

class PaymentSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'member', 'amount', 'payment_method', 'transaction_id', 'date_paid']
