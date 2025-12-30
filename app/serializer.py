from rest_framework import serializers
from .models import SCHOOL

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SCHOOL
        fields = "__all__"
