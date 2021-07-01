from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from .models import Opportunity


class OpportunityLIst(ListView):

    model = Opportunity
    template_name = 'opportunities/opportunity_list.html'
    paginate_by = 10


class OpportunityDetail(DetailView):

    model = Opportunity
    template_name = 'opportunities/opportunity_detail.html'
    pk_url_kwarg = 'opportunity_pk'


class OpportunityCreate(CreateView):

    model = Opportunity
    template_name = 'opportunities/opportunity_form.html'
    fields = '__all__'
    success_url = reverse_lazy('opportunities')


class OpportunityUpdate(UpdateView):
    model = Opportunity
    template_name = 'opportunities/opportunity_edit_form.html'
    pk_url_kwarg = 'opportunity_pk'
    fields = '__all__'
    success_url = reverse_lazy('opportunities')


class OpportunityDelete(DeleteView):

    model = Opportunity
    template_name = 'opportunities/opportunity_confirm_delete.html'
    pk_url_kwarg = 'opportunity_pk'
    success_url = reverse_lazy('opportunities')


class OpportunityForm(FormView):

    model = Opportunity


