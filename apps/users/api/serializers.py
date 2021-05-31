from rest_framework import serializers
from apps.users.models import User
from apps.partners.models import Partner
from apps.settings.models import Setting
from django.contrib.auth.models import Group


class EmailAndPasswordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user


class UsernameAndPasswordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'partner')
        extra_kwargs = {'password': {'write_only': True}}


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'partner')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        if not groups:
            new_group, created = Group.objects.get_or_create(name='user')
            print('new_group', new_group)
            print('created', created)
            validated_data['groups'] = new_group if new_group else created
        instance = self.Meta.model(**validated_data)
        print(validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        Setting(owner=instance).save()
        instance.save()
        Partner(email=instance.email, name=instance.username,
                owner=instance).save()
        return instance


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }
