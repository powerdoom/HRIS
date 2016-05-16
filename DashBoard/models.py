from django.db import models
from django.contrib.auth.models import User
from datetime import date

EDU_REC = (
    ('H', '高中'),
    ('C', '大专'),
    ('U', '本科'),
    ('G', '研究生'),
)

DGR = (
    ('B', '学士'),
    ('M', '硕士'),
    ('D', '博士'),
)

PRO_LEVEL = (
    ('H', '正高'),
    ('PH', '副高'),
    ('M', '中级'),
    ('L', '初级'),
    ('PL', '员级'),
)
MNG_LEVEL = (
    ('FT', '副厅'),
    ('ZZ', '正处'),
    ('FZ', '副处'),
    ('ZZ', '正科'),
    ('FK', '副科'),
    ('KY', '科员'),
    ('BSY', '办事员'),
)

SKL_LEVEL = (
    ('PSW', '高级技师'),
    ('SW', '技师'),
    ('HW', '高级工'),
    ('MW', '中级工'),
    ('LW', '初级工'),
    ('W', '普通工'),
)


class ProfileBasic(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICE = (
        (MALE, '男'),
        (FEMALE, '女'),
    )

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    realname = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=2, choices=SEX_CHOICE, default=MALE, blank=True)
    id_real = models.CharField(max_length=18, blank=True)
    department = models.CharField(max_length=30, blank=True)
    minority = models.CharField(max_length=10, blank=True)
    party = models.CharField(max_length=20, blank=True)
    dob = models.DateField(default=date.today)
    firstwt = models.DateField(default=date.today)
    phone = models.CharField(max_length=24, blank=True)
    pwd_que = models.CharField(max_length=128, blank=True)
    pwd_anw = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.realname

class ProfileEdu(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    school = models.CharField(max_length=30, blank=True)
    edu_rec = models.CharField(max_length=6, blank=True, choices=EDU_REC)
    degree = models.CharField(max_length=4, blank=True, choices=DGR)
    special = models.CharField(max_length=30, blank=True)
    start_time = models.DateField(blank=True)
    end_time = models.DateField(blank=True)

class ProfileProTech(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    pro = models.CharField(max_length=10, blank=True)
    pro_name = models.CharField(max_length=12, blank=True)
    pro_level = models.CharField(max_length=4, blank=True, choices=PRO_LEVEL)
    ori_time = models.DateField(blank=True)
    depart = models.CharField(max_length=16, blank=True)

class ProfileSkillTech(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    skl = models.CharField(max_length=16, blank=True)
    skl_level = models.CharField(max_length=8, blank=True, choices=SKL_LEVEL)
    ori_time = models.DateField(blank=True)

class Professional(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    pro_type = models.CharField(max_length=12, blank=True)
    pro_level = models.CharField(max_length=4, blank=True, choices=PRO_LEVEL)
    pro_deg = models.CharField(max_length=4, blank=True)
    pro = models.CharField(max_length=12, blank=True)
    start_time = models.DateField(blank=True)
    end_time = models.DateField(blank=True)

class Management(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    mng = models.CharField(max_length=30, blank=True)
    mng_level = models.CharField(max_length=6, blank=True, choices=MNG_LEVEL)
    mng_deg = models.CharField(max_length=2, blank=True)
    start_time = models.DateField(blank=True)
    end_time = models.DateField(blank=True)

class Skilled(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    skl = models.CharField(max_length=12, blank=True)
    skl_level = models.CharField(max_length=12, blank=True, choices=SKL_LEVEL)
    skl_deg = models.CharField(max_length=2, blank=True)
    start_time = models.DateField(blank=True)
    end_time = models.DateField(blank=True)
