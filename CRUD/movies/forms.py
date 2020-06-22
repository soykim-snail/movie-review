from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='영화명',
        widget=forms.TextInput(
            attrs={
                'class': 'my-movie',
            }
        )        
    )
    title_en = forms.CharField(
        label='영화명(영문)',
        widget=forms.TextInput(
            attrs={
                'class': 'my-movie',
            }
        )
    )
    audience = forms.IntegerField(
        label='누적 관객수'
    )
    open_date = forms.DateField(
        label='개봉일'
    )
    genre = forms.CharField(
        label='장르'
    )
    watch_grade = forms.CharField(
        label='관람등급'
    )
    score = forms.FloatField(
        label='평점'
    )
    poster_url = forms.CharField(
        label='포스터 이미지 URL'
    )
    description = forms.CharField(
        label='영화 소개',
        widget=forms.Textarea(
            attrs={
                'class': ''                
            }
        )
    )


    class Meta:
        model = Movie
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)