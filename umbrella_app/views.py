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

        form_view = FormView.get(self, request, *args, **kwargs)
        form_data = form_view.context_data["form"]

        unknown = form_view.context_data["form"]
        object_methods = [
            method_name
            for method_name in dir(unknown)
            if callable(getattr(unknown, method_name))
        ]

        print(object_methods)
        # listView = BaseListView.get(self, request, *args, **kwargs)
        # Uhrat_what_time = self.request.POST["at_what_time"]
        # where_are_you = self.request.POST["where_are_you"]

        # formData = {"at_what_time": Uhrat_what_time, "where_are_you": where_are_you}
        # print(formData)
        # listData = listView.context_data['object_list']
        return render(request, self.template_name, {"form_data": form_data})

    # def form_valid(self, form):
    #     time = form.cleaned_data["at_what_time"]
    #     print("form_valid---------------", self.request.POST)
    #     return super(LocationFormView, self).form_valid(form)

    # def get_context_data(self, form, **kwargs):
    #     time = form.cleaned_data["at_what_time"]
    #     context = super(LocationFormView, self).get_context_data(form,**kwargs)
    #     print("getContext---------------", self.request.POST, time)
    #     # print(kwargs)
    #     return context
