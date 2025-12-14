from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .models import Contact, Story, ClimateNews, Research, Event

import random  

# ---------------- PUBLIC PAGES ----------------

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def research(request):
    return render(request,'research.html')

def news(request):
    return render(request,'news.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
    return render(request, 'contact.html')

def stories(request):
    return render(request, 'stories.html')

def innovation(request):
    return render(request, 'innovation.html')

def info(request):
    return render(request, 'info.html')

def latestresearch(request):
    return render(request, 'latestresearch.html')

def morestories(request):
    return render(request, 'morestories.html')


# ---------------- AUTH ----------------

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("admin_dashboard")
            else:
                return redirect("user_dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "register.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already taken"})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  # auto-login after registration
        return redirect("user_dashboard")

    return render(request, "register.html")


# ---------------- DASHBOARDS ----------------

@login_required
def user_dashboard(request):
    tips = [
        "Planting trees helps absorb carbon dioxide and cools the environment.",
        "Switching to renewable energy reduces greenhouse gas emissions.",
        "Reducing meat consumption lowers methane emissions from livestock.",
        "Walking or cycling instead of driving cuts down on fossil fuel use.",
        "Conserving water also saves energy used in water treatment.",
        "Recycling reduces waste and saves natural resources.",
        "Solar panels can power homes sustainably and reduce electricity bills.",
        "Supporting local farmers reduces food miles and emissions.",
        "Energy-efficient appliances lower household carbon footprints.",
        "Community clean-up drives help reduce pollution and raise awareness."
    ]
    fact = random.choice(tips)
    return render(request, "user_dashboard.html", {"fact": fact})


def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    context = {
        "total_users": User.objects.count(),
        "total_stories": Story.objects.count(),
        "total_tips": ClimateNews.objects.count(),
        "total_events": Event.objects.count(),
    }
    return render(request, "admin_dashboard.html", context)


# ---------------- ADMIN CRUD ----------------
''''''
@user_passes_test(is_admin)
def manage_news(request):
    if request.method == "POST":
        text = request.POST.get("text")
        ClimateNews.objects.create(user=request.user, text=text, approved=True)
        return redirect("manage_news")
    news = ClimateNews.objects.all()
    return render(request, "manage_news.html", {"news": news})
''''''

@login_required
def manage_news(request):
    if request.method == "POST":
        text = request.POST.get("text")
        ClimateNews.objects.create(
            user=request.user,
            text=text,
            approved=False
        )
    news = ClimateNews.objects.all()
    return render(request, "manage_news.html", {"news": news})




@user_passes_test(is_admin)
def edit_news(request, news_id):
    news = get_object_or_404(ClimateNews, id=news_id)
    if request.method == "POST":
        news.text = request.POST.get("text")
        news.approved = request.POST.get("approved") == "on"
        news.save()
        return redirect("manage_news")
    return render(request, "edit_news.html", {"news": news})

@user_passes_test(is_admin)
def delete_news(request, news_id):
    news = get_object_or_404(ClimateNews, id=news_id)
    news.delete()
    return redirect("manage_news")


@user_passes_test(is_admin)
def manage_stories(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Story.objects.create(user=request.user, title=title, content=content, approved=True)
        return redirect("manage_stories")
    stories = Story.objects.all()
    return render(request, "manage_stories.html", {"stories": stories})

@user_passes_test(is_admin)
def edit_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.method == "POST":
        story.title = request.POST.get("title")
        story.content = request.POST.get("content")
        story.approved = request.POST.get("approved") == "on"
        story.save()
        return redirect("manage_stories")
    return render(request, "edit_story.html", {"story": story})

@user_passes_test(is_admin)
def delete_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    story.delete()
    return redirect("manage_stories")


@user_passes_test(is_admin)
def manage_research(request):
    if request.method == "POST":
        title = request.POST.get("title")
        summary = request.POST.get("summary")
        link = request.POST.get("link")
        Research.objects.create(title=title, summary=summary, link=link, added_by=request.user)
        return redirect("manage_research")
    research = Research.objects.all()
    return render(request, "manage_research.html", {"research": research})

@user_passes_test(is_admin)
def edit_research(request, research_id):
    research = get_object_or_404(Research, id=research_id)
    if request.method == "POST":
        research.title = request.POST.get("title")
        research.summary = request.POST.get("summary")
        research.link = request.POST.get("link")
        research.save()
        return redirect("manage_research")
    return render(request, "edit_research.html", {"research": research})

@user_passes_test(is_admin)
def delete_research(request, research_id):
    research = get_object_or_404(Research, id=research_id)
    research.delete()
    return redirect("manage_research")


@user_passes_test(is_admin)
def manage_events(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        location = request.POST.get("location")
        date = request.POST.get("date")
        Event.objects.create(title=title, description=description, location=location, date=date, created_by=request.user)
        return redirect("manage_events")
    events = Event.objects.all()
    return render(request, "manage_events.html", {"events": events})

@user_passes_test(is_admin)
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event.title = request.POST.get("title")
        event.description = request.POST.get("description")
        event.location = request.POST.get("location")
        event.date = request.POST.get("date")
        event.save()
        return redirect("manage_events")
    return render(request, "edit_event.html", {"event": event})

@user_passes_test(is_admin)
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect("manage_events")


def morestories(request):
    # Fetch only approved stories
    stories = Story.objects.filter(approved=True).order_by('-id')
    return render(request, "morestories.html", {"stories": stories})

def latestresearch(request):
    # Fetch all research articles (or filter approved if you add that field later)
    research = Research.objects.all().order_by('-created_at')
    return render(request, "latestresearch.html", {"research": research})


def events(request):
    # Fetch all research articles (or filter approved if you add that field later)
    research = Event.objects.all().order_by('-created_at')
    return render(request, "events.html", {"events": events})



