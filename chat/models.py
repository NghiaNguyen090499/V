from django.db import models
from django import forms


class Voting(models.Model):
    question = models.CharField(max_length=255)
    options = models.TextField()
    is_open = models.BooleanField(default=False)


class AuthenticationMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class AuthForm(forms.Form):
    authentication_methods = forms.ModelMultipleChoiceField(
        queryset=AuthenticationMethod.objects.all(),
        widget=forms.CheckboxSelectMultiple,    
        label="Chọn phương thức xác thực",
    )
    
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    authentication_methods = models.ManyToManyField(AuthenticationMethod)

    def __str__(self):
        return self.question


class ImageReview(models.Model):
    image = models.ImageField(upload_to='review_images/')
    question = models.ForeignKey(Poll, on_delete=models.CASCADE)
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200 )
    votes = models.IntegerField(default=0)      
    image_review = models.ForeignKey(ImageReview, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
    
    

