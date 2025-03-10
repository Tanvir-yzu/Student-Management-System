from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Student
from .forms import StudentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_message = "Student created successfully!"
    success_url = reverse_lazy('student-list')

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_message = "Student updated successfully!"
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')

    def delete(self, request, *args, **kwargs):  # Fixed parameter syntax
        response = super().delete(request, *args, **kwargs)
        messages.success(request, "Student deleted successfully!")
        return response

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'