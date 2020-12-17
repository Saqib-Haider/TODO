from django.shortcuts import render,HttpResponse,redirect
from .models import Task
from .forms import TaskForm,UpdateTaskForm
# Create your views here.
def task_list(request):
	queryset = Task.objects.order_by('complete_time','complete_time')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(title__icontains=query)
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
	'tasks':queryset,
	'form':form,
	}
	return render(request, 'tasklist.html', context)

def task_update(request, pk):
	queryset = Task.objects.get(id=pk)
	form = UpdateTaskForm(instance=queryset)
	if request.method == 'POST':
		form = UpdateTaskForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {
		'form':form
		}

	return render(request, 'updatetask.html', context)

def task_delete(request, pk):
	queryset = Task.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/')

	context = {
		'item':queryset
		}
	return render(request, 'deletetask.html', context)