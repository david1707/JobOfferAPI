from django.urls import path

from jobs.api.views import JobOfferListCreateAPIView, JobOfferListDetailAPIView

urlpatterns = [
    path('jobs/', JobOfferListCreateAPIView.as_view(), name="job-offer-list"),
    path('jobs/<int:pk>/', JobOfferListDetailAPIView.as_view(), name="job-offer-detail")
]
