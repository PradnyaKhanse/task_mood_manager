import requests
from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tips = []
    mood = request.GET.get('mood', '').lower()

    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        mood = request.POST.get('mood', '').lower()
        deadline = request.POST.get('deadline')  # new line

        if title:
            Task.objects.create(title=title, mood=mood, deadline=deadline)
        return redirect(f'/?mood={mood}')

    if mood:
        try:
            resp = requests.post(
                'http://127.0.0.1:5001/api/tips',
                json={'mood': mood},
                timeout=3
            )
            if resp.ok:
                tips = resp.json().get('tips', [])
        except requests.RequestException:
            tips = ['Could not retrieve tips.']

    tasks = Task.objects.all().order_by('-id')
    return render(request, 'core/task_list.html', {
        'tasks': tasks,
        'tips': tips,
        'mood': mood
    })

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
