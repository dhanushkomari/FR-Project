from django.db import models

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length = 10, blank = True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.status)




#######################  PATIENT MODEL    ############################
bg = (
    ('A +ve', 'A +ve'),
    ('A -ve', 'A -ve'),
    ('B +ve', 'B +ve'),
    ('B -ve', 'B -ve'),
    ('AB +ve', 'AB +ve'),
    ('AB -ve', 'AB -ve'),
    ('O +ve', 'O +ve'),
    ('O -ve', 'O -ve'),
    )
gend = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('other', 'other'),
)
stat = (
    ('Active', 'Active'),
    ('Not Active', 'Not Active'),
)

class Patient(models.Model):    
    patient_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 30, blank = False)
    last_name = models.CharField(max_length = 30, blank = False)
    username = models.CharField(max_length = 30, unique = True)
    age = models.IntegerField()
    blood_group = models.CharField(default = "A +ve", choices = bg, max_length = 10)
    gender = models.CharField(default = "Male", choices = gend, max_length = 10)
    status = models.CharField(default = "Active", choices = stat, max_length = 10)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length = 50, blank = False, help_text = 'abc@example.com')
    city = models.CharField(max_length = 25, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    # photo = models.ImageField(upload_to='Patient_Users',blank = True, null = True)
        
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        ordering = ('-patient_id',)

    # def get_url():
        # return reverse('')
    
    def __str__(self):
        return '{}'.format(self.username)

