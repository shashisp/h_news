from django.forms import ModelForm
from news.models import Article, Vote, Read, Delete


class ArticleForm(ModelForm):

	class Meta(ModelForm):
		model = Article
		fields = ('title', 'url', 'description')
		excludes = ('hn_id', 'hn_url',
					'posted_by', 'comments', 'up_votes' ,'posted_on')

	def __init__(self, *args, **kwargs):
		super(ArticleForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({'class' : 'form-control input', 'placeholder':'Title'})
		self.fields['url'].widget.attrs.update({'class' : 'form-control', 'placeholder':'link'})
		self.fields['description'].widget.attrs.update({'class':'form-control', 'placeholder': 'Description (optional)'})


	def clean(self):
		pass


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ('article', 'voted_by')


class ReadForm(ModelForm):
    class Meta:
        model = Read
        fields = ('article', 'read_by')


class DeleteForm(ModelForm):
    class Meta:
        model = Delete
        fields = ('article', 'deleted_by')

