from django.http import HttpResponse
from django.shortcuts import render_to_response
from recipe.models import RecipeDump
from django.template import Context, loader
from django.http import Http404


def hello(request):
    return HttpResponse("Hello world")

def detail(request, recipe_id=None):
    try:
        p = RecipeDump.objects.get(pk=recipe_id)
    except RecipeDump.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'recipe': p})

def index(request):
    obj = RecipeDump.objects.all()
    t = loader.get_template('index.html')
    c = Context({
        'obj': obj,
    })
    return HttpResponse(t.render(c)) 

# def datadisp(request):         
    # obj = RecipeDump.objects.all()[1]
   #  cat_name = obj.category_name
   #  name = obj.name

    # ingredients = obj.ingredients
   #  output = 'Name %s, Category %s ' %(name, cat_name)
   #  output = '<html><body>%s</body></html>' %output
    # t = get_template('display.html')
   
    #  html = t.render(Context()
    # return HttpResponse(output)

