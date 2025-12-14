from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('stories/', views.stories, name='stories'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('research/', views.research, name='research'),
    path('events/', views.events, name='events'),
    
    path('morestories/', views.morestories, name='morestories'),
    path('info/', views.info, name='info'),
    path('latestresearch/', views.latestresearch, name='latestresearch'),
    path('innovation/', views.innovation, name='innovation'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    # Dashboards
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Admin content management
    path('manage_news/', views.manage_news, name='manage_news'),
    path('manage_news/edit/<int:news_id>/', views.edit_news, name='edit_news'),
    path('manage_news/delete/<int:news_id>/', views.delete_news, name='delete_news'),

    path('manage_stories/', views.manage_stories, name='manage_stories'),
    path('manage_stories/edit/<int:story_id>/', views.edit_story, name='edit_story'),
    path('manage_stories/delete/<int:story_id>/', views.delete_story, name='delete_story'),

    path('manage_research/', views.manage_research, name='manage_research'),
    path('manage_research/edit/<int:research_id>/', views.edit_research, name='edit_research'),
    path('manage_research/delete/<int:research_id>/', views.delete_research, name='delete_research'),

    path('manage_events/', views.manage_events, name='manage_events'),
    path('manage_events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('manage_events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
