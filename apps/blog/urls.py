from django.conf.urls import url

from .views import IndexView, BigCategoryView, ArticleCategoryView, ArticleDetailView, TagArticleView, DateArticleView, AddLikeView  # MessageView
from users.views import LogoutView, LoginView, RegisterView, ForgetPwdView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    # url(r'^category/(?P<big_slug>.*?)/$', BigCategoryView.as_view(), name="big_category"),
    url(r'^category/(?P<big_slug>[^/]+)/$', BigCategoryView.as_view(), name="big_category"),
    url(r'^category/(?P<big_slug>[^/]+)/(?P<category_slug>[^/]+)/$', ArticleCategoryView.as_view(), name="article_category"),
    url(r'^article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name="article_detail"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagArticleView.as_view(), name="tag"),
    url(r'^date/(?P<year>\d+)/(?P<month>\d+)/$', DateArticleView.as_view(), name="date"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # 喜欢
    # url(r'^love/$', LoveView, name='love'),
    url(r'^add_like/$', AddLikeView, name="add_like"),
    # url(r'^category/about/$', AboutView, name='about'),
    # url(r'^category/donate/$', DonateView, name='donate'),
    # url(r'^category/exchange/$', ExchangeView, name='exchange'),
    # url(r'^category/project/$', ProjectView, name='project'),
    # url(r'^category/question/$', QuestionView, name='question'),
]
