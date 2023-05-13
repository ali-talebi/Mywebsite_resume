from django.db import models
from django.utils import timezone  
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.



class Education(models.Model) : 
    STATUS_LEVEL = (
        ('end' , "پایان") , 
        ('continue'  , "در حال تحصیل") , 
    )
    
    STATUS_LEVEL_educations = (
    ( "Bachelor's degree" , "Bachelor's degree") ,  
    ('Masters' , 'Masters' )  ,  
    ('P.H.D' , 'P.H.D') 
    )

    
    
    university = models.CharField(verbose_name="اسم دانشگاه" , max_length=200 )
    start = models.DateTimeField(verbose_name="شروع " , default=timezone.now  , null = True )
    start_update = models.DateTimeField(verbose_name="شروع " , auto_now_add = True , null = True )

    end   = models.DateTimeField(verbose_name="پایان " , default=timezone.now , null = True , blank = True ) 
    end_update = models.DateTimeField(verbose_name="پایان " , auto_now_add = True , null = True )   
    field = models.CharField(verbose_name="رشته"  , max_length=200 )
    avg   = models.FloatField(verbose_name="معدل" , blank = True , null = True )
    status = models.CharField(verbose_name="وضعیت" , max_length= 10 , choices = STATUS_LEVEL )
    level = models.CharField(verbose_name="مقطع" , max_length= 50 , choices = STATUS_LEVEL_educations , null = True , blank = True )
    def __str__(self) : 
        return self.field + " " + self.university
    
    
    class Meta : 
        db_table = "Education"
        verbose_name_plural = "تحصیلات" 
    
    

    
class skills(models.Model) : 
    level_skills = (
        ('Beginner' , 'Beginner')  , 
        ('Expert' , 'Expert' )  , 
        ('professional' , 'professional') , 
        ('Professor','Professor' )
        
    )
    picture = models.FileField(verbose_name=" عکس مهارت " , upload_to= "skills"  , null = True , blank = True )
    name = models.CharField(verbose_name="مهارت" , max_length= 30  )
    applications = RichTextField(verbose_name="کاربرد ها "   )
    level = models.CharField(verbose_name="سطح مهارت" , max_length= 30 , choices = level_skills )
    tools = models.CharField(verbose_name= "ابزار ها " , max_length= 200 , blank = True )
    
    
    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "skills"
        verbose_name_plural = "مهارت ها "








class EXPERIENCE(models.Model):
    name = models.CharField(verbose_name="جایگاه شغلی" , max_length=200 )
    name_company = models.CharField(verbose_name="نام شرکت" , max_length=200 )
    start = models.DateTimeField(verbose_name="شروع " , default=timezone.now  , null = True )
    start_update = models.DateTimeField(verbose_name="شروع " , auto_now_add = True , null = True )
    end   = models.DateTimeField(verbose_name="پایان " , default=timezone.now , null = True , blank = True ) 
    end_update = models.DateTimeField(verbose_name="پایان " , auto_now_add = True , null = True ) 
    descriptions = RichTextField(verbose_name = "توضیحات"  , null = True , blank = True )
    
    def __str__(self) : 
        return self.name + " -- " + self.name_company 
    
    
    class Meta : 
        db_table = "EXPERIENCE"
        verbose_name_plural = "تجربیات عملی "



class interests(models.Model) : 
    picture = models.FileField(verbose_name="عکس علاقه مندی" , upload_to= "interests_picture"  , null = True , blank = True )
    name = models.CharField(verbose_name="نام علاقه مندی", max_length=200 , blank = True , null = True ) 
    
    def __str__(self) : 
        return self.name 
    
    
    class Meta : 
        db_table = "interests"
        verbose_name_plural = "علاقه مندی ها "
        


class Person(models.Model):
    about_me = models.CharField(verbose_name="درباره من ", max_length=200 , blank = True , null = True ) 
    picture = models.FileField(verbose_name="عکس" , upload_to= "Image_person"  , null = True , blank = True )
    name   = models.CharField(verbose_name="اسم   " , max_length=200 )
    family = models.CharField(verbose_name=" اسم خانوادگی   " , max_length=200 )   
    email  = models.EmailField(verbose_name="ایمیل  " , max_length=200 )
    phone  = models.BigIntegerField(verbose_name="همراه شخصی " )
    git_hub_slug = models.CharField(verbose_name="آدرس گیت هاب    " , max_length=200 )
    Linkedin = models.CharField(verbose_name= "آدرس لینک دین " , max_length=200 )
    educations = models.ManyToManyField('Education' )
    skills = models.ManyToManyField('skills' )
    interests = models.ManyToManyField('interests' , verbose_name="علاقه مندی ها "  , null = True , blank = True)
    experiences = models.ManyToManyField('EXPERIENCE' , null = True , blank = True )
    address = models.CharField(verbose_name="آدرس"  , null = True , blank = True , max_length= 200 )
    
    
    def __str__(self) : 
        return self.name + self.family 
    
    
    class Meta : 
        db_table = "Person" 
        verbose_name_plural = "فرد "
    
    
    
