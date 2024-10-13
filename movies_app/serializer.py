from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie,Collection
# --- creating user registration serializer -------
class UserRegistraionSerializer(serializers.ModelSerializer):
   class Meta:
    model=User
    fields=['username','password']
    extra_kwargs={
      'password':{'write_only':True}
    }
    def  create(self,validated_data):
      user=User(**validated_data)
      user.set_password(validated_data['password'])
      user.save()
      return user

#---- Creating Movie serializer --------
class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model=Movie
    fields=['uuid','title','description','genres']

#----- Creating collection serializer ---------
class CollectionSerializer(serializers.ModelSerializer):
  movies=MovieSerializer(many=True,read_only=True)
  class Meta:
    model=Collection
    fields=['uuid','title','description','movies']