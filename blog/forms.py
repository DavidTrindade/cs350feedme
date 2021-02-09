from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from urllib.error import URLError
from .models import Feed
import feedparser as fp

class FaveForm(forms.ModelForm):

    class Meta:
        model = Feed
        fields = ('feed_link',)

    def clean_link(self):
        cleaned_data = self.cleaned_data['feed_link']

        validator = URLValidator(message="Enter valid URL")
        validator(cleaned_data)
        try:
            f = fp.parse(cleaned_data)
            if 'bozo' in f:
                if f.bozo == 1:
                    raise ValidationError("Link is not a valid Feed")
        except URLError:
            self.add_error('feed_link', "Link is not a Feed")

        return cleaned_data

    def save(self, commit=True):
        feed = super(FaveForm, self).save(commit=False)
        f = fp.parse(feed.feed_link)
        feed.title = f.feed.title
        feed.desc = f.feed.description
        feed.link = f.feed.link
        if commit:
            feed.save()
        return feed
