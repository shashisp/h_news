from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
import news.models as models
from django.contrib.auth.decorators import login_required
from news.forms import *
from django.http import HttpResponseRedirect, HttpResponse



class ArticleListView(ListView):
    """ generic list view to render list of articles
    """ 
    model = models.Article
    queryset = models.Article.objects.all()
    template_name = 'dashboard.html'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            deleted = models.Delete.objects.filter(deleted_by=self.request.user)
            deleted = deleted.values_list('article', flat=True)

            #Dont render deleted objects
            self.object_list = self.object_list.exclude(id__in=deleted)
            context['object_list'] = self.object_list
  
            voted = models.Vote.objects.filter(voted_by=self.request.user)
            articles_in_page = [article.id for article in context["object_list"]]
            voted = voted.filter(article_id__in=articles_in_page)
            voted = voted.values_list('article_id', flat=True)
            context["voted"] = voted
            
            read = models.Read.objects.filter(read_by=self.request.user)
            read = read.filter(article_id__in=articles_in_page)
            read = read.values_list('article_id', flat=True)
            context['read'] = read


        return context


@login_required(login_url='/login/')
def create_new(request):
    """ Method to create new article manually
    """
    if request.method == 'GET':
        form = ArticleForm()
    else:
        
        form = ArticleForm(request.POST)
        
        if form.is_valid():
        	title = form.cleaned_data['title']
        	url = form.cleaned_data['url']
        	description = form.cleaned_data['description']
        	posted_by = request.user #requested user (loggedin)
        	posted_on = timezone.now() #current time
        	article = models.Article.objects.create(title=title, url=url,
        				posted_on=posted_on, posted_by=posted_by,
        				description=description)
        	return HttpResponseRedirect('/')
 
    return render(request, 'news/new.html', {
        'form': form,
    })


class VoteFormView(FormView):
    """ generic form view to send votes
    """
    form_class = VoteForm


    def form_valid(self, form):
        article = get_object_or_404(models.Article, pk=form.data["article"])
        user = self.request.user
        prev_vote = models.Vote.objects.filter(article=article, voted_by=user)
        has_voted = prev_vote.count() > 0

        if not has_voted:
            models.Vote.objects.create(article=article, voted_by=user)
        else:
            prev_vote[0].delete()

        return HttpResponseRedirect('/')

class ReadFormView(FormView):
    """ generic form view to mark as read
    """
    form_class = ReadForm


    def form_valid(self, form):
        article = get_object_or_404(models.Article, pk=form.data["article"])
        user = self.request.user
        prev_read = models.Read.objects.filter(article=article, read_by=user)
        has_read = prev_read.count() > 0

        if not has_read:
            models.Read.objects.create(article=article, read_by=user)
        else:
            prev_read[0].delete()

        return HttpResponseRedirect('/')

class DeleteFormView(FormView):
    """ generic form view to mark as read
    """
    form_class = DeleteForm


    def form_valid(self, form):
        article = get_object_or_404(models.Article, pk=form.data["article"])
        user = self.request.user
        prev_delete = models.Delete.objects.filter(article=article, deleted_by=user)
        has_deleted = prev_delete.count() > 0

        if not has_deleted:
            models.Delete.objects.create(article=article, deleted_by=user)
        else:
            prev_delete[0].delete()

        return HttpResponseRedirect('/')

class ArticleDetailView(DetailView):
    model = models.Article
    slug_field = "title"
    template_name = "news/article_detail.html"