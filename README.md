# Hi 👋

Hi I am **PAVAN CHOWDRI M** excited to share my latest backend project


# Movie Collection API 🎬

## Overview
The **Movie collection API** is a Restful API build with Django and Django Rest framework that allows user to add collection of the movies and also based on collection the api will provide top 3 favorite genres of the user.I have performed the CRUD operation like creating the collection, update the collection of specific one, delete the specific collection.
 
 -  movie api used  - https://demo.credy.in/api/v1/maya/movies/
## Features
- User registration and authentication using JWT token.
-  Getting all the movie list.
-  Create and manage movie collections.
-  Counting the number of requests and also reseting.
-  Delete,update and get the specific movie collection.

## Technology used

- Django
- Django Rest framework
- Django Rest framework Simple JWT for authentication
- Database - sqlite
- version Control - Git
- Thunder Client - API testing

## Steps to execute

1. First install all the dependencies present in the requirement.txt file
2. After cloning my repositroy inside the project root folder create .env file and add MOVIE_API_USERNAME= , MOVIE_API_PASSWORD=
3. Make migration and run the project
4. Open Postman or Thunder Client
	
	- User registration ( POST - http://127.0.0.1:8000/register/)
	
		- In the body add { "username":"", "password":"" } 
		- The access_token : ""  and the refresh_token: "" will be generated and the access token will expires in 1 day and refresh token will expire in 2 days
	- Getting Movie list (GET - http://127.0.0.1:8000/movies/)
		
		- Once you register in response copy the access_token, inside the Header add 
			
				Authentication : Bearer <Your access token>
		- Now Get the request you can see the respones as 
		
				 {
			  "count": 45466,
			  "next": "https://demo.credy.in/api/v1/maya/movies/?page=2",
			  "previous": null,
			  "results": [
			    {
			      "title": "Queerama",
			      "description": "50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
			      "genres": "",
			      "uuid": "57baf4f4-c9ef-4197-9e4f-acf04eae5b4d"
			    },
	- Creating Collection for user - (POST - http://127.0.0.1:8000/collection/)
		
		- Once you register in response copy the access_token, inside the Header add 
		
				Authentication : Bearer <Your access token>
		- Inside the body add the movie collection which you can get from *Getting movie list api*
		
				{
			    "title": "My Favorite Movies",
			    "description": "A collection of my favorite movies.",
			    "movies": [
			        {
			            "title": "Queerama",
			      "description": "50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
			      "genres": "",
			      "uuid": "57baf4f4-c9ef-4197-9e4f-acf04eae5b4d"
			        }, 
			   }
			 
		- In the respone you will get the **uuid**
	- Getting movie collection (GET - http://127.0.0.1:8000/collection/)
	
		- Once you register in response copy the access_token, inside the Header add 
		
				Authentication : Bearer <Your access token>
				
		- In response you wil see the json data
			
				{
			  "is_success": true,
			  "data": {
			    "collections": [
			      {
			        "uuid": "3dd34ce3-d888-4424-86be-196197447252",
			        "title": "My Favorite Movies",
			        "description": "A collection of my favorite movies.",
			        "movies": []
			      },
			      {
			        "uuid": "74bf3cb5-1b93-4097-a6a9-b54f12cf3374",
			        "title": "My Favorite Movies",
			        "description": "A collection of my favorite movies.",
			        "movies": [
			          {
			            "uuid": "57baf4f4-c9ef-4197-9e4f-acf04eae5b4d",
			            "title": "Queerama",
			            "description": "50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
			            "genres": ""
			          },
			          ],
			    "favorite_genres": "Horror, Action, Drama"
				  }
				}

	- Getting movie collection of specific user (GET - http://127.0.0.1:8000/collection/<collection_uuid>/
	
		-  Once you register in response copy the access_token, inside the Header add 
		
				Authentication : Bearer <Your access token>
		- In response you will get json data as below
		
					{
				  "is_success": true,
				  "data": {
				    "uuid": "da6ed9ba-bbda-4cdf-836a-5041df49fa6b",
				    "title": "My Favorite Movies",
				    "description": "A collection of my favorite movies.",
				    "movies": [
				      {
				        "uuid": "57baf4f4-c9ef-4197-9e4f-acf04eae5b4d",
				        "title": "Queerama",
				        "description": "50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
				        "genres": ""
				      },
				      {
				        "uuid": "720e8796-5397-4e81-9bd7-763789463707",
				        "title": "Betrayal",
				        "description": "When one of her hits goes wrong, a professional assassin ends up with a suitcase full of a million dollars belonging to a mob boss ...",
				        "genres": "Action,Drama,Thriller"
				      },
				      {
				        "uuid": "129cf5d9-827c-4e42-843e-1f87ef99452f",
				        "title": "Caged Heat 3000",
				        "description": "It's the year 3000 AD. The world's most dangerous women are banished to a remote asteroid 45 million light years from earth. Kira Murphy doesn't belong; wrongfully accused of a crime she did not commit, she's thrown in this interplanetary prison and left to her own defenses. But Kira's a fighter, and soon she finds herself in the middle of a female gang war; where everyone wants a piece of the action... and a piece of her! \"Caged Heat 3000\" takes the Women-in-Prison genre to a whole new level... and a whole new galaxy!",
				        "genres": "Science Fiction"
				      }
				    ]
				  }
				} 
				 
	- Updating the specific collection  (PUT - http://127.0.0.1:8000/collection/<collection_uuid : (Hint) response of creating collection>/
	
		-  Once you register in response copy the access_token, inside the Header add 
		
				Authentication : Bearer <Your access token>
			
		- In response you will get message as ** collection updated successfully **
	- DELETE the specific collection (DELETE - http://127.0.0.1:8000/collection/<collection_uuid : (Hint) response of creating collection>/

		- Once you register in response copy the access_token, inside the Header add 
		
				Authentication : Bearer <Your access token>

		- In response you will get message as ** collection deleted successfully **
	- Request Count ( GET - http://127.0.0.1:8000/request-count/)
	
		-  Once you register in response copy the access_token, inside the Header add 
		
				Authentication : Bearer <Your access token>
		- in response you will get request count as 
		
				 {
				 "request_count":7   ## indicates that i have done 7 api request
				 } 

	- Request_count_reset(POST - http://127.0.0.1:8000/request-count/reset)
	 
		- Once you register in response copy the access_token, inside the Header add 
		
				Authentication : Bearer <Your access token>
		 - In response you will get message as ** Request count reset successfullt**

###  Future Enhancement
Using this backend now i am able to build frontend which will allow user to create collection dynamically. using technology like react,angular,..

### Social media link 🔗
- Linkedin link : https://www.linkedin.com/in/pavan-chowdri-m-226a55212/
- Github Repo link : https://github.com/PavanChowdri?tab=repositories
