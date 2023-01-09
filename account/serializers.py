from rest_framework import serializers

from .models import User, Profile


class IsSenderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'is_sender', ]
        read_only_fields = ['is_sender', ]

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        return data

    def create(self, validated_data):
        new_user = Profile(
            username=validated_data['username'],
        )
        new_user.is_sender = True
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('id', 'user', 'is_sender', 'is_buyer')

class IsBuyerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'is_sender', ]
        read_only_fields = ['is_sender', ]

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        return data

    def create(self, validated_data):
        new_user = Profile(
            username=validated_data['username'],
        )
        new_user.is_sender = False
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user
