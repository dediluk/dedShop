from django import forms

from .models import Reviews, RatingStar, Rating
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class ReviewForm(forms.ModelForm):
    """Форма для отправки отзывов"""
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'captcha')
        widgets = { #для рендеринга хтмл формы.
            'name': forms.TextInput(attrs={'class': "form-control border"}),
            'email': forms.EmailInput(attrs={'class': "form-control border"}),
            'text': forms.Textarea(attrs={'class': "form-control border"})
        }


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)


