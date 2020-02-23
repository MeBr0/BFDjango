import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from todo.auth_.models import MyUser


@csrf_exempt
def register(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')

    user = MyUser.objects.create_user(username=username)
    user.set_password(password)
    user.save()

    return JsonResponse({'message': f'user with username {user.username} created'}, status=200)
