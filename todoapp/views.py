from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm,UpdateTaskForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .filters import TaskFilter




# Create your views here.
def task_list(request):
	searchfilter = TaskFilter(request.GET)
	task = searchfilter.qs
	queryset = task.order_by('-create_time', 'complete_time')

	completed_tasks = task.filter(status="True").count()
	total_tasks = task.count()
	#percentage = completed_tasks / total_tasks * 100
	if total_tasks != 0:
		percentage = completed_tasks / total_tasks * 100
	else:
		percentage = 0
	paginator = Paginator(queryset, 20)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
	"tasks":queryset,
	"form":form,
	"page_request_var": page_request_var,
	"searchfilter" : searchfilter,
	"completed_tasks": completed_tasks,
	"total_tasks" : total_tasks,
	"percentage" : percentage,
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
		"form":form,
		"title": queryset.title,
		}

	return render(request, 'updatetask.html', context)

def task_delete(request, pk):
	queryset = Task.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/')

	context = {
		"item":queryset,
		"title": queryset.title,
		}
	return render(request, 'deletetask.html', context)