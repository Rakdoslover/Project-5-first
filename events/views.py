from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Event
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
