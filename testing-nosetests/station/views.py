import json
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        json.dumps({'hello': 'world'}), content_type="application/json")
