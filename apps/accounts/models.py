from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user=models.OneToOneField(User,related_name="account",on_delete=models.CASCADE)
    address=models.CharField(max_length=255,blank=True,null=True)
    zipcode=models.CharField(max_length=10,blank=True,null=True)
    place=models.CharField(max_length=255,blank=True,null=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    
    def __str__(self):
        return '%s' % self.user.username

User.userprofile=property(lambda u:UserAccount.objects.get_or_create(user=u)[0])