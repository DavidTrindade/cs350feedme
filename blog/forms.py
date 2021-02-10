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

    def clean(self):
        cleaned_data = super().clean()
        feed_link = cleaned_data.get("feed_link")

        try:
            validator = URLValidator(message="Enter a valid URL")
            validator(feed_link)
            try:
                f = fp.parse(feed_link)
                if 'bozo' in f:
                    if f.bozo == 1:
                        self.add_error('feed_link', "Link is not a valid Feed")
            except URLError:
                self.add_error('feed_link', "Link is not a Feed")
        except ValidationError as e:
            self.add_error('feed_link', e)

        return cleaned_data

    def save(self, commit=True):
        feed = super(FaveForm, self).save(commit=False)
        f = fp.parse(self.cleaned_data["feed_link"])
        feed.title = f.feed.title
        feed.desc = f.feed.description
        feed.link = f.feed.link
        if commit:
            feed.save()
        return feed
