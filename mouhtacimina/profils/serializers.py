from rest_framework import serializers
from .models import Member, Section, MemberType

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name', 'description']

class MemberTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberType
        fields = ['id', 'type_name', 'description']

class MemberSerializer(serializers.ModelSerializer):
    section = SectionSerializer(read_only=True)
    member_type = MemberTypeSerializer(read_only=True)
    
    class Meta:
        model = Member
        fields = ['id', 'username', 'email', 'section', 'member_type', 'date_joined']
