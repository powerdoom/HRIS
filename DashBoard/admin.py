from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from DashBoard.models import ProfileBasic
from DashBoard.models import ProfileEdu
from DashBoard.models import ProfileProTech
from DashBoard.models import ProfileSkillTech
from DashBoard.models import Professional
from DashBoard.models import Management
from DashBoard.models import Skilled

class ProfileBasicInline(admin.StackedInline):
    model = ProfileBasic
    verbose_name_plural = 'Base Profile'

class ProfileEduInline(admin.TabularInline):
    model = ProfileEdu
    fk_name = 'user_id'

class ProfileProTechInline(admin.TabularInline):
    model = ProfileProTech
    fk_name = 'user_id'

class ProfileSkillTechInline(admin.TabularInline):
    model = ProfileSkillTech
    fk_name = 'user_id'

class ProfessionalInline(admin.TabularInline):
    model = Professional
    fk_name = 'user_id'

class ManagementInline(admin.TabularInline):
    model = Management
    fk_name = 'user_id'

class SkilledInline(admin.TabularInline):
    model = Skilled
    fk_name = 'user_id'

class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileBasicInline,
        ProfileEduInline,
        ProfileProTechInline,
        ProfileSkillTechInline,
        ProfessionalInline,
        ManagementInline,
        SkilledInline,
    ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
