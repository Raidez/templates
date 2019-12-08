from django.db import models

class Task(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name = "task"
		verbose_name_plural = "tasks"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("task_detail", kwargs={"pk": self.pk})
