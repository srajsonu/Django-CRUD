from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView, DeleteView

from autos.forms import MakeForm
from cats.models import *

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.all().count()
        cl = Cat.objects.all()

        ctx = {'breed_count': bc, 'cat_list': cl}
        return render(request, 'cats/cat_list.html', ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()

        ctx = {'breed_list': bl}
        return render(request, 'cats/breed_list.html', ctx)


class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request):
        form = MakeForm()
        ctx = {'form': form}

        return render(request, self.template, ctx)

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)

class BreedUpate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_form.html'

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=breed)
        ctx = {'form': form}

        return render(request, self.template, ctx)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=breed)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_confirm_delete.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {'make': make}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
