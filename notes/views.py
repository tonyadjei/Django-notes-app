from django.shortcuts import render, redirect
from .models import Note
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms



@login_required(login_url="/accounts/login/")
def note_list(request):
    # only show notes of logged in user
    notes = Note.objects.filter(author__exact=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, slug):
    # get note with slug
    note = Note.objects.get(slug=slug)
    return render(request, 'notes/note_detail.html', {'note': note})


@login_required(login_url="/accounts/login/")
def note_create(request):
    if request.method == 'POST':
        form = forms.CreateNote(request.POST, request.FILES)
        if form.is_valid():
            # save note to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('notes:list')
    else:
        form = forms.CreateNote()
    return render(request, 'notes/note_create.html', {'form': form})
