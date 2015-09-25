from django.contrib import admin
import news.models as models


class ArticleAdmin(admin.ModelAdmin):
	model = models.Article
	list_display = ('title','posted_on', 'comments', 'up_votes')


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Vote)
admin.site.register(models.Read)
admin.site.register(models.Delete)