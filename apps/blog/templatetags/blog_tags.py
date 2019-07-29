from django import template
from ..models import BigCategory, ArticleCategory, ArticleTag, Article, Banner

register = template.Library()


@register.simple_tag
def get_big_category():
    return BigCategory.objects.all()


@register.simple_tag
def get_category(big_category):
    return ArticleCategory.objects.filter(bigCategory=big_category)


@register.simple_tag
def get_all_tags():
    return ArticleTag.objects.all()


@register.simple_tag
def get_tag_article_list(tag):
    """返回当前标签下所有发表的文章列表"""
    return Article.objects.filter(tag=tag)


@register.simple_tag
def get_article_public_date():
    article_dates = Article.objects.datetimes('add_time', 'month', order='DESC')
    return article_dates


@register.simple_tag
def get_like_articles():
    return Article.objects.all().order_by('-like_nums')[:8]


# 获取右侧栏热门专题幻灯片查询集
@register.simple_tag
def get_banner_right():
    return Banner.objects.filter(number__gt=5, number__lte=10)


