from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
			FACEBOOK_PROFILE = f"https://graph.facebook.com/v3.3/{facebook_auth.uid}/picture"
			response = requests.get(FACEBOOK_PROFILE, params={'height':300, 'width':300},)
	return render(request, 'accounts/profile.html', {'response':response})


def FacebookProfileDisconnect(request):
	if request.method == 'POST':
		print(request.POST)
	return redirect('accounts:login')