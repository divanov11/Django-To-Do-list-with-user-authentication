from cProfile import label
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Task
from .forms import PositionForm

# Imports for translation
from django.utils.translation import gettext_lazy as _


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            Task(user = user, title = "ফজর আদায় করেছি").save()
            Task(user = user, title = "যুহুর আদায় করেছি").save()
            Task(user = user, title = "আসর আদায় করেছি").save()
            Task(user = user, title = "মাগরিব আদায় করেছি").save()
            Task(user = user, title = "ঈশা আদায় করেছি").save()
            Task(user = user, title = "১ পৃষ্ঠা অর্থসহ কুরআন পড়েছি").save()
            Task(user = user, title = "চোখের হিফাজত করেছি").save()
            Task(user = user, title = "গীবত করিনি").save()
            Task(user = user, title = "৫ টাকা দান করেছি").save()
            Task(user = user, title = "গান শুনিন").save()
            Task(user = user, title = "৫ মিনিট দুআ করেছি").save()
            Task(user = user, title = "বাবা-মার সাথে ভালো ব্যবহার করেছি").save()
            Task(user = user, title = "সঠিক সময়ে ঘুমিয়েছি ও সাহরি খেয়েছি").save()
            Task(user = user, title = "অর্ধপারা অর্থসহ কুরআন পড়েছি").save()
            Task(user = user, title = "তারাবীহ আদায় করেছি").save()
            Task(user = user, title = "সীরাত পড়েছি ১০ পৃষ্ঠা").save()
            Task(user = user, title = "নেট ব্যবহার অর্ধেক কমিয়েছি").save()
            Task(user = user, title = "তাহাজ্জুদ আদায় করেছি").save()
            Task(user = user, title = "সকাল-সন্ধার দোয়া পড়েছি").save()
            Task(user = user, title = "সীরাত পড়েছি ২০ পৃষ্ঠা").save()
            Task(user = user, title = "১ পারা অর্থসহ কুরআন পড়েছি").save()
            Task(user = user, title = "প্রয়োজন ছাড়া নেট ব্যবহার করিনি").save()
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        #context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
     model = Task
     context_object_name = 'task'
     template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8', 'day9', 'day10', 'day11', 'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19', 'day20', 'day21', 'day22', 'day23', 'day24', 'day25', 'day26', 'day27', 'day28', 'day29', 'day30']
    success_url = reverse_lazy('tasks')


# class DeleteView(LoginRequiredMixin, DeleteView):
#     model = Task
#     context_object_name = 'task'
#     success_url = reverse_lazy('tasks')
#     def get_queryset(self):
#         owner = self.request.user
#         return self.model.objects.filter(user=owner)

class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('tasks'))
