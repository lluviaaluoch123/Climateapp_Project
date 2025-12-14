from django.db import models
from django.contrib.auth.models import User

# Contact form submissions
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # use DateTimeField for consistency

    def __str__(self):
        return f"{self.name} : {self.email} : {self.subject}"

'''
# Climate news articles
class ClimateNews(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    summary = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    '''

'''
class ClimateNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
'''

class ClimateNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]



# Climate technology / innovations
class ClimateTech(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='trends_images/', blank=True, null=True)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Community climate stories (general)
class ClimateStory(models.Model):
    title = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    image = models.ImageField(upload_to='stories_images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

'''
# Climate news submitted by users
class ClimateNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
'''

# Community stories with moderation
class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="stories/", blank=True, null=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Climate research articles
class Research(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    link = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Climate events
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
