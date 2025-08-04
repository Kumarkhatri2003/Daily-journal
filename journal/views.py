from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm  


# Create your views here.
@login_required
def entry_list(request):
     entries = Entry.objects.filter(user=request.user).order_by('-created_at')
     return render(request,'journal/entry_list.html',{'entries': entries})


@login_required
def entry_detail(request, pk): #pk->Primary key
     entry = get_object_or_404(Entry,pk=pk,user=request.user)
     return render (request,'journal/entry_details.html',{'entry': entry})


@login_required
def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = request.user
            new_entry.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'journal/entry_form.html', {'form': form})


@login_required
def entry_edit(request,pk):
    entry = get_object_or_404(Entry,pk=pk,user=request.user)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=entry.pk)
    
    else:
        form = EntryForm(instance=entry)
        return render(request,'journal/entry_form.html',{'form':form})
  
    
@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'journal/entry_confirm_delete.html', {'entry': entry})


               