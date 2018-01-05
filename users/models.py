from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
#画风标签
class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#分类    
class Category(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='photo', null=True, blank=True)


    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

#约稿发布约稿信息！
class Post(models.Model):


    # 约稿信息标题
    title = models.CharField(max_length=70)

    # 约稿信息正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于约稿信息的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField()

    # 这两个列分别表示约稿信息的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    # 约稿信息摘要，可以没有约稿信息摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把约稿信息对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇约稿信息只能对应一个分类，但是一个分类下可以有多篇约稿信息，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇约稿信息可以有多个标签，同一个标签下也可能有多篇约稿信息，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定约稿信息可以没有标签，因此为标签 tags 指定了 blank=True。
    # 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    category = models.ForeignKey(Category)
    #tags = models.ManyToManyField(Tag, blank=True)

    # 约稿信息作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把约稿信息和 User 关联了起来。
    # 因为我们规定一篇约稿信息只能有一个作者，而一个作者可能会写多篇约稿信息，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User,related_name='web_post')

    def get_absolute_url(self):
        return reverse('users:post_detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title


class works(models.Model):

    work = models.ImageField(upload_to='photo', null=True, blank=True)
    author = models.ForeignKey(User,related_name='web_work')
    tags = models.ForeignKey(Tag, blank=True)
    intorduce   = models.TextField(max_length=500, blank=True)
    titles= models.CharField(max_length=70,blank=True)
    def get_work_url(self):
        return reverse('usworkpost_detail', kwargs={'pk': self.pk})





class Comment(models.Model):
    email = models.EmailField(max_length=255)

    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    avatar = models.ForeignKey(Profile,null=True)
    author = models.ForeignKey(User,null=True)
    post = models.ForeignKey(Post)


    def __str__(self):
        return self.text[:20]



from tinymce.models import HTMLField
import tinymce


class admin_Post(models.Model):
    title = models.CharField(max_length=70)

    # 约稿信息正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于约稿信息的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField()

    # 这两个列分别表示约稿信息的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('users:admin_post_detail', kwargs={'pk': self.pk})