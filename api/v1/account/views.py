from rest_framework import generics, viewsets
from account.models import Profile
from .serializers import ProfileSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def profile_detail(request):
    try:
        profile = Profile.objects.get(user=request.user)
    # except Profile.DoesNotExist:
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data)
