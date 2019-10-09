from django.db import models


class JobOffer(models.Model):
    company_name = models.CharField(max_length=60)
    company_email = models.EmailField(max_length=60)
    job_title = models.CharField(max_length=60)
    job_description = models.TextField(max_length=250)
    salary = models.IntegerField()
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.job_title} - {self.salary}€'
