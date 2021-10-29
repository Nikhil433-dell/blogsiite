from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    query = models.TextField()
    
    def __str__(self):
        return f" Message from {self.name}"


class Blog(models.Model):
    topic_name = models.CharField(max_length=15)
    writer_name = models.ForeignKey(User, on_delete=models.CASCADE, default="none")
    category = models.CharField(max_length=15)
    blog_img = models.ImageField(null=True, blank=True, upload_to="media/")
    desc = models.TextField()
    parent_blog = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created = models.DateField(auto_now_add=True)
    liked = models.ManyToManyField(User, blank=True, related_name='likes')
    question = models.CharField(max_length=300 , blank=True)
    

    def __str__(self):
        return f"{self.topic_name} from {self.writer_name} "

    def num_likes(self):
        return self.liked.all().count()

    def num_comments(self):
        return self.comment_set.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"



    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,related_name="comments", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    comment_blog = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"Comment by {self.user} for  {self.post} "
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    pro_img = models.ImageField(null=True, blank=True, upload_to="media/")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField(User, related_name="is_following", blank=True)
    # following = models.ManyToManyField(User, related_name="following", blank=True)


    def __str__(self):
        return str(self.user.username)


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        default_user_profile.followers.add(instance)
        profile.followers.add(default_user_profile.user)


    post_save.connect(post_save_user_receiver, sender=User)
    
