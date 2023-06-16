from django.shortcuts import render
from fuel.models import Fuel
# from _decimal import Decimal
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView,\
    DeleteView
from fuel.forms import SearchForm, FuelForm
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class FuelListView(FormView):
    template_name = "fuel/fuel_list.html"
    form_class = SearchForm
    success_url = "."

    def get_context_data(self, **kwargs):
        print(self.request.user)
        return {
            "fuels": Fuel.objects.filter(),
            "form": self.form_class()}

    def form_valid(self, form):
        filter_ = Q()
        if form.cleaned_data["fraze"] != "":
            filter_ |= Q(
                Q(title__icontains=form.cleaned_data["fraze"])
                |Q(description__icontains=form.cleaned_data["fraze"]))

        fuels = Fuel.objects.filter(filter_).order_by("-date_from", )
        return render(
            request=self.request,
            template_name=self.template_name,
            context={
                "form": form,
                "fuels": fuels})

    def form_invalid(self, form):
        return render(
            request=self.request,
            template_name=self.template_name,
            context={
                "form": form,
                "fuels": Fuel.objects.filter()})


class FuelDetailsView(TemplateView):
    template_name = "fuel/fuel_details.html"

    def get_context_data(self, **kwargs):
        fuel_id = self.kwargs.get("pk", None)
        return {"fuel": Fuel.objects.get(pk=fuel_id)}


class FuelCreateView(
        LoginRequiredMixin,
        CreateView):
    model = Fuel
    form_class = FuelForm
    template_name = "fuel/fuel_update.html"
    success_url = reverse_lazy("fuel-list")


class FuelUpdateView(
        LoginRequiredMixin,
        UpdateView):
    model = Fuel
    form_class = FuelForm
    template_name = "fuel/fuel_update.html"
    success_url = reverse_lazy("fuel-list")

class FuelDeleteView(
        LoginRequiredMixin,
        DeleteView):
    model = Fuel
    template_name = "fuel/fuel_delete.html"
    success_url = reverse_lazy("fuel-list")


def fuel_list(request):
    fuels = Fuel.objects.filter().order_by("-date_from", )
    print(fuels.query)
    return render(request=request,
                  template_name="fuel_list.html",
                  context={"fuels": fuels})
    
