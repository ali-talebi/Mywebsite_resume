from django.contrib import admin
from .models import Education  , Person , skills   , EXPERIENCE , interests

# Register your models here.

class Education_Admin(admin.ModelAdmin) : 
    list_display = ("university"  , 'level' , "start" , "end" , "field" , "avg" , "status" ) 
    list_editable = ("status" , )
    search_fields = ("university" , "field" , )
    
    
    
admin.site.register(Education , Education_Admin )


@admin.register(Person)
class Person_Admin(admin.ModelAdmin) : 
    list_display = ("name"  , 'family' , "email" , "phone" , "git_hub_slug"  , "Linkedin" , "all_skills" , "all_interests" )  
    
    def all_skills(self , obj):
        return ' | '.join([ i.name for i in obj.skills.all() ])
    all_skills.short_description = "مهارت ها "
    
    
    def all_interests(self , obj ) : 
        return ' | '.join([ i.name for i in obj.interests.all() ])
    
    all_interests.short_description = " علاقه مندی ها  "
        

    
    
@admin.register(skills)
class skills_Admin(admin.ModelAdmin) : 
    list_display = ("name"  , 'applications' , "level" , "tools"   )
    list_editable = ("level" , )  
    search_fields = ("name" , "applications" , "tools"  ) 
    
    
@admin.register(EXPERIENCE)
class EXPERIENCE_Admin(admin.ModelAdmin) : 
    list_display = ("name"  , "name_company" , "start" , "end"   )
    
    search_fields = ("name" , "name_company"  ) 
    
    
@admin.register(interests)
class interests_Admin(admin.ModelAdmin) : 
    list_display = ("name"  ,   )
    search_fields = ("name" , )
    
    
    