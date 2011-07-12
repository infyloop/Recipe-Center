from django.http import HttpResponse
from django.shortcuts import render_to_response
from recipe.models import RecipeDump


def hello(request):
    return HttpResponse("Hello world")

def datadisp(request):
    obj = RecipeDump.objects.all()[1]
    cat_name = obj.category_name
    name = obj.name

   # ingredients = obj.ingredients
    output = 'Name %s, Category %s ' %(name, cat_name)
    output = '<html><body>%s</body></html>' %output
    return HttpResponse(output)
