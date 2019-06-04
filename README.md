# social_sweethearts
## Task
A) User should connect/login with Facebook (logout accordingly) (Note: Plugins can be used); \
B) The Facebook app should simply provide the following output: the name and profile picture of the logged-in user; \
C) The token, which will be stored for the user in the database, should be a long living access token; \
D) If the user removes the Facebook app, the user shall be marked as "is_active = false" in the database 
   (Note: Facebook DeAuth callback);
 
## To run this app :
   A) You have to create venv and install dependency from requirments.txt to venv and run migrate command. \
   B) Use your own database and Facebook App ID and SECRET (as I tried to authenticate user in dev mode facebook denied to
    login saying if you are in dev mode only developer account could be logged in.) \
   C) I have used decouple to keep away Important information from settings.py
    



### Note:- 
Token stored in database is long living upto 60 days which can be accessed \
as ->  facebook_auth.extra_data['access_token']  
I was not able to use DeAuth although I went through the process doc which stated that when ever any user with perform DeAuth
Facebook will "Whenever a user of your app de-authorizes it, this URL will be sent an HTTP POST containing a signed request. 
Read our guide to parsing the signed request to see how to decode this to find out the user ID that triggered the callback."
after processing Facebook POST Data we can mark particular user as "is_active = False" in the database.
