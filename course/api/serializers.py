from rest_framework import serializers
from course.models import *



class BranchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)

    def create(self, validated_data):
        return Branch.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.save()
        return instance


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    Branch = serializers.CharField(required=True)
    photo = serializers.ImageField(required=False)

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.Branch = validated_data.get('Branch', instance.Branch)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.save()
        return instance



class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    address = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    group = serializers.CharField(required=True)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.group = validated_data.get('group', instance.group)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.save()
        return instance

