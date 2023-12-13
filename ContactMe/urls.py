# urls.py
from django.urls import path
from .views import ContactListView, ContactDetailView, ContactCreateView, ContactUpdateView, ContactDeleteView

app_name = 'ContactMe'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('contact/create/', ContactCreateView.as_view(), name='contact_create'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('contact/update/<int:pk>/', ContactUpdateView.as_view(), name='contact_edit'),
    path('contact/delete/<int:pk>/', ContactDeleteView.as_view(), name='contact_confirm_delete'),
    # Add other URL patterns as needed
]
