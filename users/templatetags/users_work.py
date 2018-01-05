
from django import template
from ..models import works
from ..models import Post, Category,User,Tag
register = template.Library()
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()


@register.simple_tag
def get_works():
    return Tag.objects.all()

