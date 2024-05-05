from django.contrib import admin

from .models import Commission, Job, JobApplication


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication


class JobApplicationInline(admin.TabularInline):
    model = JobApplication


class JobAdmin(admin.ModelAdmin):
    model = Job
    search_fields = ("role",)
    inlines = [JobApplicationInline]


class JobInline(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    search_fields = ("title",)
    inlines = [JobInline]


admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Commission, CommissionAdmin)
