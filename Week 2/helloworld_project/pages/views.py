from django.http import HttpResponse


# do not know why this method must be lowerCamelCase
def homePageView(request):
    return HttpResponse('Hello, World!')
