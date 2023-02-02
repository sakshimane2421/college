from django.db import models

# Create your models here.

class Student(models.Model):
	id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	mobile_number=models.CharField(max_length=15)
	address=models.TextField()
	roll_number=models.IntegerField()


	def __str__(self):
        	return self.name

class Course(models.Model):
	name = models.CharField(max_length=255)
	course_code = models.CharField(max_length=255)
	start_year = models.IntegerField()
	intake = models.IntegerField()
	duration = models.IntegerField()

		
	def __str__(self):
    		return self.name



class Department(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
    		return self.name

# one to many relatonship
class Laboratory(models.Model):
	department_id = models.ForeignKey (Department , on_delete=models.CASCADE)
	lab_name=models.CharField(max_length=255)

	def __str__(self):
			return self.lab_name

class Faculty(models.Model):
	department_id = models.ForeignKey(Department , on_delete=models.CASCADE)
	Name_of_Faculty = models.CharField(max_length=255)
	Designation = models.CharField(max_length=255)

	def __str__(self):
			return self.Name_of_Faculty


class Visiting_Faculty(models.Model):
	department_id = models.ForeignKey(Department , on_delete=models.CASCADE)
	Name_of_Faculty = models.CharField(max_length=255)
	Designation = models.CharField(max_length=255)

	def __str__(self):
			return self.Name_of_Faculty



class Facillities(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	
	def __str__(self):
			return self.name



class Contact(models.Model):
	name = models.CharField(max_length=255)
	mobile_number = models.IntegerField()
	email_address = models.EmailField()
	message = models.TextField()

	def __str__(self):
			return self.name