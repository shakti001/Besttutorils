from django.contrib import admin
from .models import Slider, Tutorial , Caurses , footer_discription,Contact,email_templates,Topic,general_setting


# Register your models here.
admin.site.register(Slider)
admin.site.register(Tutorial)
admin.site.register(footer_discription)
admin.site.register(Contact)
admin.site.register(Caurses)
admin.site.register(email_templates)
admin.site.register(Topic)
admin.site.register(general_setting)
