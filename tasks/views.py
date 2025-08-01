from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Category
from .forms import TaskForm, CategoryForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)
    
    category_filter = request.GET.get('category')
    if category_filter:
        tasks = tasks.filter(category__id=category_filter)

    dashboard = {
        'total': tasks.count(),
        'completed': tasks.filter(completed=True).count(),
        'pending': tasks.filter(completed=False).count(),
    }

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'categories': categories,
        'dashboard': dashboard
    })

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# -------------------------------
# Category Views
# -------------------------------

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'tasks/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')  # ✅ Now points to category_list
    else:
        form = CategoryForm()
    return render(request, 'tasks/category_form.html', {'form': form})
