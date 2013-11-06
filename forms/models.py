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
    Two_1=models.IntegerField(verbose_name="Number of Blocks in which intensive strategy implementation is in progress")
    Two_2=models.IntegerField(verbose_name="Number of Gram Panchayats in which intensive strategy implementation is in progress")
    Two_3=models.IntegerField(verbose_name="Number of villages in which intensive strategy implementation is in progress")
    Three_1=models.IntegerField(verbose_name="Number of new SHGs promoted with NRLM target households")
    Three_2=models.IntegerField(verbose_name="Number of Pre-NRLM SHGs brought into the NRLM fold after revival/training and strengthening")
    Three_4=models.IntegerField(verbose_name="Number of SHGs that are provided with basic SHG training at community level")
    Three_5=models.IntegerField(verbose_name="Number of SHGs in which standard bookkeeping practices is introduced")
    Three_6=models.IntegerField(verbose_name="Number of SHGs that are following Pancha Sutras")
    Three_7=models.IntegerField(verbose_name="Number of SHGs bookkeepers identified and positioned after initial training")
    Three_8=models.IntegerField(verbose_name="Number of internal CRPs identified and trained in the intensive blocks")
    Four_1=models.IntegerField(verbose_name="Number of Villages in which PIP process has been completed")
    Four_2=models.IntegerField(verbose_name="Number of GPs in which PIP process has been completed")
    Four_3=models.IntegerField(verbose_name="Number of Poorest of the Poor (POP) households identified")
    Four_4=models.IntegerField(verbose_name="Number of Poor households identified")
    Four_5=models.IntegerField(verbose_name="Number of Non-Poor households identified")
    Four_6=models.IntegerField(verbose_name="Number of households having persons with disability member")
    Five_1=models.IntegerField(verbose_name="Number of SHGs which are more than 3 month old")
    Five_2=models.IntegerField(verbose_name="Number of 3 month old SHGs having bank accounts")
    Five_5=models.IntegerField(verbose_name="Number of predominantly SC-SHGs (SC>=50%) provided RF")
    Five_6=models.IntegerField(verbose_name="Number of predominantly ST-SHGs (ST>=50%) provided RF")
    Five_7=models.IntegerField(verbose_name="Number of predominantly Minority-SHGs (Minority>=50%) provided RF")
    Five_8=models.IntegerField(verbose_name="Number of Other-SHGs (with SC/ST<50%) provided RF")
    Five_9=models.IntegerField(verbose_name="Number of predominantly PWD-SHGs (PWD>=50%) provided RF")
    Five_10=models.DecimalField(verbose_name="Amount of RF provided to predominantly SC-SHGs (SC>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_11=models.DecimalField(verbose_name="Amount of RF provided to predominantly ST-SHGs (ST>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_12=models.DecimalField(verbose_name="Amount of RF provided to predominantly Minority-SHGs (Minority>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_13=models.DecimalField(verbose_name="Amount of RF provided to Other-SHGs (SC/ST<50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_14=models.DecimalField(verbose_name="Amount of RF provided to predominantly PWD-SHGs (PWD>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_1=models.IntegerField(verbose_name="Number of 6 month old SHGs in intensive blocks")
    Six_2=models.IntegerField(verbose_name="Number of SHGs which have prepared Micro Investment Plan (MIP)/Micro Credit Plan (MCP)")
    Six_5=models.IntegerField(verbose_name="Number of predominantly SC-SHG (SC>=50%) provided CIF")
    Six_6=models.IntegerField(verbose_name="Number of predominantly ST-SHG (ST>=50%) provided CIF")
    Six_7=models.IntegerField(verbose_name="Number of predominantly Minority-SHG (Minority>=50%) provided CIF")
    Six_8=models.IntegerField(verbose_name="Number of Other-SHG (with SC/ST<50%) provided CIF")
    Six_9=models.IntegerField(verbose_name="Number of predominantly PWD-SHG (PWD>=50%) provided CIF")
    Six_10=models.DecimalField(verbose_name="Amount of CIF provided to predominantly SC-SHG (SC>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_11=models.DecimalField(verbose_name="Amount of CIF provided to predominantly ST-SHG (ST>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_12=models.DecimalField(verbose_name="Amount of CIF provided to predominantly Minority-SHG (Minority>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_13=models.DecimalField(verbose_name="Amount of CIF provided to Other-SHG (SC/ST<50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_14=models.DecimalField(verbose_name="Amount of CIF provided to predominantly PWD-SHG (PWD>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Seven_1=models.IntegerField(verbose_name="Number of VOs formed")
    Seven_2=models.IntegerField(verbose_name="Number of SHGs holding membership in the VOs")
    Seven_3=models.IntegerField(verbose_name="Number of VOs provided training on basic VO management")
    Seven_4=models.IntegerField(verbose_name="Number of VOs having trained Bookkeeper")
    Seven_5=models.IntegerField(verbose_name="Number of VOs provided VRF (CIF)")
    Seven_6=models.DecimalField(verbose_name="Amount of VRF(CIF) provided to VOs (in Rs.Lakhs)",max_digits=15, decimal_places=2)
    Seven_7=models.IntegerField(verbose_name="Number of CLFs formed")
    Seven_8=models.IntegerField(verbose_name="Number of CLFs provided CIF")
    Seven_9=models.DecimalField(verbose_name="Amount of CIF provided to CLFs (in Rs.Lakhs)",max_digits=15, decimal_places=2)
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
    Two_1=models.IntegerField(verbose_name="Number of Blocks in which intensive strategy implementation is in progress")
    Two_2=models.IntegerField(verbose_name="Number of Gram Panchayats in which intensive strategy implementation is in progress")
    Two_3=models.IntegerField(verbose_name="Number of villages in which intensive strategy implementation is in progress")
    Three_1=models.IntegerField(verbose_name="Number of new SHGs promoted with NRLM target households")
    Three_2=models.IntegerField(verbose_name="Number of Pre-NRLM SHGs brought into the NRLM fold after revival/training and strengthening")
    Three_4=models.IntegerField(verbose_name="Number of SHGs that are provided with basic SHG training at community level")
    Three_5=models.IntegerField(verbose_name="Number of SHGs in which standard bookkeeping practices is introduced")
    Three_6=models.IntegerField(verbose_name="Number of SHGs that are following Pancha Sutras")
    Three_7=models.IntegerField(verbose_name="Number of SHGs bookkeepers identified and positioned after initial training")
    Three_8=models.IntegerField(verbose_name="Number of internal CRPs identified and trained in the intensive blocks")
    Four_1=models.IntegerField(verbose_name="Number of Villages in which PIP process has been completed")
    Four_2=models.IntegerField(verbose_name="Number of GPs in which PIP process has been completed")    
    Five_5=models.IntegerField(verbose_name="Number of predominantly SC-SHGs (SC>=50%) provided RF")
    Five_6=models.IntegerField(verbose_name="Number of predominantly ST-SHGs (ST>=50%) provided RF")
    Five_7=models.IntegerField(verbose_name="Number of predominantly Minority-SHGs (Minority>=50%) provided RF")
    Five_8=models.IntegerField(verbose_name="Number of Other-SHGs (with SC/ST<50%) provided RF")
    Five_9=models.IntegerField(verbose_name="Number of predominantly PWD-SHGs (PWD>=50%) provided RF")
    Five_10=models.DecimalField(verbose_name="Amount of RF provided to predominantly SC-SHGs (SC>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_11=models.DecimalField(verbose_name="Amount of RF provided to predominantly ST-SHGs (ST>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_12=models.DecimalField(verbose_name="Amount of RF provided to predominantly Minority-SHGs (Minority>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_13=models.DecimalField(verbose_name="Amount of RF provided to Other-SHGs (SC/ST<50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_14=models.DecimalField(verbose_name="Amount of RF provided to predominantly PWD-SHGs (PWD>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_2=models.IntegerField(verbose_name="Number of SHGs which have prepared Micro Investment Plan (MIP)/Micro Credit Plan (MCP)")
    Six_5=models.IntegerField(verbose_name="Number of predominantly SC-SHG (SC>=50%) provided CIF")
    Six_6=models.IntegerField(verbose_name="Number of predominantly ST-SHG (ST>=50%) provided CIF")
    Six_7=models.IntegerField(verbose_name="Number of predominantly Minority-SHG (Minority>=50%) provided CIF")
    Six_8=models.IntegerField(verbose_name="Number of Other-SHG (with SC/ST<50%) provided CIF")
    Six_9=models.IntegerField(verbose_name="Number of predominantly PWD-SHG (PWD>=50%) provided CIF")
    Six_10=models.DecimalField(verbose_name="Amount of CIF provided to predominantly SC-SHG (SC>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_11=models.DecimalField(verbose_name="Amount of CIF provided to predominantly ST-SHG (ST>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_12=models.DecimalField(verbose_name="Amount of CIF provided to predominantly Minority-SHG (Minority>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_13=models.DecimalField(verbose_name="Amount of CIF provided to Other-SHG (SC/ST<50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_14=models.DecimalField(verbose_name="Amount of CIF provided to predominantly PWD-SHG (PWD>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Seven_1=models.IntegerField(verbose_name="Number of VOs to be formed")
    Seven_2=models.IntegerField(verbose_name="Number of SHGs holding membership in the VOs")
    Seven_3=models.IntegerField(verbose_name="Number of VOs provided training on basic VO management")
    Seven_4=models.IntegerField(verbose_name="Number of VOs having trained Bookkeeper")
    Seven_5=models.IntegerField(verbose_name="Number of VOs provided VRF (CIF)")
    Seven_6=models.DecimalField(verbose_name="Amount of VRF(CIF) provided to VOs (in Rs.Lakhs)",max_digits=15, decimal_places=2)
    Seven_7=models.IntegerField(verbose_name="Number of CLFs to be formed")
    Seven_8=models.IntegerField(verbose_name="Number of CLFs provided CIF")
    Seven_9=models.DecimalField(verbose_name="Amount of CIF provided to CLFs (in Rs.Lakhs)",max_digits=15, decimal_places=2)
    Col4_SC=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (SCs)")
    Col5_SC=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (SCs)",max_digits=15, decimal_places=2)
    Col7_SC=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (SCs)")
    Col8_SC=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (SCs)",max_digits=15, decimal_places=2)
    Col4_ST=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (STs)")
    Col5_ST=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (STs)",max_digits=15, decimal_places=2)
    Col7_ST=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (STs)")
    Col8_ST=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (STs)",max_digits=15, decimal_places=2)
    Col4_Min=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (Minorities)")
    Col5_Min=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (Minorities)",max_digits=15, decimal_places=2)
    Col7_Min=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (Minorities)")
    Col8_Min=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (Minorities)",max_digits=15, decimal_places=2)
    Col4_Oth=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (Others)")
    Col5_Oth=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (Others)",max_digits=15, decimal_places=2)
    Col7_Oth=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (Others)")
    Col8_Oth=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (Others)",max_digits=15, decimal_places=2)
    Col4_PWD=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (PWDs)")
    Col5_PWD=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (PWDs)",max_digits=15, decimal_places=2)
    Col7_PWD=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (PWDs)")
    Col8_PWD=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (PWDs)",max_digits=15, decimal_places=2)
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
    Two_1=models.IntegerField(verbose_name="Number of Blocks in which intensive strategy implementation is in progress")
    Two_2=models.IntegerField(verbose_name="Number of Gram Panchayats in which intensive strategy implementation is in progress")
    Two_3=models.IntegerField(verbose_name="Number of villages in which intensive strategy implementation is in progress")
    Three_1=models.IntegerField(verbose_name="Number of new SHGs promoted with NRLM target households")
    Three_2=models.IntegerField(verbose_name="Number of Pre-NRLM SHGs brought into the NRLM fold after revival/training and strengthening")
    Three_4=models.IntegerField(verbose_name="Number of SHGs that are provided with basic SHG training at community level")
    Three_5=models.IntegerField(verbose_name="Number of SHGs in which standard bookkeeping practices is introduced")
    Three_6=models.IntegerField(verbose_name="Number of SHGs that are following Pancha Sutras")
    Three_7=models.IntegerField(verbose_name="Number of SHGs bookkeepers identified and positioned after initial training")
    Three_8=models.IntegerField(verbose_name="Number of internal CRPs identified and trained in the intensive blocks")
    Four_1=models.IntegerField(verbose_name="Number of Villages in which PIP process has been completed")
    Four_2=models.IntegerField(verbose_name="Number of GPs in which PIP process has been completed")
    Four_3=models.IntegerField(verbose_name="Number of Poorest of the Poor (POP) households identified")
    Four_4=models.IntegerField(verbose_name="Number of Poor households identified")
    Four_5=models.IntegerField(verbose_name="Number of Non-Poor households identified")
    Four_6=models.IntegerField(verbose_name="Number of households having persons with disability member")
    Five_1=models.IntegerField(verbose_name="Number of SHGs which are more than 3 month old")
    Five_2=models.IntegerField(verbose_name="Number of 3 month old SHGs having bank accounts")
    Five_5=models.IntegerField(verbose_name="Number of predominantly SC-SHGs (SC>=50%) provided RF")
    Five_6=models.IntegerField(verbose_name="Number of predominantly ST-SHGs (ST>=50%) provided RF")
    Five_7=models.IntegerField(verbose_name="Number of predominantly Minority-SHGs (Minority>=50%) provided RF")
    Five_8=models.IntegerField(verbose_name="Number of Other-SHGs (with SC/ST<50%) provided RF")
    Five_9=models.IntegerField(verbose_name="Number of predominantly PWD-SHGs (PWD>=50%) provided RF")
    Five_10=models.DecimalField(verbose_name="Amount of RF provided to predominantly SC-SHGs (SC>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_11=models.DecimalField(verbose_name="Amount of RF provided to predominantly ST-SHGs (ST>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_12=models.DecimalField(verbose_name="Amount of RF provided to predominantly Minority-SHGs (Minority>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_13=models.DecimalField(verbose_name="Amount of RF provided to Other-SHGs (SC/ST<50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Five_14=models.DecimalField(verbose_name="Amount of RF provided to predominantly PWD-SHGs (PWD>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_1=models.IntegerField(verbose_name="Number of 6 month old SHGs in intensive blocks")
    Six_2=models.IntegerField(verbose_name="Number of SHGs which have prepared Micro Investment Plan (MIP)/Micro Credit Plan (MCP)")
    Six_5=models.IntegerField(verbose_name="Number of predominantly SC-SHG (SC>=50%) provided CIF")
    Six_6=models.IntegerField(verbose_name="Number of predominantly ST-SHG (ST>=50%) provided CIF")
    Six_7=models.IntegerField(verbose_name="Number of predominantly Minority-SHG (Minority>=50%) provided CIF")
    Six_8=models.IntegerField(verbose_name="Number of Other-SHG (with SC/ST<50%) provided CIF")
    Six_9=models.IntegerField(verbose_name="Number of predominantly PWD-SHG (PWD>=50%) provided CIF")
    Six_10=models.DecimalField(verbose_name="Amount of CIF provided to predominantly SC-SHG (SC>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_11=models.DecimalField(verbose_name="Amount of CIF provided to predominantly ST-SHG (ST>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_12=models.DecimalField(verbose_name="Amount of CIF provided to predominantly Minority-SHG (Minority>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_13=models.DecimalField(verbose_name="Amount of CIF provided to Other-SHG (SC/ST<50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Six_14=models.DecimalField(verbose_name="Amount of CIF provided to predominantly PWD-SHG (PWD>=50%) (Rs. in lakhs)",max_digits=15, decimal_places=2)
    Seven_1=models.IntegerField(verbose_name="Number of VOs formed")
    Seven_2=models.IntegerField(verbose_name="Number of SHGs holding membership in the VOs")
    Seven_3=models.IntegerField(verbose_name="Number of VOs provided training on basic VO management")
    Seven_4=models.IntegerField(verbose_name="Number of VOs having trained Bookkeeper")
    Seven_5=models.IntegerField(verbose_name="Number of VOs provided VRF (CIF)")
    Seven_6=models.DecimalField(verbose_name="Amount of VRF(CIF) provided to VOs (in Rs.Lakhs)",max_digits=15, decimal_places=2)
    Seven_7=models.IntegerField(verbose_name="Number of CLFs formed")
    Seven_8=models.IntegerField(verbose_name="Number of CLFs provided CIF")
    Seven_9=models.DecimalField(verbose_name="Amount of CIF provided to CLFs (in Rs.Lakhs)",max_digits=15, decimal_places=2)
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
    Col2_smmu=models.IntegerField(verbose_name="Number of units setup that are approved (SMMU)")
    Col2_dmmu=models.IntegerField(verbose_name="Number of units setup that are approved (DMMU)")
    Col2_bmmu=models.IntegerField(verbose_name="Number of units setup that are approved (BMMU)")
    Col2_bmmup=models.IntegerField(verbose_name="Number of units setup that are approved (BMMU Partnership)")
    Col3_smmu=models.IntegerField(verbose_name="Number of units setup that are Positioned (SMMU)")
    Col3_dmmu=models.IntegerField(verbose_name="Number of units setup that are Positioned (DMMU)")
    Col3_bmmu=models.IntegerField(verbose_name="Number of units setup that are Positioned (BMMU)")
    Col3_bmmup=models.IntegerField(verbose_name="Number of units setup that are Positioned (BMMU Partnership)")
    Col4_smmu=models.IntegerField(verbose_name="Thematic Positions Approved (SMMU)")
    Col4_dmmu=models.IntegerField(verbose_name="Thematic Positions Approved (DMMU)")
    Col4_bmmu=models.IntegerField(verbose_name="Thematic Positions Approved (BMMU)")
    Col4_bmmup=models.IntegerField(verbose_name="Thematic Positions Approved (BMMU Partnership)")
    Col5_smmu=models.IntegerField(verbose_name="Thematic Staff in Position (SMMU)")
    Col5_dmmu=models.IntegerField(verbose_name="Thematic Staff in Position (DMMU)")
    Col5_bmmu=models.IntegerField(verbose_name="Thematic Staff in Position (BMMU)")
    Col5_bmmup=models.IntegerField(verbose_name="Thematic Staff in Position (BMMU Partnership)")
    Col6_smmu=models.IntegerField(verbose_name="Thematic staff Inducted (SMMU)")
    Col6_dmmu=models.IntegerField(verbose_name="Thematic staff Inducted (DMMU)")
    Col6_bmmu=models.IntegerField(verbose_name="Thematic staff Inducted (BMMU)")
    Col6_bmmup=models.IntegerField(verbose_name="Thematic staff Inducted (BMMU Partnership)")
    Col7_smmu=models.IntegerField(verbose_name="Thematic staff Immersed (SMMU)")
    Col7_dmmu=models.IntegerField(verbose_name="Thematic staff Immersed (DMMU)")
    Col7_bmmu=models.IntegerField(verbose_name="Thematic staff Immersed (BMMU)")
    Col7_bmmup=models.IntegerField(verbose_name="Thematic staff Immersed (BMMU Partnership)")
    Col8_smmu=models.IntegerField(verbose_name="Support staff Positions approved (SMMU)")
    Col8_dmmu=models.IntegerField(verbose_name="Support staff Positions approved (DMMU)")
    Col8_bmmu=models.IntegerField(verbose_name="Support staff Positions approved (BMMU)")
    Col8_bmmup=models.IntegerField(verbose_name="Support staff Positions approved (BMMU Partnership)")
    Col9_smmu=models.IntegerField(verbose_name="Support staff in Position (SMMU)")
    Col9_dmmu=models.IntegerField(verbose_name="Support staff in Position (DMMU)")
    Col9_bmmu=models.IntegerField(verbose_name="Support staff in Position (BMMU)")
    Col9_bmmup=models.IntegerField(verbose_name="Support staff in Position (BMMU Partnership)")
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
    Col2_SC=models.IntegerField(verbose_name="Total number of SHGs (SCs)")
    Col2_ST=models.IntegerField(verbose_name="Total number of SHGs (STs)")
    Col2_Min=models.IntegerField(verbose_name="Total number of SHGs (Minorities)")
    Col2_Oth=models.IntegerField(verbose_name="Total number of SHGs (Others)")
    Col2_PWD=models.IntegerField(verbose_name="Total number of SHGs (PWDs)")
    Col3_SC=models.IntegerField(verbose_name="No of SHG eligible for Bank Credit (SCs)")
    Col3_ST=models.IntegerField(verbose_name="No of SHG eligible for Bank Credit (STs)")
    Col3_Min=models.IntegerField(verbose_name="No of SHG eligible for Bank Credit (Minorities)")
    Col3_Oth=models.IntegerField(verbose_name="No of SHG eligible for Bank Credit (Others)")
    Col3_PWD=models.IntegerField(verbose_name="No of SHG eligible for Bank Credit (PWDs)")
    Col4_SC=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (SCs)")
    Col4_ST=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (STs)")
    Col4_Min=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (Minorities)")
    Col4_Oth=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (Others)")
    Col4_PWD=models.IntegerField(verbose_name="No of SHGs Accessed with Bank Credit (PWDs)")
    Col5_SC=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (SCs)",max_digits=15, decimal_places=2)
    Col5_ST=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (STs)",max_digits=15, decimal_places=2)
    Col5_Min=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (Minorities)",max_digits=15, decimal_places=2)
    Col5_Oth=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (Others)",max_digits=15, decimal_places=2)
    Col5_PWD=models.DecimalField(verbose_name="Amount of Loan Accessed(Rs. In Lakh) (PWDs)",max_digits=15, decimal_places=2)
    Col6_SC=models.IntegerField(verbose_name="No of SHG eligible for Interest Subvention (SCs)")
    Col6_ST=models.IntegerField(verbose_name="No of SHG eligible for Interest Subvention (STs)")
    Col6_Min=models.IntegerField(verbose_name="No of SHG eligible for Interest Subvention (Minorities)")
    Col6_Oth=models.IntegerField(verbose_name="No of SHG eligible for Interest Subvention (Others)")
    Col6_PWD=models.IntegerField(verbose_name="No of SHG eligible for Interest Subvention (PWDs)")
    Col7_SC=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (SCs)")
    Col7_ST=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (STs)")
    Col7_Min=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (Minorities)")
    Col7_Oth=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (Others)")
    Col7_PWD=models.IntegerField(verbose_name="No of SHG provided with Interest Subvention (PWDs)")
    Col8_SC=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (SCs)",max_digits=15, decimal_places=2)    
    Col8_ST=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (STs)",max_digits=15, decimal_places=2)
    Col8_Min=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (Minorities)",max_digits=15, decimal_places=2)
    Col8_Oth=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (Others)",max_digits=15, decimal_places=2)
    Col8_PWD=models.DecimalField(verbose_name="Amount of Interest Subvention Given(Rs. In Lakh) (PWDs)",max_digits=15, decimal_places=2)
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