from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .forms import CityForm
from .models import City



def show_city(request, pk=None):

    form = CityForm
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            form = CityForm()
    if pk:
        city = City.objects.filter(id=pk).first
        return render(request, 'cities/detail.html', context={'city': city,})

    list_cities = City.objects.all()
    lst = Paginator(list_cities, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    return render(request, 'cities/cities.html', context={'page_obj': page_obj, 'form': form})


class CityDetailView(DetailView):

    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):

    model = City
    form_class = CityForm
    template_name = 'cities/add.html'
    success_url = reverse_lazy('add')


class CityUpdateView(SuccessMessageMixin ,UpdateView):

    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city')
    success_message = "The city was update successfully"

class CityDeleteView(DeleteView):

    model = City

    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('city')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class CityListView(ListView):
    paginate_by = 10
    model = City
    template_name = 'cities/cities.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        form = CityForm
        context['form'] = form
        return context