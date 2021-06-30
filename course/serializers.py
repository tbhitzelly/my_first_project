from rest_framework import serializers


class BranchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)



class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    Branch = serializers.CharField(required=True)
    photo = serializers.ImageField(required=False)



class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    address = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    group = serializers.CharField(required=True)