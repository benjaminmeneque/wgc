from django.urls import path

from christmas_party.views import AttendanceCreateView, SuccessView

urlpatterns = [
    path("", AttendanceCreateView.as_view(), name="attendance-create"),
    path(
        "success/<str:coupon_code>/", SuccessView.as_view(), name="attendance-success"
    ),
]
