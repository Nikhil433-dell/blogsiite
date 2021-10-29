from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import  Contact, Blog, Like, Comment, Profile
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def index(request):
    try:

        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            query = request.POST['query']
            contact = Contact(name=name, email=email, query=query)
            contact.save()
            send_mail(f'Hello {name}!',f' Thank You for giving the feedback. \n \n Your message has been received.     You will receive a response from us within 1-2 business days. Please do not reply to this email id. \n \n Hope you are enjoying well. \n \n  From: Blogsite \n To: {email}', 'blogsiteofficial7@gmail.com', [email],  fail_silently=False)
    except Exception as e:
        print(e)
    return render(request, 'index.html')



def loginUser(request):
    try:
        if request.method=="POST":
            email = request.POST.get('username')
            password = request.POST.get('password')

        # check if user has entered correct credentials
            user_obj = User.objects.get(email=email.lower())
            user = authenticate(username=user_obj, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home")
            else:
                messages.error(request, "Email not found!")
                return render(request, 'index.html')
    except Exception as e:
        print(e)

    return render(request, 'login.html')

def logoutUser(request):
    try:
        logout(request)
        print(f"{request.user}__logged out")
    except Exception as e:
        print(e)
    return redirect("/")


def new(request):
    try:
        if request.method == "POST":
            last_name = "None"
            email = request.POST['email']
            username = request.POST['username']
            first_name = username
            password1 = request.POST['pass1']
            password2 = request.POST['pass2']
            if password1 != password2:
                messages.error(request, "Error: Passwords not matching!")
                print("Passwords not matching!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Error: Email Taken!")
                print("Email Taken!")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Error: Username Taken!")
                print("Username Taken!")
            elif password1 == username:
                messages.error(request, "Password is not Strong!")
                print("Error: Password is not Strong!")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username,  password=password1)
                user.save()
                new_bio = Profile(user=user)
                new_bio.save()
                send_mail(f'Welcome {username}!', f'Congratulations! \n \n You have just joined thousands of people who are eager to mould their emotions in the form of blog by signing in on our website BLOGSITE.It will provide you the best platform to share your valuable experience in the form of words that may be going to affect positively the life of people who are the regular readers of it. \n \n We promise you to provide the best and original content .The unique point that you all must know is that our website offers you the chance to question a certain blog in case if you don’ t agree with the thoughts of writer as we respect the beliefs and philosphy and line of thinking of every person provided it is rational. \n \n Hope you are going to enjoy it. \n \n From: Blogsite \n To: {email}', 'blogsiteofficial7@gmail.com', [email],  fail_silently=False)
                return render(request, "login.html")
    except Exception as e:
        print(e)
    return render(request, "new.html")


@login_required
def home(request):
    try:
        if request.user.is_anonymous:
            return redirect("/login")
        allbloges = Blog.objects.all()
    except Exception as e:
        print(e)
    return render(request, 'home.html', {"blog": allbloges})


@login_required
def search(request):
    try:
        if request.method == "GET":
            inpu = request.GET["inpu"]
            if len(inpu) > 80:
                result = Blog.objects.none()
            else:
                result1 = Blog.objects.filter(topic_name__icontains=inpu)
                result2 = Blog.objects.filter(category__icontains=inpu)
                result3 = Blog.objects.filter(desc__icontains=inpu)
                result4 = Blog.objects.filter(question__icontains=inpu)
                result = result1.union(result2, result3, result4)

    except Exception as e:
        print(e)
    return render(request, "home_search.html" , {"inp": result, "inpu" : inpu})

