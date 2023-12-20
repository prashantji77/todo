from enum import unique
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from authAPI.managers import UserManager
from django.utils.translation import gettext as _

class User(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=256,blank=True,null=True)
    last_name=models.CharField( max_length=256,blank=True,null=True)
    email=models.EmailField(_("email address"), max_length=100,unique=True)
    isActive=models.BooleanField(_("active"),default=False)
    role=models.CharField(_("role"), max_length=100)
    is_staff=models.BooleanField(_("staff status"),default=False,
                                 help_text=_("Designtes whether the user can log into this admin site."),
                                 )
    is_admin=models.BooleanField(_("staff status"),default=False)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    objects=UserManager()

    def __str__(self):
        return self.email
    