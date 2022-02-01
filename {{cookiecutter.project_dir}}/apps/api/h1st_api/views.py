"""
A view is a callable which takes a request and returns a response.
This can be more than just a function, and Django provides an example of some classes which can be used as views.
These allow you to structure your views and reuse code by harnessing inheritance and mixins.
There are also some generic views for tasks which we’ll get to later,
but you may want to design your own structure of reusable views which suits your use case.

For more information, please see https://docs.djangoproject.com/en/3.2/topics/class-based-views/.
"""

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# append python path to include ai package
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
sys.path.append(str(ROOT_DIR))

from ai.models.translate import TranslateModel
from ai.models.my_ml_model import MyMLModel

translate_model = TranslateModel()
my_ml_model = MyMLModel().load_params('example_ml_model')


def default(request):
    """default view"""
    text = 'Congratulations! This is your Human-First REST API!'
    return HttpResponse(text)


@api_view(['POST'])
def translate(request):
    """Translate text to and from specified language"""
    data = JSONParser().parse(request)

    rule_based_result = translate_model.predict(data)["result"]
    ml_result = my_ml_model.predict(data)['result']
    final_result = rule_based_result + '|' + ml_result

    return JsonResponse({'output': final_result})
