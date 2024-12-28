from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from apps.posts.models import Post
from apps.posts.models import Comment
from django.contrib import messages
from django.http import JsonResponse

User = get_user_model()


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "accounts/accounts.html")


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password"})
    return render(request, "accounts/login.html")


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone_number = request.POST["phone_number"]
        email = request.POST["email"]

        if User.objects.filter(username=username).exists():
            return render(request, "accounts/register.html",
                          {"error": "Username already exists"})

        try:
            user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                            last_name=last_name, phone_number=phone_number, email=email)
            login(request, user)
            return redirect("home")
        except Exception as e:
            return render(request, "accounts/register.html",
                          {"error": "Registration failed"})

    return render(request, "accounts/register.html")


def profile(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=user_id)
    user_posts = Post.objects.filter(publisher=user).order_by('-created_at')
    return render(request, "accounts/accounts.html", {
        "user": user,
        "posts": user_posts
    })


def addpost(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        media_url = request.POST.get("media_url")
        caption = request.POST.get("caption")
        media_type = request.POST.get("media_type")
        category = request.POST.get("category")
        Post.objects.create(media_url=media_url, caption=caption,
                            publisher=request.user, media_type=media_type)
        return redirect("feed")
    return render(request, "accounts/addpost.html")


def feed(request):
    if not request.user.is_authenticated:
        return redirect('login')

    following_users = list(request.user.following.all())
    following_users.append(request.user)
    posts = Post.objects.filter(publisher__in=following_users).order_by(
        '-created_at').select_related('publisher')
    return render(request, "accounts/feed.html", {"posts": posts})


def add_comment(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        text = request.POST.get("text")
        if text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text
            )
            post.comments_count += 1
            post.save()

            return redirect("feed")

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request'
    }, status=400)


def toggle_like(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        post.likes_count -= 1
    else:
        post.likes.add(request.user)
        post.likes_count += 1
    post.save()
    return JsonResponse({
        'likes_count': post.likes_count,
        'is_liked': request.user in post.likes.all()
    })


def update_profile_picture(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        profile_picture = request.POST.get("profile_picture")
        request.user.profile_picture = profile_picture
        request.user.save()
        return redirect("profile", request.user.id)
    return redirect("profile", request.user.id)


def friends(request):
    if not request.user.is_authenticated:
        return redirect('login')
    users = User.objects.exclude(id=request.user.id)
    users_data = [
        {
            'user': user,
            'is_following': request.user in user.followers.all()
        }
        for user in users
    ]
    return render(request, "accounts/friends.html", {"users": users_data})


def followUser(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user.is_authenticated:
        if request.user != user_to_follow:
            if request.user in user_to_follow.followers.all():
                user_to_follow.followers.remove(request.user)
                request.user.following.remove(user_to_follow)
            else:
                user_to_follow.followers.add(request.user)
                request.user.following.add(user_to_follow)
            user_to_follow.save()
            request.user.save()
    return redirect('profile', user_id=user_id)


def user_logout(request):
    logout(request)
    return redirect("home")
