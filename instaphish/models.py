from django.db import models


class Accounts(models.Model):
    login = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    is_insta = models.BooleanField(default=True)

    def __str__(self):
        return f'Login: {self.login} , password: {self.password}'

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'