from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('book/', views.ListBookView.as_view(), name='list-book') ,
    path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name='detail-book'),
    path('book/create/', views.CreateBookView.as_view(), name='create-book'),
    path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete-book'),
    path('book/<int:pk>/update/', views.UpdateBookView.as_view(), name='update-book'),
    path('book/<int:book_id>/review/', views.CreateReviewView.as_view(), name='review'),
    path('book/search/', views.SearchBook, name='search'),
    path('book/Narrow down/business/', views.Categorize_by_business, name='narrow-down-business'),
    path('book/Narrow down/science・Technology/', views.Categorize_by_science_and_Technology, name='narrow-down-science・Technology'),
    path('book/Narrow down/Humanities・ideas/', views.Categorize_by_Humanities_and_ideas, name='narrow-down-Humanities・ideas'),
    path('book/Narrow down/computer・IT/', views.Categorize_by_computer_and_IT, name='narrow-down-computer・IT'),
    
]


