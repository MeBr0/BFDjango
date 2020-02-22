import json

from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return JsonResponse({'message': 'logged in'}, status=200)

    else:
        return JsonResponse({'message': 'user not found or not active'}, status=200)


@csrf_exempt
def logout(request):
    user = auth.logout(request)

    return JsonResponse({'message': 'logged out'}, status=200)



