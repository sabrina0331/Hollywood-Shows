from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Show
from .forms import ShowForm
# Create your views here.
def allshows(request):
    shows = Show.objects.all()
    context = {
        'shows' : shows
    }
    return render(request, 'shows/allshows.html',context)

def new_page(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shows:allshows'))
    else:
        form = ShowForm()
    context ={'form': form}
    return render(request,'shows/new_page.html',context)

def show_detail(request,show_id):
    this_show = Show.objects.get(id=show_id)
    context = { 'this_show': this_show }
    return render(request,'shows/show_detail.html', context)

def update_show(request,show_id):
    update_show = Show.objects.get(id=show_id)
    if request.method != 'POST':
        print("It's not a post request")
        form = ShowForm(instance=update_show)
    else:
        form=ShowForm(instance=update_show,data=request.POST)
        print('It is a post request')
        if form.is_valid():
            form.save()
            print('form saved')
            return HttpResponseRedirect(reverse('shows:show_detail', args=[update_show.id]))
    context = {'update_show': update_show, 'form':form}
    return render(request,'shows/update_show.html',context)

def delete_show(request,delete_id):
    delete_this = Show.objects.get(id=delete_id)
    delete_this.delete()
    return redirect('shows:allshows')

def search_show(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        print('pressed search')
        searched_show = Show.objects.filter(title__contains=searched)
        return render(request,'shows/search_show.html', 
            {'searched': searched, 'searched_show':searched_show})
    else:
        print('get a get request')
        return redirect(request,'shows/allshows.hmtl')
