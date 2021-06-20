from django.shortcuts import render
from .models import Opportunity
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy


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


class OpportunityDelete(DeleteView):

    model = Opportunity


class OpportunityForm(FormView):

    model = Opportunity


