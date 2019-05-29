from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


from bbs import models,comment_hader
import json


# Create your views here.

category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')


def index(request):
    category_obj = models.Category.objects.get(position_index=1 )
    article_list = models.Article.objects.filter(status='published')
    return render(request,'bbs/index.html',{'category_list':category_list,
                                            'category_obj': category_obj,
                                            'article_list':article_list})



def category(request,id):
    category_obj = models.Category.objects.get(id=id)
    if category_obj.position_index == 1:    #如果是首页
        article_list = models.Article.objects.filter(status='published')
    else:
        article_list = models.Article.objects.filter(category_id=category_obj.id,status='published')
    return render(request,'bbs/index.html',{'category_list':category_list,
                                            'category_obj':category_obj,
                                            'article_list':article_list})

def acc_login(request,):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            # pass authentication
            login(request,user)
            return HttpResponseRedirect(request.GET.get('next') or '/bbs')

        else:
            login_error = '错误的用户名或密码 请重新输入!!!'
            return render(request, 'login.html', {'login_error':login_error})

    return render(request, 'login.html')


def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/bbs')



def  article_detail(request,articlt_id):
   article_obj = models.Article.objects.get(id=articlt_id)
   comment_tree = comment_hader.build_tree(article_obj.comment_set.select_related())
   return render(request,'bbs/article_detail.html',{'article_obj':article_obj,
                                                    'category_list':category_list,})


def post_comment(request):
    print(request.POST)
    if request.method == "POST":
        new_comment_obj = models.Comment(
            article_id=request.POST.get('article_id'),
            parent_comment_id=request.POST.get('parent_comment_id'),
            comment_type=request.POST.get('comment_type'),
            user_id=request.user.userprofile.id,
            comment=request.POST.get('comment')
        )

        new_comment_obj.save()

        return HttpResponse('post-comment-success')



def get_comments(request, article_id):
    article_obj = models.Article.objects.get(id=article_id)
    comment_tree = comment_hader.build_tree(article_obj.comment_set.select_related())
    tree_html = comment_hader.render_comment_tree(comment_tree)

    return HttpResponse(tree_html)