from .models import Activity
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy


class ActivityLIst(ListView):

    model = Activity
    template_name = 'activities/activity_list.html'
    paginate_by = 10
