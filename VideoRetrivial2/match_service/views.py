from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext

# Create your views here.
from match_service.models import *


def match_page(request):
    context = {}
    if request.method == 'POST':
        return render_to_response(
            'video_labeling.html',
            context,
        )

    return render_to_response(
        'wellcome_page.html',
        context,
        context_instance = RequestContext(request)
    )

    pass

def get_next_video(request):
    context = {
        'title':'',
        'youtube_url':''

    }
    return HttpResponse(
        json.dumps(context),
        content_type='application/json'
    )
