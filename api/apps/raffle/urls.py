# from django.urls import path
# from .views import (
#     RaffleListView,
#     RaffleCreateView,
#     RaffleDeleteView,
#     RaffleDetailView,
#     RaffleUpdateView
# )
#
# urlpatterns = [
#     path('create', RaffleCreateView.as_view(), name='create-raffle'),
#     path('<int:id>', RaffleDetailView.as_view(), name='view-raffle-detail'),
#     path('list', RaffleListView.as_view(), name='view-raffle-list'),
#     path('<int:id>/update', RaffleUpdateView.as_view(), name='update-raffle'),
#     path('<int:id>/delete', RaffleDeleteView.as_view(), name='delete-raffle'),
# ]