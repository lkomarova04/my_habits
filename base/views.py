from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Habit
from .forms import PositionForm


def index(request):
    return render(request, 'base/index.html')

def login(request):
    return render(request, 'base/login.html')

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('habits')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('habits')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('habits')
        return super(RegisterPage, self).get(*args, **kwargs)


class HabitList(LoginRequiredMixin, ListView):
    model = Habit
    context_object_name = 'habits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habits'] = context['habits'].filter(user=self.request.user)
        context['count'] = context['habits'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['habits'] = context['habits'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class HabitDetail(LoginRequiredMixin, DetailView):
    model = Habit
    context_object_name = 'habit'
    template_name = 'base/habit.html'


class HabitCreate(LoginRequiredMixin, CreateView):
    model = Habit
    fields = ['title', 'complete','created_date','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun',  ]
    success_url = reverse_lazy('habits')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(HabitCreate, self).form_valid(form)


class HabitUpdate(LoginRequiredMixin, UpdateView):
    model = Habit
    fields = ['title', 'complete','created_date','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', ]
    success_url = reverse_lazy('habits')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    context_object_name = 'habit'
    success_url = reverse_lazy('habits')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class HabitReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_habit_order(positionList)

        return redirect(reverse_lazy('habits'))