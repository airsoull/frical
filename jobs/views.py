from django.views.generic import ListView, DetailView

from .models import Job


class JobsListView(ListView):
    model = Job

    def get_queryset(self):
        return Job.objects.visible()

jobs_list_view = JobsListView.as_view()


class JobDetailView(DetailView):
    model = Job

    def get_queryset(self):
        return Job.objects.visible()

job_detail_view = JobDetailView.as_view()