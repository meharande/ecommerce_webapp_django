from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Please provide an email')

        user = self.model(
            email = self.normalize_email(email),
            phone = kwargs.get('phone'),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **kwargs):
        user = self.create_user(
            email = email,
            password = password,
            phone=kwargs.get('phone')
        )

        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(
            email = email,
            password = password,
            phone = kwargs.get('phone')
        )

        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user