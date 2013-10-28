from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed, pre_delete, post_delete, pre_save, post_save
import datetime
from data_log import delete_log, save_log
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
    def get_state(self):
        return self.id
post_save.connect(save_log, sender = State)
pre_delete.connect(delete_log, sender = State)
    
class Project(models.Model):
    project_name=models.CharField(max_length=30, db_column="PROJECT_NAME", unique=True)
    def __unicode__(self):
        return self.project_name
    def get_state(self):
        return None
post_save.connect(save_log, sender = Project)
pre_delete.connect(delete_log, sender = Project)

class UserModel(models.Model):
    user_created = models.ForeignKey(User, related_name ="%(class)s_created", editable = False, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_modified = models.ForeignKey(User, related_name ="%(class)s_related_modified",editable = False, null=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
  
    class Meta:
        abstract = True
    def get_state(self):
        return self.state.id

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
    Four_1=models.IntegerField()
    Four_2=models.IntegerField()
    Four_3=models.IntegerField()
    Four_4=models.IntegerField()
    Four_5=models.IntegerField()
    Four_6=models.IntegerField()
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
    def get_state(self):
        return self.state.id
post_save.connect(save_log, sender = Progress)
pre_delete.connect(delete_log, sender = Progress)
    
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
    Four_1=models.IntegerField()
    Four_2=models.IntegerField()
    Four_3=models.IntegerField()
    Four_4=models.IntegerField()
    Four_5=models.IntegerField()
    Four_6=models.IntegerField()
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
    Col2_SC=models.IntegerField()
    Col3_SC=models.IntegerField()
    Col4_SC=models.IntegerField()
    Col5_SC=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_SC=models.IntegerField()
    Col7_SC=models.IntegerField()
    Col8_SC=models.DecimalField(max_digits=15, decimal_places=7)
    Col2_ST=models.IntegerField()
    Col3_ST=models.IntegerField()
    Col4_ST=models.IntegerField()
    Col5_ST=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_ST=models.IntegerField()
    Col7_ST=models.IntegerField()
    Col8_ST=models.DecimalField(max_digits=15, decimal_places=7)
    Col2_Min=models.IntegerField()
    Col3_Min=models.IntegerField()
    Col4_Min=models.IntegerField()
    Col5_Min=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_Min=models.IntegerField()
    Col7_Min=models.IntegerField()
    Col8_Min=models.DecimalField(max_digits=15, decimal_places=7)
    Col2_Oth=models.IntegerField()
    Col3_Oth=models.IntegerField()
    Col4_Oth=models.IntegerField()
    Col5_Oth=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_Oth=models.IntegerField()
    Col7_Oth=models.IntegerField()
    Col8_Oth=models.DecimalField(max_digits=15, decimal_places=7)
    Col2_PWD=models.IntegerField()
    Col3_PWD=models.IntegerField()
    Col4_PWD=models.IntegerField()
    Col5_PWD=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_PWD=models.IntegerField()
    Col7_PWD=models.IntegerField()
    Col8_PWD=models.DecimalField(max_digits=15, decimal_places=7)
    def __unicode__(self):
        return self.state.state_name+" "+self.project.project_name+" "+str(self.year)
    def get_state(self):
        return self.state.id
post_save.connect(save_log, sender = Target)
pre_delete.connect(delete_log, sender = Target)

class ProgressTill13(UserModel):
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
    Four_1=models.IntegerField()
    Four_2=models.IntegerField()
    Four_3=models.IntegerField()
    Four_4=models.IntegerField()
    Four_5=models.IntegerField()
    Four_6=models.IntegerField()
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
    def get_state(self):
        return self.state.id
post_save.connect(save_log, sender = ProgressTill13)
pre_delete.connect(delete_log, sender = ProgressTill13)

"""class HrUnit(models.Model):
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
        return self.hrunit.hrunit_name+" "+self.state.state_name+" "+self.project.project_name+" "+self.month+" "+str(self.year)"""

class HrDetails(UserModel):
    state=models.ForeignKey(State)
    project=models.ForeignKey(Project)
    month=models.CharField(max_length=3, choices=Month, db_column="Month")
    year=models.CharField(max_length=4)
    Col2_smmu=models.IntegerField()
    Col3_smmu=models.IntegerField()
    Col4_smmu=models.IntegerField()
    Col5_smmu=models.IntegerField()
    Col6_smmu=models.IntegerField()
    Col7_smmu=models.IntegerField()
    Col8_smmu=models.IntegerField()
    Col9_smmu=models.IntegerField()
    Col2_dmmu=models.IntegerField()
    Col3_dmmu=models.IntegerField()
    Col4_dmmu=models.IntegerField()
    Col5_dmmu=models.IntegerField()
    Col6_dmmu=models.IntegerField()
    Col7_dmmu=models.IntegerField()
    Col8_dmmu=models.IntegerField()
    Col9_dmmu=models.IntegerField()
    Col2_bmmu=models.IntegerField()
    Col3_bmmu=models.IntegerField()
    Col4_bmmu=models.IntegerField()
    Col5_bmmu=models.IntegerField()
    Col6_bmmu=models.IntegerField()
    Col7_bmmu=models.IntegerField()
    Col8_bmmu=models.IntegerField()
    Col9_bmmu=models.IntegerField()
    Col2_bmmup=models.IntegerField()
    Col3_bmmup=models.IntegerField()
    Col4_bmmup=models.IntegerField()
    Col5_bmmup=models.IntegerField()
    Col6_bmmup=models.IntegerField()
    Col7_bmmup=models.IntegerField()
    Col8_bmmup=models.IntegerField()
    Col9_bmmup=models.IntegerField()
    def __unicode__(self):
        return self.state.state_name+" "+self.project.project_name+" "+self.month+" "+str(self.year)
    def get_state(self):
        return self.state.id
post_save.connect(save_log, sender = HrDetails)
pre_delete.connect(delete_log, sender = HrDetails)

"""class Category(models.Model):
    category_name=models.CharField(max_length=20, db_column="CATEGORY_NAME", unique=True)
    def __unicode__(self):
        return self.category_name"""
    
class FinancialAssistance(UserModel):
#    user = models.ForeignKey(User, null = True, db_column="USER")
    state=models.ForeignKey(State)
    project=models.ForeignKey(Project)
    month=models.CharField(max_length=3, choices=Month, db_column="Month")
    year=models.CharField(max_length=4)
    #category=models.ForeignKey(Category)
    Col2_SC=models.IntegerField()
    Col3_SC=models.IntegerField()
    Col4_SC=models.IntegerField()
    Col5_SC=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_SC=models.IntegerField()
    Col7_SC=models.IntegerField()
    Col8_SC=models.DecimalField(max_digits=15, decimal_places=7)
    Col2_ST=models.IntegerField()
    Col3_ST=models.IntegerField()
    Col4_ST=models.IntegerField()
    Col5_ST=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_ST=models.IntegerField()
    Col7_ST=models.IntegerField()
    Col8_ST=models.DecimalField(max_digits=15, decimal_places=7)
    Col2_Min=models.IntegerField()
    Col3_Min=models.IntegerField()
    Col4_Min=models.IntegerField()
    Col5_Min=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_Min=models.IntegerField()
    Col7_Min=models.IntegerField()
    Col8_Min=models.DecimalField(max_digits=15, decimal_places=7)
    Col2_Oth=models.IntegerField()
    Col3_Oth=models.IntegerField()
    Col4_Oth=models.IntegerField()
    Col5_Oth=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_Oth=models.IntegerField()
    Col7_Oth=models.IntegerField()
    Col8_Oth=models.DecimalField(max_digits=15, decimal_places=7)
    Col2_PWD=models.IntegerField()
    Col3_PWD=models.IntegerField()
    Col4_PWD=models.IntegerField()
    Col5_PWD=models.DecimalField(max_digits=15, decimal_places=7)
    Col6_PWD=models.IntegerField()
    Col7_PWD=models.IntegerField()
    Col8_PWD=models.DecimalField(max_digits=15, decimal_places=7)
    def __unicode__(self):
        return self.state.state_name+" "+self.project.project_name+" "+self.month+" "+str(self.year)
    def get_state(self):
        return self.state.id
post_save.connect(save_log, sender = FinancialAssistance)
pre_delete.connect(delete_log, sender = FinancialAssistance)

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

class ServerLog(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.utcnow)
    user = models.ForeignKey(User, null = True)
    state = models.IntegerField(null = True)
    action = models.IntegerField()
    entry_table = models.CharField(max_length=100)
    model_id = models.IntegerField(null = True)
    """def __unicode__(self):
        return self.user.username +" "+ self.state.state_name+" "+self.timestamp"""
    
class CocoUser(UserModel):
    user = models.OneToOneField(User)
    states = models.ManyToManyField(State)
    def get_state(self):
        return self.states.all()
    def __unicode__(self):
        return self.user.username
    
class FullDownloadStats(models.Model):
    user = models.ForeignKey(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()