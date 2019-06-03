from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

from social_django.models import UserSocialAuth

import requests

@login_required
def Profile(request):
	if request.method == "GET":
		try:
			facebook_auth = request.user.social_auth.get(provider='facebook')
		except UserSocialAuth.DoesNotExist:
			facebook_auth = None
		if facebook_auth:
			# reading profile picture doesn't require an access token or permission
			# if you want to get JSON response simply put redirect=false in your query parameter
			FACEBOOK_PROFILE = f"https://graph.facebook.com/v3.3/{facebook_auth.uid}/picture"
			response = requests.get(FACEBOOK_PROFILE, params={'height':300, 'width':300, 'redirect':'false'})

			if response.status_code == 200:
				response.encoding = 'utf-8'
				profile_image = response.json()['data']['url']
	return render(request, 'accounts/profile.html', {'profile_image':profile_image})


@csrf_exempt
def FacebookProfileDisconnect(request):
	if request.method == 'POST':
		print(request.POST)
	return redirect('accounts:login')