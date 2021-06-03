from django.forms import ModelForm
from main_app.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'text', 'user_name']


