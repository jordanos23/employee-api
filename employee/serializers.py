from django.forms import ValidationError
from rest_framework import serializers

from .models import Employee


def is_email_unique(email):
    if Employee.objects.filter(email=email).exists():
        raise ValidationError("Employee with that email already exists")
    return


class EmployeeSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50, min_length=2, allow_blank=False)
    last_name = serializers.CharField(max_length=50, min_length=2, allow_blank=False)
    email = serializers.EmailField(required=True, validators=[is_email_unique])
    gender = serializers.ChoiceField(choices=Employee.gender_choices)
    # resume = serializers.FileField(required=True, allow_empty_file=False, validators=[])

    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "email", "gender"]

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=False, max_length=50, min_length=2, allow_blank=False
    )
    last_name = serializers.CharField(
        required=False, max_length=50, min_length=2, allow_blank=False
    )
    email = serializers.EmailField(required=False, validators=[is_email_unique])
    gender = serializers.ChoiceField(required=False, choices=Employee.gender_choices)
    # resume = serializers.FileField(required=True, allow_empty_file=False, validators=[])

    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "email", "gender"]

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
