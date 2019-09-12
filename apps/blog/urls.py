from django.conf.urls import url

from .views import IndexView, BigCategoryView, ArticleCategoryView, ArticleDetailView, TagArticleView, DateArticleView, \
    AddLikeView, AddCommentsView  # MessageView
from users.views import LogoutView, LoginView, RegisterView, ForgetPwdView, ActiveUserView

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
    url(r'^add_like/$', AddLikeView, name="add_like"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    # url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    # url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),
]
