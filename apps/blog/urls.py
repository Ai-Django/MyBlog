from django.conf.urls import url

from .views import IndexView, BigCategoryView, ArticleCategoryView, ArticleDetailView, TagArticleView, DateArticleView  # MessageView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    # url(r'^category/(?P<big_slug>.*?)/$', BigCategoryView.as_view(), name="big_category"),
    url(r'^category/(?P<big_slug>[^/]+)/$', BigCategoryView.as_view(), name="big_category"),
    url(r'^category/(?P<big_slug>[^/]+)/(?P<category_slug>[^/]+)/$', ArticleCategoryView.as_view(), name="article_category"),
    url(r'^article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name="article_detail"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagArticleView.as_view(), name="tag"),
    url(r'^date/(?P<year>\d+)/(?P<month>\d+)/$', DateArticleView.as_view(), name="date"),
    # url(r'^category/about/$', AboutView, name='about'),
    # url(r'^category/donate/$', DonateView, name='donate'),
    # url(r'^category/exchange/$', ExchangeView, name='exchange'),
    # url(r'^category/project/$', ProjectView, name='project'),
    # url(r'^category/question/$', QuestionView, name='question'),
]
