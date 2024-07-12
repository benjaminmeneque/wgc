from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from christmas_party.forms import AttendanceForm
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
    form_class = AttendanceForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        coupon_code = generate_coupon_code()
        self.object.coupon = coupon_code
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("attendance-success", kwargs={"coupon_code": self.object.coupon})


class SuccessView(TemplateView):
    template_name = "christmas_party/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coupon_code"] = self.kwargs.get("coupon_code")
        return context


# TODO save the data in google sheets(optional because we have a admin site)
# TODO fix the validations in contact number
# TODO make UI applicable to the christmas party theme
# TODO make the form more informative and more beautiful
