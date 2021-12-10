from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50)
    confirm_password = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'email', 'phone', 'password', 'confirm_password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValueError('Email is must')
        is_user_existed = User.objects.filter(email__exact=email)
        if is_user_existed:
            serializers.ValidationError('Email is already taken')
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password is not None and password != confirm_password:
            self.add_error('confirm_password', 'password must match')
        return self.cleaned_data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
