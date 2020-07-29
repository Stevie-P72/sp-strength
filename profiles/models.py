from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_info_first_name = models.CharField(max_length=80, null=True, blank=True)
    personal_info_last_name = models.CharField(max_length=80, null=True, blank=True)
    default_billing_address_line1 = models.CharField(max_length=80, null=True, blank=True)
    default_billing_address_line2 = models.CharField(max_length=80, null=True, blank=True)
    default_billing_address_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_billing_address_country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
