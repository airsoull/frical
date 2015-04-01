from django.views.generic import ListView

from .models import Job


class JobsListView(ListView):
    model = Job

    def get_queryset(self):
        return Job.objects.visible()

jobs_list_view = JobsListView.as_view()