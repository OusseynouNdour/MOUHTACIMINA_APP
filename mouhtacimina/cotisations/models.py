from django.db import models

from mouhtacimina.profils.models import Member

class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('wave', 'Wave'),
        ('orange_money', 'Orange Money')
    ])
    transaction_id = models.CharField(max_length=100, unique=True)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.member}"

