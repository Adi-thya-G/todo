from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.
  

class Todo_table(BaseModel):
    category_list=[
          ('Personal Work','Personal Work'),
          ('Office Work','Office Work'),
          ( 'Creative Work','Creative Work'),
          ( 'Meetings & Appointments','Meetings & Appointments'),
          ( 'Health & Wellness','Health & Wellness'),
          ('Miscellaneous','Miscellaneous'),
    ]
    
    Priority_list=[('Low Priority','Non-Urgent'),('Medium Priority','Standard'),('High Priority','Urgent')]
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_id")
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    category=models.CharField(max_length=50,choices=category_list,default=category_list[0])
    deadline = models.DateTimeField() 
    is_completed = models.BooleanField(default=False)
    priority_level=models.CharField(max_length=50,choices=Priority_list,default=Priority_list[1])
    alternative_refernce=models.EmailField(blank=True,null=True)
    def __str__(self):
        return self.title