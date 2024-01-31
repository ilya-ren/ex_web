from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission


class Cliente(AbstractBaseUser, PermissionsMixin):
    rut        = models.CharField(max_length=13, primary_key=True)
    first_name = models.CharField(max_length=25, blank=False, null=True)
    last_name  = models.CharField(max_length=25, blank=False, null=True)
    ap_materno = models.CharField(max_length=25, blank=False, null=True)
    fec_nac    = models.DateField(blank=False, null=True)
    tele       = models.CharField(max_length=20, blank=False, null=True)
    region     = models.CharField(max_length=20, blank=False, null=True)
    ciudad     = models.CharField(max_length=20, blank=False, null=True)
    comuna     = models.CharField(max_length=20, blank=False, null=True)
    dire       = models.CharField(max_length=100, blank=False, null=True)
    email      = models.EmailField(max_length=40, blank=False, null=False, unique=True)
    password   = models.CharField(max_length=128, blank=False, null=False)

    is_active  = models.BooleanField(default=True)

    groups = models.ManyToManyField(Group, related_name='clientes', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='clientes', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut']

    def __str__(self):
        return f"{self.rut} {self.first_name} {self.last_name} {self.ap_materno}"
    
   