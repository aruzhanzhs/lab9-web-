from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=False)
    city = models.CharField(max_length=200)
    address = models.TextField(null=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=False)
    salary = models.FloatField(null=False)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='vacancy')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }

