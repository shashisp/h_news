from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import FormView
import news.models as models
from django.contrib.auth.decorators import login_required
from news.forms import *
from django.http import HttpResponseRedirect, HttpResponse

def home(request):

	return render(request, 'dashboard.html')


class ArticleListView(ListView):
	model = models.Article
	queryset = models.Article.objects.all()
	template_name = 'dashboard.html'
	paginate_by = 5



@login_required(login_url='/login/')
def create_new(request):
    if request.method == 'GET':
        form = ArticleForm()
    else:
        
        form = ArticleForm(request.POST)
        
        if form.is_valid():
        	title = form.cleaned_data['title']
        	url = form.cleaned_data['url']
        	description = form.cleaned_data['description']
        	posted_by = request.user
        	posted_on = timezone.now()
        	comments = 0
        	up_votes = 0
        	hn_id = 0
        	hn_url = "htt://abc.com"
        	article = models.Article.objects.create(title=title, url=url,
        				posted_on=posted_on, posted_by=posted_by, up_votes=up_votes,
        				comments=comments,
        				hn_id=hn_id,
        				hn_url=hn_url,
        				description=description)
        	return HttpResponseRedirect('/')
 
    return render(request, 'news/new.html', {
        'form': form,
    })


class VoteFormView(FormView):
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
