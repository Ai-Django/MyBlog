from django.contrib import admin

# Register your models here.
from blog.models import ArticleCategory, Article, ArticleTag, BigCategory, Banner, Keyword


class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'add_time')


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'add_time')


class BigCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_time')


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'add_time')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'category', 'add_time', 'show_tag')
    list_filter = ('add_time', 'category')
    list_per_page = 50

    def show_tag(self, obj):
        return [ta.name for ta in obj.tag.all()]

    # def get_image_name(self, obj):
    #     image = datetime.now().strftime('%Y%m%d%H%M%S') + obj.image
    #     return image

    filter_horizontal = ('tag', )


class BannerAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'content', 'image', 'url')


admin.site.site_title = "管理系统"
admin.site.site_header = "Blog后台管理系统"


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(BigCategory, BigCategoryAdmin)
admin.site.register(Banner, BannerAdmin)
# admin.site.register(Keyword, KeywordAdmin)

