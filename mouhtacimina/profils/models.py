from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class MemberType(models.Model):
    type_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.type_name

class Member(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    member_type = models.ForeignKey(MemberType, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

