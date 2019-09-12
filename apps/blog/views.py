from django.core.paginator import Paginator, PageNotAnInteger
# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import ArticleComments
from .models import Article, BigCategory, ArticleCategory, Banner, ArticleTag


class IndexView(View):
    def get(self, request):
        articles = Article.objects.all().order_by("-add_time")
        hot_articles = articles.order_by("-like_nums")[:5]
        left_big_banners = Banner.objects.filter(number__lte=5)
        # like_articles = articles.order_by("-read_nums")[:10]

        # big_categories = BigCategory.objects.all().order_by('add_time')
        # article_categories = ArticleCategory.objects.all()

        # 分页机制 Django1.11 官方文档
        # paginator = Paginator(contact_list, 25)  # Show 25 contacts per page
        #
        # page = request.GET.get('page')
        # try:
        #     contacts = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     contacts = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     contacts = paginator.page(paginator.num_pages)

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)  # 因为用get方法，如果get到的是空，就把1返回，所以下面的异常处理不需要考虑EmptyPage，只需处理PageNotAnInteger一场
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 10)  # Show 10 contacts per page

        all_articles = p.page(page)

        return render(request, "index.html", {
            'articles': all_articles,
            'hot_articles': hot_articles,
            'banner_articles': left_big_banners,
            # 'like_articles': like_articles
            # 'big_categorys': big_categories,
            # 'article_categorys': article_categories
        })


class BigCategoryView(View):
    def get(self, request, big_slug):
        # big_category = BigCategory.objects.get(id=int(big_id))
        if big_slug == "resources":
            return render(request, 'resources.html', {
                "category": "resources"
            })
        if big_slug == "about":
            return render(request, 'about.html', {
                "category": "about"
            })
        if big_slug == "message":
            return render(request, 'message.html', {
                "category": "message"
            })
        if big_slug == "reward":
            return render(request, 'reward.html', {
                "category": "reward"
            })
        if big_slug == "exchange":
            return render(request, 'exchange.html', {
                "category": "exchange"
            })
        if big_slug == "question":
            return render(request, 'question.html', {
                "category": "question"
            })
        if big_slug == "cooperation":
            return render(request, 'cooperation.html', {
                "category": "cooperation"
            })
        big_category = BigCategory.objects.get(slug=big_slug)
        all_articles = big_category.get_big_category_article()
        # all_articles = Article.objects.get(big_category=big_category)

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)  # 因为用get方法，如果get到的是空，就把1返回，所以下面的异常处理不需要考虑EmptyPage，只需处理PageNotAnInteger一场
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 10)  # Show 10 contacts per page

        all_articles = p.page(page)

        return render(request, 'categorypage.html', {
            "all_articles": all_articles,
        })


class ArticleCategoryView(View):
    def get(self, request, big_slug, category_slug):
        category = ArticleCategory.objects.get(slug=category_slug)
        all_articles = category.get_category_article()

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)  # 因为用get方法，如果get到的是空，就把1返回，所以下面的异常处理不需要考虑EmptyPage，只需处理PageNotAnInteger一场
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 10)  # Show 10 contacts per page

        all_articles = p.page(page)

        return render(request, 'categorypage.html', {
            "all_articles": all_articles,
        })


class ArticleDetailView(View):
    def get(self, request, article_id):
        articles = Article.objects.get(id=int(article_id))
        articles.read_nums += 1
        articles.save()
        return render(request, 'article.html', {
            'article': articles
        })


class TagArticleView(View):
    def get(self, request, tag_id):
        tag = ArticleTag.objects.get(id=int(tag_id))
        all_articles = Article.objects.filter(tag=tag)

        return render(request, 'categorypage.html', {
            'all_articles': all_articles
        })


class DateArticleView(View):
    def get(self, request, year, month):
        all_articles = Article.objects.filter(add_time__year=year, add_time__month=month)
        return render(request, 'categorypage.html', {
            'all_articles': all_articles
        })


# class AddLikeView(View):
#     def post(self, request):
#         article_id = request.POST.get('article_id', '')
#         if article_id:
#             article = Article.objects.get(id=int(article_id))
#             article.like_nums += 1
#             article.save()
#             return HttpResponse('{"status":"success","msg":"您已经点过赞了"}', content_type='application/json')
#         else:
#             return HttpResponse('{"status":"fail","msg":"点赞出错了"}', content_type='application/json')


@csrf_exempt
def AddLikeView(request):
    article_id = request.POST.get('article_id', '')
    if article_id:
        article = Article.objects.get(id=int(article_id))
        article.like_nums += 1
        article.save()
        return HttpResponse('{"status":"success","msg":"您已经点过赞了"}', content_type='application/json')
    else:
        return HttpResponse('{"status":"fail","msg":"点赞出错了"}', content_type='application/json')


def page_not_found(request):
    # 全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    # 全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response


# class CommentView(View):
#     def get(self, request, article_id):
#         article = Article.objects.get(id=int(article_id))
#         all_comments = ArticleComments.objects.filter(article=article)
#         # all_resources = CourseResource.objects.filter(course=course)
#         # user_courses = UserCourse.objects.filter(course=course)
#         user_ids = [all_comment.user.id for all_comment in all_comments]
#         user_counts = user_ids.count()
#         # all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
#         # 取出所有课程ID
#         # course_ids = [user_courses.course.id for user_courses in all_user_courses]
#         # 获取用户学过的相关课程
#         # relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
#         return render(request, 'comment/comment_list.html', {
#             'all_comments': all_comments,
#             'user_count': user_counts
#             })


class AddCommentsView(View):
    def post(self, request):
        article_id = request.POST.get('article_id', 0)
        comments = request.POST.get('comments', '')
        if int(article_id) > 0 and comments:
            article_comments = ArticleComments()
            article = Article.objects.get(id=int(article_id))
            article_comments.article = article
            article_comments.comments = comments
            article_comments.user = request.user
            article_comments.save()
            return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加失败"}', content_type='application/json')
