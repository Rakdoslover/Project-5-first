from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Workout_Session
from .forms import WorkoutSessionForm


def our_sessions(request):
    """ A view to return the our sessions page """

    our_sessions = Workout_Session.objects.all()
    context = {
        'our_sessions': our_sessions
    }

    return render(request, 'workouts/our_sessions.html', context)


def session_detail(request, workout_session_id):
    """ A view to show individual session details """

    workout_session = get_object_or_404(
        Workout_Session, pk=workout_session_id)

    context = {
        'workout_session': workout_session
    }

    return render(request, 'workouts/session_detail.html', context)


@login_required
def add_session(request):
    """ Add a session to sessions page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST, request.FILES)
        if form.is_valid():
            session = form.save()
            messages.success(request, 'Successfully added session!')
            return redirect(reverse('session_detail', args=[session.id]))
        else:
            messages.error(
                request, 'Failed to add session.'
                'Please ensure the form is valid.'
            )
    else:
        form = WorkoutSessionForm()

    template = 'workouts/add_session.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_session(request, session_id):
    """ Edit a session in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    session = get_object_or_404(Workout_Session, pk=session_id)
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST, request.FILES, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated session!')
            return redirect(reverse('session_detail', args=[session.id]))
        else:
            messages.error(
                request, 'Failed to update session.'
                'Please ensure the form is valid.'
                )
    else:
        form = WorkoutSessionForm(instance=session)
        messages.info(request, f'You are editing {session.name}')

    template = 'workouts/edit_session.html'
    context = {
        'form': form,
        'session': session,
    }

    return render(request, template, context)


@login_required
def delete_session(request, session_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    session = get_object_or_404(Workout_Session, pk=session_id)
    product.delete()
    messages.success(request, 'Session deleted!')
    return redirect(reverse('our_sessions'))
