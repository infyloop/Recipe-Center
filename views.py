from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render_to_response
from recipe.models import RecipeDump
from django.template import Context, loader
from django.http import Http404


def hello(request):
    return HttpResponse("Hello world")

def detail(request, recipe_id=None):
    try:
        p = RecipeDump.objects.filter(slug=recipe_id)[0]
    except IndexError:
        raise Http404
    return render_to_response('detail.html', {'recipe': p})

def index(request):
    obj = RecipeDump.objects.all()
    paginator = Paginator(obj,20)#show 20 recipes per page
    page = request.GET.get('page', 1)
    try:
         recipes = paginator.page(page)
    except PageNotAnInteger:
      # If page is not an integer, deliver first page.
      recipes = paginator.page(1)
    except EmptyPage:
      #If page is out of range, deliver last page of results.
      recipes = paginator.page(paginator.num_pages)
    t = loader.get_template('index.html')
    c = Context({
        'recipes': recipes,
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

