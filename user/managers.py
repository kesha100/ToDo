from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    """Custom User Manager"""
    use_in_migrations = True

    def create_superuser(self, email, password=None):
        email = self.normalize_email(email=email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_user(self, email, password):
        email = self.normalize_email(email=email)
        user = self.model(email=email)
        user.set_password(password)
        # user.create_activation_code()
        user.save(using=self._db)
        return user

