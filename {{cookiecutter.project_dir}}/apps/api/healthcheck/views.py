"""
A view is a callable which takes a request and returns a response. This can be more than just a function,
and Django provides an example of some classes which can be used as views.
These allow you to structure your views and reuse code by harnessing inheritance and mixins.
There are also some generic views for tasks which we’ll get to later,
but you may want to design your own structure of reusable views which suits your use case.

For more information, please see https://docs.djangoproject.com/en/3.2/topics/class-based-views/.
"""
from django.http import HttpResponse


def health(request):
    """health check"""
    return HttpResponse('all is good here')
