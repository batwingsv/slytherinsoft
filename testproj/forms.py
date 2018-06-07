from django import forms
from testproj.models import Ideas
from django.forms import ModelForm, Textarea
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class IdeasForm(ModelForm):
    #text = forms.CharField(widget=forms.Textarea, label='Entry')
    title = forms.CharField(help_text='Enter title')
    cover = forms.ImageField(help_text='Choose cover image')
    content = forms.CharField(widget=SummernoteWidget())
    #text = forms.CharField(widget=TinyMCEWidget(attrs={'cols': 80, 'rows': 30}), label='Entry')
    class Meta:
        model = Ideas
        exclude = ['likes']
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }

class AddIdeaAuthorized(forms.Form):
    ideaadd_title_auth = forms.CharField(label='Idea Title: ', max_length=100)
    ideaadd_text_auth = forms.CharField(label='Idea Text: ', widget=SummernoteWidget())
    ideaadd_cover_auth = forms.ImageField()

