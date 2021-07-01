from .models import Activity
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class ActivityUpdate(UpdateView):

    model = Activity
    template_name = 'activities/activity_edit_form.html'
    pk_url_kwarg = 'activity_pk'
    fields = '__all__'
    success_url = reverse_lazy('activities')


class ActivityDelete(DeleteView):

    model = Activity
    template_name = 'activities/activity_confirm_delete.html'
    pk_url_kwarg = 'activity_pk'
    success_url = reverse_lazy('activities')
