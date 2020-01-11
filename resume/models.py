from django.db import models
from users.models import CusetomUser
# Create your models here.
class Resume(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),

    )

    user = models.OneToOneField(CusetomUser, on_delete=models.CASCADE)
    gender = models.CharField(
                            max_length=1,
                            choices=GENDER_CHOICES,
                            null=True,
                            blank=True)
    birth_date = models.DateField("Date of Birth", null=True, blank=True)
    address_one = models.CharField(max_length=100, null=True, blank=True)
    address_two = models.CharField(max_length=100, blank=True, null=True)
    address_three = models.CharField(max_length=100, blank=True, null=True)    
    # country = models.ForeignKey(
    #                             Country,
    #                             on_delete=models.DO_NOTHING,
    #                             blank=True,
    #                             null=True)
    # state = ChainedForeignKey(
    #                         State,
    #                         chained_field="country",
    #                         chained_model_field="country",
    #                         null=True,
    #                         blank=True)
    # citie = ChainedForeignKey(
    #                         Citie,
    #                         chained_field="state",
    #                         chained_model_field="state",
    #                         null=True,
    #                         blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    is_hoo = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username