@login_required
def feedback(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            query = request.POST['query']
            contact = Contact(name=name, email=email, query=query)
            contact.save()
            send_mail(f'Hello {name}!',f' Thank You for giving the feedback. \n \n Your message has been received.     You will receive a response from us within 1-2 business days. Please do not reply to this email id. \n \n Hope you are enjoying well. \n \n  From: Blogsite \n To: {email}', 'blogsiteofficial7@gmail.com', [email],  fail_silently=False)
            return redirect("home")
    except Exception as e:
        print(e)
    return render(request, "feedback.html")

@login_required
def like_unlike_post(request):
    try:
        username = request.user.username
        if request.method == 'POST':
            post_id = request.POST.get("post_id")
            post_obj = Blog.objects.get(id=post_id)
            profile = User.objects.get(username=username)

            if profile in post_obj.liked.all():
                post_obj.liked.remove(profile)
            else:
                post_obj.liked.add(profile)

            like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

            if not created:
                if like.value=='Like':
                    like.value='Unlike'
                else:
                    like.value='Like'
            else:
                like.value='Like'

                post_obj.save()
                like.save()
    except Exception as e:
        print(e)
    return redirect('home')


@login_required
def likePost(request):
    try:
        username = request.user.username
        if request.method == 'POST':
            post_id = request.POST.get("post_id")
            post_obj = Blog.objects.get(id=post_id)
            profile = User.objects.get(username=username)

            if profile in post_obj.liked.all():
                post_obj.liked.remove(profile)
            else:
                post_obj.liked.add(profile)

            like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

            if not created:
                if like.value=='Like':
                    like.value='Unlike'
                else:
                    like.value='Like'
            else:
                like.value='Like'

                post_obj.save()
                like.save()
    except Exception as e:
        print(e)
    return redirect(f"/main/{post_id}")


@login_required
def like(request):
    try:
        username = request.user.username
        if request.method == 'POST':
            post_id = request.POST.get("post_id")
            post_obj = Blog.objects.get(id=post_id)
            profile = User.objects.get(username=username)

            if profile in post_obj.liked.all():
                post_obj.liked.remove(profile)
            else:
                post_obj.liked.add(profile)

            like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

            if not created:
                if like.value=='Like':
                    like.value='Unlike'
                else:
                    like.value='Like'
            else:
                like.value='Like'

                post_obj.save()
                like.save()
        user = request.user
    except Exception as e:
        print(e)
    return redirect(f"/user_profile/{user.id}")






@login_required
def likeView(request):
    try:
        username = request.user.username
        if request.method == 'POST':
            post_id = request.POST.get("post_id")
            post_obj = Blog.objects.get(id=post_id)
            profile = User.objects.get(username=username)

            if profile in post_obj.liked.all():
                post_obj.liked.remove(profile)
            else:
                post_obj.liked.add(profile)

            like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

            if not created:
                if like.value=='Like':
                    like.value='Unlike'
                else:
                    like.value='Like'
            else:
                like.value='Like'

                post_obj.save()
                like.save()
        user = request.user
    except Exception as e:
        print(e)
    return redirect(f"/viewprofile/{post_obj.writer_name.id}")


@login_required
def showblog(request, pk):
    try:
        post = Blog.objects.filter(pk=pk).first()
        comments= Comment.objects.filter(post=post, parent=None)
        replies= Comment.objects.filter(post=post).exclude(parent=None)
        replyDict={}
        for reply in replies:
            if reply.parent.id not in replyDict.keys():
                replyDict[reply.parent.id]=[reply]
            else:
                replyDict[reply.parent.id].append(reply)
        context = {"blog":post,'replyDict': replyDict, 'comment': comments, "user": request.user}
    except Exception as e:
        print(e)
    return render(request, "main_post.html", context)

@login_required
def postComment(request, pk):
    try:
        if request.method == "POST":
            comment=request.POST.get('comment')
            user=request.user
            post_id = request.POST.get("post_id")
            post= Blog.objects.get(id=post_id)
            parentSno = request.POST.get("parentSno")
            if parentSno == "":
                new_comment = Comment(comment_blog= comment, user=user, post=post)
                new_comment.save()
            else:
                parent= Comment.objects.get(id=parentSno)
                comment=Comment(comment_blog= comment, user=user, post=post , parent=parent)
                comment.save()
    except Exception as e:
        print(e)
    return redirect(f"/main/{pk}")

@login_required
def create_blog(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            category = request.POST.get("category")
            desc = request.POST.get("desc")
            question = request.POST.get("question")
            images = request.FILES.get('image')
            user = request.user
            new_blog = Blog(topic_name=name, category=category, desc=desc, question=question, writer_name=user,     blog_img=images)
            new_blog.save()
            return redirect(f"/main/{new_blog.pk}")
    except Exception as e:
        print(e)
    return render(request, "addBlog.html")




@login_required
def user_profile(request, pk):
    try:
        user = request.user
        bloges = Blog.objects.filter(writer_name=user)
        if request.method == 'POST' and request.FILES['image']:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            url = fs.url(filename)
            id_us = Profile.objects.get(user__id=user.id)
            id_us.pro_img = image
            id_us.save()
        profile = Profile.objects.get(user=user)
        page = Profile.objects.get(user__id=pk)
        cont = {"blog" : bloges, "profile": profile, "page": page}
    except Exception as e:
        print(e)
    return render(request, "user_profile.html", cont)


@login_required
def delete_post(request, pk):
    try:
        post = Blog.objects.get(pk=pk)
        post.delete()
        user = request.user
    except Exception as e:
        print(e)
    return redirect(f"/user_profile/{user.id}")


@login_required
def edit_profile(request):
    try:
        user = request.user
        if request.method == 'POST':
            id_us = Profile.objects.get(user__id=user.id)
            id_us.bio = request.POST.get('bio')
            id_us.save()
            return redirect(f"/user_profile/{user.id}")
    except Exception as e:
        print(e)
    return render(request, "edit_profile.html")


@login_required
def view_profile(request, pk):
    try:
        current_user = request.GET.get('user')
        page = Profile.objects.get(user__id=pk)
        bloges = Blog.objects.filter(writer_name__id=pk)
        for e in page.followers.all():
            print(e)
        is_following = False
        if request.user in page.followers.all():
            is_following = True
        cont = {"blog" : bloges, "profile" : page, "current_user" : current_user, "is_following": is_following}
    except Exception as e:
        print(e)
    return render(request, "viewprofile.html", cont)



@login_required
def view_writer(request):
    try:
        users = User.objects.all().exclude(username=request.user.username)
        context = {"users": users}
    except Exception as e:
        print(e)
    return render(request, "writer.html", context)



@login_required
def writer_search(request):
    try:
        if request.method == "GET":
            inpu = request.GET["inpu"]
            if len(inpu) > 80:
                result = User.objects.none()
            else:
                result = User.objects.filter(username__icontains=inpu).exclude(username=request.user.username)
    except Exception as e:
        print(e)
    return render(request, "writersearch.html", {"result": result, "inpu": inpu})


def ansblog(request, pk):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            category = request.POST.get("category")
            desc = request.POST.get("desc")
            question = request.POST.get("question")
            image = request.FILES.get('image')
            post = Blog.objects.get(pk=pk)
            user = request.user
            new_blog = Blog(topic_name=name, category=category,parent_blog=post, desc=desc, question=question,  writer_name=user, blog_img=image)
            new_blog.save()
            return redirect(f"/main/{new_blog.pk}")
    except Exception as e:
        print(e)
    return render(request, "ansBlog.html")



def seeblog(request, pk):
    try:
        post = Blog.objects.get(pk=pk)
        blog = Blog.objects.filter(parent_blog=post)
        context = {"blog": blog}
    except Exception as e:
        print(e)
    return render(request, "seeblog.html", context)



class ProfileFollowToggee( LoginRequiredMixin , View):
    try:
        def post(self, request, pk, *args, **kwargs):
            user_to_toggle = request.POST.get('username')
            profile_ = Profile.objects.get(user__username__iexact=user_to_toggle)
            user = request.user
            if user in profile_.followers.all():
                profile_.followers.remove(user)
            else:
                profile_.followers.add(user)

            return redirect(f"/viewprofile/{pk}")
    except Exception as e:
        print(e)


def privacypolicy(request):
    return render(request, "privacypolicy.html")


def termcondition(request):
    return render(request, "termcondition.html")


def about_us(request):
    return render(request, "about_us.html")


def confirm_password(request):
    return render(request, "confirm_password.html")



def forget_password(request):
    return render(request, "password_reset.html")