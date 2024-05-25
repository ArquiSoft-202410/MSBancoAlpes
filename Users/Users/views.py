from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

@require_http_methods(["POST"])
def test(request):
    return JsonResponse({"message": "This is a test"})

