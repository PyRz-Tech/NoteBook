from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import TextForm
from .models import Text
from asgiref.sync import async_to_sync
from core.utils.analyze_sentiment import analyze_setinment
from django.utils import timezone
# Create your views here.


def begin(request):
    return render(request, 'begin.html')

@login_required(login_url='begin/')
def dashboard(request):
    entries = Text.objects.filter(user=request.user).order_by('date')

    labels = []
    values = []
    last_value = 0

    for entry in entries:       
        date_str = entry.date.strftime('%b %d, %H:%M')
        labels.append(date_str)
        if entry.sentiment == 'POSITIVE':
            value = entry.sentiment_score or 0
        elif entry.sentiment == 'NEGATIVE':
            value = -(entry.sentiment_score or 0)
        else:
            value = 0

        values.append(round(value, 2))
        last_value = round(value, 2)

    if not labels:
        now = timezone.now().strftime('%b %d, %H:%M')
        labels = [now]
        values = [0]
        last_value = 0

    context = {
        'labels': labels,      
        'values': values,
        'last_value': last_value,
    }

    return render(request, 'dashboard.html', context)

@login_required(login_url='begin/')
def logout_view(request):
    logout(request)
    return redirect('core:begin')

@login_required(login_url='begin/')
def note_detail(request, pk):
    text = get_object_or_404(Text, pk=pk)
    return render(request, 'note.html', {'entry':text})

@login_required(login_url='begin/')
def capture_vibe(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            entry = Text.objects.create(
                user=request.user,
                text=form.cleaned_data['text']
            )
            label, score = async_to_sync(analyze_setinment)(form.cleaned_data['text'])
            
            entry.sentiment = label
            entry.sentiment_score = score
            entry.save()

            return redirect('core:dashboard')
    else:
        form = TextForm()

    return render(request, 'capture_vibe.html', {'form':form})

@login_required(login_url='begin/')
def notes(request):
    texts = Text.objects.filter(user=request.user)
    return render(request, 'latest_vibes.html', {'entries':texts})
