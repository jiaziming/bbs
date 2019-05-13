from django.shortcuts import render


from bbs import models


# Create your views here.

def index(request):

    category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')
    return render(request,'bbs/index.html',{'category_list':category_list})