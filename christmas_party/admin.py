from django.contrib import admin

from christmas_party.models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "company",
        "contact_number",
        "coupon",
        "create_timestamp",
    ]


admin.site.register(Attendance, AttendanceAdmin)
