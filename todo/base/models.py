from django.db import models
import uuid

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract= True