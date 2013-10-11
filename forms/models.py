from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Month = (
        ('Jan','January'),
        ('Feb','February'),
        ('Mar','March'),
        ('Apr','April'),
        ('May','May'),
        ('Jun','June'),
        ('Jul','July'),
        ('Aug','August'),
        ('Sep','September'),
        ('Oct','October'),
        ('Nov','November'),
        ('Dec','December'),
)

class State(models.Model):
    state_name=models.CharField(max_length=30, db_column="STATE_NAME", unique=True) #null=True blank=True
    def __unicode__(self):
        return self.state_name
    
class Project(models.Model):
    project_name=models.CharField(max_length=30, db_column="PROJECT_NAME", unique=True)
    def __unicode__(self):
        return self.project_name

class UserModel(models.Model):
    user_created = models.ForeignKey(User, related_name ="%(class)s_created", editable = False, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_modified = models.ForeignKey(User, related_name ="%(class)s_related_modified",editable = False, null=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
  
    class Meta:
        abstract = True

class Progress(UserModel):
#    user = models.ForeignKey(User, null = True, db_column="USER")
    state=models.ForeignKey(State)
    project=models.ForeignKey(Project)
    month=models.CharField(max_length=3, choices=Month, db_column="Month")
    year=models.CharField(max_length=4)
    Two_1=models.IntegerField()
    Two_2=models.IntegerField()
    Two_3=models.IntegerField()
    Three_1=models.IntegerField()
    Three_2=models.IntegerField()
    Three_4=models.IntegerField()
    Three_5=models.IntegerField()
    Three_6=models.IntegerField()
    Three_7=models.IntegerField()
    Three_8=models.IntegerField()
    Four_1=models.IntegerField(null=True,blank=True)
    Four_2=models.IntegerField(null=True,blank=True)
    Four_3=models.IntegerField(null=True,blank=True)
    Four_4=models.IntegerField(null=True,blank=True)
    Four_5=models.IntegerField(null=True,blank=True)
    Four_6=models.IntegerField(null=True,blank=True)
    Five_1=models.IntegerField()
    Five_2=models.IntegerField()
    Five_5=models.IntegerField()
    Five_6=models.IntegerField()
    Five_7=models.IntegerField()
    Five_8=models.IntegerField()
    Five_9=models.IntegerField()
    Five_10=models.DecimalField(max_digits=15, decimal_places=7)
    Five_11=models.DecimalField(max_digits=15, decimal_places=7)
    Five_12=models.DecimalField(max_digits=15, decimal_places=7)
    Five_13=models.DecimalField(max_digits=15, decimal_places=7)
    Five_14=models.DecimalField(max_digits=15, decimal_places=7)
    Six_1=models.IntegerField()
    Six_2=models.IntegerField()
    Six_5=models.IntegerField()
    Six_6=models.IntegerField()
    Six_7=models.IntegerField()
    Six_8=models.IntegerField()
    Six_9=models.IntegerField()
    Six_10=models.DecimalField(max_digits=15, decimal_places=7)
    Six_11=models.DecimalField(max_digits=15, decimal_places=7)
    Six_12=models.DecimalField(max_digits=15, decimal_places=7)
    Six_13=models.DecimalField(max_digits=15, decimal_places=7)
    Six_14=models.DecimalField(max_digits=15, decimal_places=7)
    Seven_1=models.IntegerField()
    Seven_2=models.IntegerField()
    Seven_3=models.IntegerField()
    Seven_4=models.IntegerField()
    Seven_5=models.IntegerField()
    Seven_6=models.DecimalField(max_digits=15, decimal_places=7)
    Seven_7=models.IntegerField()
    Seven_8=models.IntegerField()
    Seven_9=models.DecimalField(max_digits=15, decimal_places=7)
    def __unicode__(self):
        return self.state.state_name+" "+self.project.project_name+" "+self.month+" "+str(self.year)
    
class Target(UserModel):
    #user = models.ForeignKey(User, null = True, db_column="USER")
    state=models.ForeignKey(State)
    project=models.ForeignKey(Project)
    year=models.CharField(max_length=4)
    Two_1=models.IntegerField()
    Two_2=models.IntegerField()
    Two_3=models.IntegerField()
    Three_1=models.IntegerField()
    Three_2=models.IntegerField()
    Three_4=models.IntegerField()
    Three_5=models.IntegerField()
    Three_6=models.IntegerField()
    Three_7=models.IntegerField()
    Three_8=models.IntegerField()
    Four_1=models.IntegerField(null=True,blank=True)
    Four_2=models.IntegerField(null=True,blank=True)
    Four_3=models.IntegerField(null=True,blank=True)
    Four_4=models.IntegerField(null=True,blank=True)
    Four_5=models.IntegerField(null=True,blank=True)
    Four_6=models.IntegerField(null=True,blank=True)
    Five_1=models.IntegerField()
    Five_2=models.IntegerField()
    Five_5=models.IntegerField()
    Five_6=models.IntegerField()
    Five_7=models.IntegerField()
    Five_8=models.IntegerField()
    Five_9=models.IntegerField()
    Five_10=models.DecimalField(max_digits=15, decimal_places=7)
    Five_11=models.DecimalField(max_digits=15, decimal_places=7)
    Five_12=models.DecimalField(max_digits=15, decimal_places=7)
    Five_13=models.DecimalField(max_digits=15, decimal_places=7)
    Five_14=models.DecimalField(max_digits=15, decimal_places=7)
    Six_1=models.IntegerField()
    Six_2=models.IntegerField()
    Six_5=models.IntegerField()
    Six_6=models.IntegerField()
    Six_7=models.IntegerField()
    Six_8=models.IntegerField()
    Six_9=models.IntegerField()
    Six_10=models.DecimalField(max_digits=15, decimal_places=7)
    Six_11=models.DecimalField(max_digits=15, decimal_places=7)
    Six_12=models.DecimalField(max_digits=15, decimal_places=7)
    Six_13=models.DecimalField(max_digits=15, decimal_places=7)
    Six_14=models.DecimalField(max_digits=15, decimal_places=7)
    Seven_1=models.IntegerField()
    Seven_2=models.IntegerField()
    Seven_3=models.IntegerField()
    Seven_4=models.IntegerField()
    Seven_5=models.IntegerField()
    Seven_6=models.DecimalField(max_digits=15, decimal_places=7)
    Seven_7=models.IntegerField()
    Seven_8=models.IntegerField()
    Seven_9=models.DecimalField(max_digits=15, decimal_places=7)
    def __unicode__(self):
        return self.state.state_name+" "+self.project.project_name+" "+str(self.year)
    
class HrUnit(models.Model):
    hrunit_name=models.CharField(max_length=20, db_column="UNIT_NAME", unique=True)
    def __unicode__(self):
        return self.hrunit_name

class HrDetails(UserModel):
#    user = models.ForeignKey(User, null = True, db_column="USER")
    state=models.ForeignKey(State)
    project=models.ForeignKey(Project)
    hrunit=models.ForeignKey(HrUnit)
    month=models.CharField(max_length=3, choices=Month, db_column="Month")
    year=models.CharField(max_length=4)
    Col_2=models.IntegerField()
    Col_3=models.IntegerField()
    Col_4=models.IntegerField()
    Col_5=models.IntegerField()
    Col_6=models.IntegerField()
    Col_7=models.IntegerField()
    Col_8=models.IntegerField()
    Col_9=models.IntegerField()
    def __unicode__(self):
        return self.hrunit.hrunit_name+" "+self.state.state_name+" "+self.project.project_name+" "+self.month+" "+str(self.year)

class Category(models.Model):
    category_name=models.CharField(max_length=20, db_column="CATEGORY_NAME", unique=True)
    def __unicode__(self):
        return self.category_name
    
class FinancialAssistance(UserModel):
#    user = models.ForeignKey(User, null = True, db_column="USER")
    state=models.ForeignKey(State)
    project=models.ForeignKey(Project)
    month=models.CharField(max_length=3, choices=Month, db_column="Month")
    year=models.CharField(max_length=4)
    category=models.ForeignKey(Category)
    Col_2=models.IntegerField()
    Col_3=models.IntegerField()
    Col_4=models.IntegerField()
    Col_5=models.DecimalField(max_digits=15, decimal_places=7)
    Col_6=models.IntegerField()
    Col_7=models.IntegerField()
    Col_8=models.DecimalField(max_digits=15, decimal_places=7)
    def __unicode__(self):
        return self.category.category_name+" "+self.state.state_name+" "+self.project.project_name+" "+self.month+" "+str(self.year)
    
"""class UserProfile(models.Model):  
    username = models.CharField( max_length=30, unique=True)
    first_name = models.CharField( max_length=30, blank=True)
    last_name = models.CharField( max_length=30, blank=True)
    email = models.EmailField( blank=True)
    password = models.CharField( max_length=128)
    is_staff = models.BooleanField( default=False)
    is_active = models.BooleanField( default=True)
    is_superuser = models.BooleanField( default=False)
    last_login = models.DateTimeField( default=timezone.now)
    date_joined = models.DateTimeField( default=timezone.now)
    objects = UserManager()

    def is_authenticated(self):
        "Always return True. This is a way to tell if the user has been authenticated in templates."
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
"""