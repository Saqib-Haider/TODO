import django_filters
from django_filters import DateTimeFilter


from . models import Task

class TaskFilter(django_filters.FilterSet):
	#create_time = DateTimeFilter(field_name="create_time")
	complete_time = DateTimeFilter(field_name="complete_time")


	class Meta:
		model = Task
		fields = ['title']