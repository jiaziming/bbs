from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255,verbose_name=u'标题')
    brief = models.CharField(null=True,blank=True,max_length=255,verbose_name=u'简介')
    category = models.ForeignKey("Category",on_delete=models.CASCADE,verbose_name=u'类别')
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    pub_date = models.DateTimeField(blank=True,null=True)
    last_modify = models.DateField(auto_now=True)
    priority = models.IntegerField(u'优先级',default=1000)
    head_img = models.ImageField(u'文章标题图片',upload_to="Img")
    status_choices = (('draft',u'草稿'),
                      ('published',u'发布'),
                      ('hidden',u'隐藏'))
    status = models.CharField(choices=status_choices,default='published',max_length=255)

    class Meta:
        verbose_name_plural = u'文章'

    def __str__(self):
        return self.title



    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(('Draft entries may not have a publication date.'))
        # Set the pub_date for published items if it hasn't been set already.
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()



class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=u'所属文章',on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self',related_name='my_children',blank=True,null=True,on_delete=models.CASCADE)
    comment_choices = (('1',u'评论'),
                       ('2',u'点赞'))
    comment_type = models.CharField(choices=comment_choices,default='1',max_length=255)

    comment = models.TextField(blank=True,null=True)
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = u'评论'

    def clean(self):
        if self.comment_type == 1 and len(self.comment) == 0:
            raise ValidationError("评论内容不能为空")

    def __str__(self):
        return  "c:%s" %(self.comment)



class Category(models.Model):
    name = models.CharField(max_length=128)
    brief = models.CharField(null=True,blank=True,max_length=255)
    set_as_top_menu =models.BooleanField(default=False)
    position_index = models.SmallIntegerField()
    admin = models.ManyToManyField("UserProfile",blank=True)

    class Meta:
        verbose_name_plural = u'类别'

    def __str__(self):
        return self.name

class  UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    sigature = models.CharField(max_length=255,blank=True,null=True)
    head_img = models.ImageField(height_field=150,width_field=150,blank=True,null=True)


    #web qq models
    friends = models.ManyToManyField('self',related_name="my_friends",blank=True)

    class Meta:
        verbose_name_plural = u'用户信息'

    def __str__(self):
        return self.name