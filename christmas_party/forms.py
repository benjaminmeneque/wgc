from django.core.exceptions import ValidationError
from django.forms import ModelForm

from christmas_party.models import Attendance


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ["full_name", "company", "contact_number"]

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        try:
            existing_attendance = Attendance.objects.get(full_name__iexact=full_name)
            raise ValidationError(
                f"You are already been registered. Your coupon code is: {existing_attendance.coupon}"
            )
        except Attendance.DoesNotExist:
            # No duplicate found, return the cleaned full_name
            return full_name
