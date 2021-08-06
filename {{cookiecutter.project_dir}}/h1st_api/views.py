import h1st_models.translate
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


def health(request):
    return HttpResponse('all is good here')


def default(request):
    text = 'Congratulations! This is your Human-First REST API!'
    return HttpResponse(text)


translate_model = h1st_models.translate.TranslateModel()


@api_view(['POST'])
def translate(request):
    """Translate text to and from specified language"""
    data = JSONParser().parse(request)
    result = translate_model.predict(data)["result"]
    return JsonResponse({'output': result})