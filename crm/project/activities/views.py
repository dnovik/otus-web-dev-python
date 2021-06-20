from .models import Activity
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy


class ActivityLIst(ListView):

    model = Activity
    template_name = 'activities/activity_list.html'
    paginate_by = 10


class ActivityDetail(DetailView):

    model = Activity
    template_name = 'activities/activity_detail.html'
    pk_url_kwarg = 'activity_pk'


class ActivityCreate(CreateView):

    model = Activity
    template_name = 'activities/activity_form.html'
    fields = '__all__'
    success_url = reverse_lazy('activities')
