from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .services import get_movie
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import UserRegistraionSerializer,CollectionSerializer,MovieSerializer
from .models import Collection,Movie
from django.core.cache import cache


# Testing  the Django project
class TestView(APIView):
  permission_classes=[AllowAny]

  def get(self,request):
    return Response({"message":"The django setup is working fine!"},status=200)




# ---- MOVIE LIST API VIEW ----

#---- GETTING MOVIE LIST --- 
class MovieListView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self,request):
    
    page_url=request.query_params.get('page',None)
    movies=get_movie(page_url)
    if movies:
      return Response(movies)
    else:
      return Response({"error":"No movies found"},status=500)


#---- USER REGISTRATION ----
class RegisterView(APIView):
  authentication_classes=[JWTAuthentication]
  permission_classes=[AllowAny]
  def post(self,request):
    # Implementing user registration
    serializers=UserRegistraionSerializer(data=request.data)

    if serializers.is_valid():
      user=serializers.save()
      access_token=AccessToken.for_user(user)
      refresh=RefreshToken.for_user(user)
      return Response({'access_token':str(access_token),'refresh_token':str(refresh)},status=201)
    return Response(serializers.errors,status=400)
  





# ----- USER COLLECTION API VIEW -----
class UserCollectionView(APIView):
  permission_classes=[IsAuthenticated]

  def get(self,request):
    # fetching all collections from auhenticated user
    user=request.user
    collections=Collection.objects.filter(user=user)

    # serializing collection data
    collection_data=CollectionSerializer(collections,many=True).data

    favroite_genre=self.get_favroite_genres(user)

    return Response({
      "is_success":True,
      "data":{
        "collections":collection_data,
        "favorite_genres":favroite_genre
      }
    },status=status.HTTP_200_OK)


  def post(self,request):
    data=request.data
    # creating a new collection 
    collection=Collection.objects.create(
      title=data['title'],
      description=data['description'],
      user=request.user

    )

    # adding movie to the collection
    movies=data.get('movies',[])
    for movie in movies:
      Movie.objects.create(
        title=movie['title'],
        description=movie['description'],
        genres=movie['genres'],
        uuid=movie['uuid'],
        collection=collection
      )

    return Response({
      "collection_uuid":str(collection.uuid)
    },status=status.HTTP_200_OK)


  def get_favroite_genres(self,user):
    # fetching top 3 favourite genres from user
    genres_count={}
    collections=Collection.objects.filter(user=user).prefetch_related('movies')

    for collection in collections:
      for movie in collection.movies.all():
        if movie.genres:
          genres=movie.genres.split(",")
          for genre in genres:
            genre=genre.strip()

            genres_count[genre]=genres_count.get(genre,0)+1
    top_genres=sorted(genres_count,key=genres_count.get,reverse=True)[:3]
    return ", ".join(top_genres)


# --------- IMPLEMENTING THE UPDATE , DELETE AND GETTING MOVIE BY UUID ------
class CollectionViewUUID(APIView):
  permission_classes=[IsAuthenticated]

  # updating the specific collection

  def put(self,request,collection_uuid):
    try:
      collection=Collection.objects.get(uuid=collection_uuid,user=request.user)
    except:
      return Response({"error":"Collection not found"},status=status.HTTP_404_NOT_FOUND)
    
    data=request.data
    collection.title=data.get('title',collection.title)
    collection.description=data.get('description',collection.description)
    collection.save()

    # update the movie in the collection
    movies_data=data.get('movies',[])
    if movies_data:
      collection.movies.all().delete()
      for movie in movies_data:
        Movie.objects.create(
          title=movie['title'],
          description=movie['description'],
          genres=movie['genres'],
          uuid=movie['uuid'],
          collection=collection
        )
      
    return Response({"message":"Collection updated successfully"},status=status.HTTP_200_OK)
  

  # getting the specific collection using uuid
  def get(self,request,collection_uuid):
    user=request.user
    try:
      collection=Collection.objects.get(uuid=collection_uuid,user=user)
      serialized_collection=CollectionSerializer(collection).data
      return Response({'is_success':True,
                       "data":serialized_collection},status=status.HTTP_200_OK)
    except Collection.DoesNotExist:
      return Response({'error':'Collection not found'},status=status.HTTP_404_NOT_FOUND)

    
  # deleting the collection using uuid

  def delete(self,request,collection_uuid):
    try:
      collection=Collection.objects.get(uuid=collection_uuid,user=request.user)
    except Collection.DoesNotExist:
      return Response({'error':'collection not found'},status=status.HTTP_404_NOT_FOUND)
    collection.delete()
    return Response({"message":"Collection deleted successfully"},status=status.HTTP_204_NO_CONTENT)
  


#-------- CREATING API FOR IMPLEMENTING THE REQUEST COUNTER MIDDLEWARE --------
class RequestCounterView(APIView):
  def get(self,request):
    request_count=cache.get('request_count',0)
    return Response({'request_count':request_count},status=status.HTTP_200_OK)
  
  def post(self,request):
    cache.set('request_count',0)
    return Response({'message':'Request count reset successfull'},status=status.HTTP_200_OK)

