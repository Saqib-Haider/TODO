from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Task
from .forms import TaskForm,UpdateTaskForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .filters import TaskFilter
from django.views.generic import UpdateView, DeleteView, ListView
from .serializers import TaskSerializer
from rest_framework import generics
from django.views.generic.edit import FormMixin




# Create your views here.
class TaskListApi(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class TaskDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

class TaskUpdateView(UpdateView):
    template_name = 'updatetask.html'
    form_class = UpdateTaskForm
    queryset = Task.objects.all()

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("id")
        instance = get_object_or_404(Task, id=id)
        return instance

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/')

class TaskDeleteView(DeleteView):
    template_name = 'deletetask.html'

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get("id")
        return get_object_or_404(Task, id=id)
    def get_success_url(self):
        return reverse('task_list')


class TaskListView(FormMixin,ListView):
	template_name = 'tasklist.html'
	form_class = TaskForm
	model = Task
	#paginate_by = 10
	context_object_name = 'tasks'
	queryset = Task.objects.all().order_by('-create_time', 'complete_time')


	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		context['searchfilter']= TaskFilter(self.request.GET, queryset=self.get_queryset())
		context['completed_tasks'] = Task.objects.filter(status=True).count()
		context['total_tasks'] = Task.objects.all().count()
		context['percentage'] = context['completed_tasks'] / context['total_tasks'] * 100
		return context

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
		return super().form_valid(form)
	success_url = ('/')

	def get_queryset(self):
		qs = self.model.objects.all()
		searchfilter= TaskFilter(self.request.GET, queryset=qs)
		return searchfilter.qs





def task_list(request):
	searchfilter = TaskFilter(request.GET)
	task = searchfilter.qs
	queryset = task.order_by('-create_time', 'complete_time')

	completed_tasks = task.filter(status=True).count()
	total_tasks = task.count()
	if total_tasks != 0:
		percentage = completed_tasks / total_tasks * 100
	else:
		percentage = 0
	paginator = Paginator(queryset, 10)
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