from django.db import models
from django.contrib.auth.models import User
import uuid



# --------- creating collection model --------
class Collection(models.Model):
  uuid=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
  title=models.CharField(max_length=255)
  description=models.TextField(blank=True,null=True)
  user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='collections')

  def __str__(self):
    return self.title


# -------- creating Movie model ------
class Movie(models.Model):
  uuid=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
  title=models.CharField(max_length=255)
  description=models.TextField()
  genres=models.CharField(max_length=255,blank=True,null=True)
  collection=models.ForeignKey(Collection,on_delete=models.CASCADE,related_name="movies")

  def __str__(self):
    return self.title
