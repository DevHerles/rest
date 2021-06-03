from rest_framework import serializers
from apps.users.models import User
from apps.partners.models import Partner
from apps.settings.models import Setting
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Password fields didn't match")
        return attrs

    def validate_old_password(self, value):
        # user = self.context['request'].user
        data = self.context['request'].data
        user_id = data.pop('id')
        user = User.objects.filter(pk=user_id).first()
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is not correct.')

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.groups.name in ['admin', 'supervisor', 'moderator']:
            instance.set_password(validated_data['password'])
            instance.save()
        else:
            if user.pk != instance.pk:
                raise serializers.ValidationError(
                    'You dont have permission for this user.')
            instance.set_password(validated_data['password'])
            instance.save()
        return instance


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
        fields = ('username', 'email', 'password', 'partner', 'groups')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # groups = validated_data.pop('groups', 'user')
        # if not groups:
        #     new_group, created = Group.objects.get_or_create(name=groups)
        #     print('new_group', new_group)
        #     print('created', created)
        #     validated_data['groups'] = new_group if new_group else created
        instance = self.Meta.model(**validated_data)
        print(validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        partner = Partner.objects.filter(email=instance.email).first()
        if partner:
            partner.owner = instance
            partner.save()
        # Partner(email=instance.email, name=instance.username,
        #         owner=instance).save()
        Setting(owner=instance).save()
        return instance


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_active', 'created_date', 'modified_date',
                   'deleted_date', 'password')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'role': instance.groups.name if instance.groups else 'user',
            'roles': []
        }


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
