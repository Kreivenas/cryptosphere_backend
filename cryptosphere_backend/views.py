from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "project": "CryptoSphere API",
        "status": "Running",
        "version": "1.0.0",
        "message": "Welcome to the future of crypto alerts. Use /admin to manage data."
    })
