
student_list = []


class student:
	#constructor 
	def __init__(self,name):
		self.name = name
		student_list.append(self)


	def print_data(self):
		return self.name

class ex_student(student):

	def print_old(self):
		original = super().print_data()
		return original + " is old student"

	def print_data(self):
		return self.name.capitalize() + " Polymorphed"


instance_class = student("vinoth")

old_student = ex_student("mark")

print(instance_class.print_data())
print(old_student.print_old())
print(old_student.print_data())