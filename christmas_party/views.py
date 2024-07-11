from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from christmas_party.models import Attendance


def generate_coupon_code():
    last_coupon = Attendance.objects.order_by("id").last()
    if not last_coupon:
        return "WGC-1"
    last_code = last_coupon.coupon
    number = int(last_code.split("-")[1]) + 1
    return f"WGC-{number}"


class AttendanceCreateView(CreateView):
    model = Attendance
    fields = ["full_name", "company", "contact_number"]

    def post(self, request, *args, **kwargs):
        full_name = request.POST.get("full_name")
        company = request.POST.get("company")
        contact_number = request.POST.get("contact_number")

        coupon_code = generate_coupon_code()

        # Create Attendance instance and save it
        attendance_instance = Attendance.objects.create(
            full_name=full_name,
            company=company,
            contact_number=contact_number,
            coupon=coupon_code,
        )

        # Redirect to success page with coupon code
        return redirect("attendance-success", coupon_code=coupon_code)


class SuccessView(TemplateView):
    template_name = "christmas_party/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coupon_code"] = kwargs.get("coupon_code")
        return context


# TODO create a modelform for attendance model
# TODO save the data in google sheets
# TODO fix the validations
