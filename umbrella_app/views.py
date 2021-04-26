from django.forms import widgets
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import BaseFormView, TemplateResponseMixin
from .forms import LocationForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "umbrella_app/index.html"


class LocationFormView(FormView, TemplateResponseMixin):
    template_name = "umbrella_app/index.html"
    form_class = LocationForm
    success_url = "umbrella"

    def get(self, request, *args, **kwargs):

        formView = FormView.get(self, request, *args, **kwargs)
        formData = formView.context_data["form"]
        print(formView.context_data["form"])
        unknown = formView.context_data["form"]
        object_methods = [
            method_name
            for method_name in dir(unknown)
            if callable(getattr(unknown, method_name))
        ]

        print(object_methods)
        # listView = BaseListView.get(self, request, *args, **kwargs)
        # UhrZeit = self.request.POST["Zeit"]
        # Ort = self.request.POST["Ort"]

        # formData = {"Zeit": UhrZeit, "Ort": Ort}
        # print(formData)
        # listData = listView.context_data['object_list']
        return render(request, self.template_name, {"formData": formData})

    # def form_valid(self, form):
    #     time = form.cleaned_data["Zeit"]
    #     print("form_valid---------------", self.request.POST)
    #     return super(LocationFormView, self).form_valid(form)

    # def get_context_data(self, form, **kwargs):
    #     time = form.cleaned_data["Zeit"]
    #     context = super(LocationFormView, self).get_context_data(form,**kwargs)
    #     print("getContext---------------", self.request.POST, time)
    #     # print(kwargs)
    #     return context
