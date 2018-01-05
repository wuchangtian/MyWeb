from django.shortcuts import render
from .models import User
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import RegisterForm,UserForm,ProfileForm,PostForm,worksForm
from .models import Post,works,Category,Tag,admin_Post
from django.core.urlresolvers import reverse
from django.views.generic import ListView
import markdown
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm


class IndexView(ListView):
    model = Post
    template_name = 'artist/typo.html'
    context_object_name = 'post_list'
    paginate_by = 6
    #类视觉函数-分页

def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST, instance=request.user)
        profile_form = ProfileForm(data=request.POST, instance=request.user.profile)
        if user_form.is_valid()and profile_form.is_valid():
            user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            profile_form.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'avatar2' in request.FILES:
               user.profile.avatar2 = request.FILES['avatar2']


            # Now we save the UserProfile model instance.
            #user.profile.save()

            return redirect('index')
        else:
            return redirect('index')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })






def index(request):
    return render(request, 'index.html')


def work_detail2(request, pk):
    # 记得在开始部分导入 Category 类
   user = get_object_or_404(Tag, pk=pk)
   post_list1 = works.objects.filter(tags=user)
   return render(request, 'artist/typoshow_detail.html', context={'post_list1': post_list1})
def work_detail(request, pk):
    post = get_object_or_404(works, pk=pk)

    return render(request, 'artist/typoshow_detail.html', {'post': post})

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'artist/typoshow_detail.html', context={'post_list': post_list})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'users/post_detail.html', context=context)



def works_new(request):
    if request.method == "POST":
        work_form = worksForm(request.POST)
        if work_form.is_valid():
            img = work_form.save(commit=False)
            img.author=request.user
            img.work=request.FILES['work']
            img.save()
            return redirect('/', pk=img.pk)
    else:
        work_form = worksForm()
    return render(request, 'users/works.html', {'work_form': work_form})

def posting(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'artist/typo.html', context={'post_list': post_list})

def posting_work(request):
    post_list = works.objects.all()
    return render(request, 'artist/typoshow.html', context={'post_list': post_list})

def post_comment(request, post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    post = get_object_or_404(Post, pk=post_pk)

    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = CommentForm(request.POST)

        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            comment.author=request.user
            # 将评论和被评论的文章关联起来。
            comment.post = post
            comment.avatar=request.user.profile
            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()

            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)

        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # 具体请看下面的讲解。
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'users/post_detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(post)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'artist/single.html', {'form': form})
@login_required
def post_delete(request):

    #先过滤，加上过滤的条件，然后用delete()
    #向server端传参数方式
    #1，通过数据 http://127.0.0.1:8000/blog/?id=2
    #2, 通过路径  http://17.0.0.1:8000/blog/20
                        # url(r'blog/(\d{4})')
    #在前端页面加上id值，{{post.id}}

    #通过url获取iD，是get的方法，"id"是url里的key,
    id = request.GET.get("id")
    #前面的id是表里的字段，把get从地址栏里获取到的id赋值给表里的id，就可以删除
    #
    Post.objects.filter(id = id).delete()
    return render(request, 'artist/gallery.html')

def post_edit(request,pk):

    obj = Post.objects.get(pk=pk)
    if request.method == 'POST':
            obj.title = request.POST.get('title')
            obj.body = request.POST.get('body')
            obj.save()

            return redirect('/gallery.html')

    return render(request,'users/post_edit.html',{'obj':obj})

def work_delete(request):


    id = request.GET.get("id")


    works.objects.filter(id = id).delete()
    return render(request, 'artist/gallery.html')





def admin_posting(request):
    post_list = admin_Post.objects.all()
    return render(request, 'artist/services.html', context={'post_list': post_list})


def admin_post_detail(request, pk):
    post123 = get_object_or_404(admin_Post, pk=pk)

    return render(request, 'artist/service_detail.html', {'post123': post123})












