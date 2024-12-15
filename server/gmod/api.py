from django.http import JsonResponse

def api(request):
    return JsonResponse({'message': 'Hello, world!'})

def apiLogin(request):
    return JsonResponse({'message': 'Hello, world!'})