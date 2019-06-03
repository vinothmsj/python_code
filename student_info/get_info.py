import sys
import ast
student = []
id =0

def check_db_for_id(local_id, op_flag):
    flag = 0
    i = 0
    for data in student:
        if(int(data['id']) == local_id):
               	if(op_flag == 1):
               		score = input("Enter the score to be updated")
               		data['score'] = score
               		flag = 1
               		print("Record Updated successfully")
               		break
               	elif(op_flag == 2):
               		del student[i]
               		flag =1
               		print("Record Deleted ")
        i = i + 1
        print(i)

    if(flag == 0):
        print("Invalid Id")
 
def update_global_id(update_id):
	global id
	id = update_id

def update_file(db_id):
	try:
		db_file = open("student_info_data" , "a")
		for data in student:
			if (data['id'] == db_id):
				db_file.write(str(data) + "\n")
		db_file.close()
	except FileNotFoundError as error:
		print(error) 


def update_info(name, score):
	global	id
	id = id + 1
	student_dict = {"name":name, "score":score , "id" : id}
	student.append(student_dict)
	update_global_id(student_dict['id'])
	update_file(id)

def get_user_info():
	global id
	print("Enter operation to perform \n"
	      "1. Add a Student \n"
	      "2. Delete a Student record \n"
	      "3. Update a student record \n"
	      "4. View Student Info\n"	
	      "5. Exit\n")
	try:	
		operation = int(input())
	except:
		print("Enter a Valid option");
		get_user_info()
	if(operation < 1 or operation > 5):
		sys.exit('Invalid Input.Exiting.')
	if(operation == 4):
		print_student_info()
	elif(operation == 1):
		name = input("Enter the student Name : ")
		if not name :
			print("Empty names not allowed")
			return
		score = input("Enter the student score : ")
		if not score:
			print("Score cannot be empty")
			return
		update_info(name , score)
	elif(operation == 3):
		local_id = input("Enter the Id of record to be updated : ")
		check_db_for_id(int(local_id) , 1)
	elif(operation == 2):
		local_id = input("Enter the Id of record to be Deleted : ")
		check_db_for_id(int(local_id) , 2)

	elif(operation == 5):
		sys.exit("Exiting!!")
	
def print_student_info():
	print("Student record Info \n")
	print("Id \t\t Name \t\t Score \n")
	for entry in student:
		print(str(entry['id']) + "\t\t" + entry['name'] + "\t\t" + entry['score'])


#Update the User info into the Local Db from the file.
def program_int():
	try:
		db_file = open("student_info_data" , "r")
		for info in db_file.readlines():
			data = ast.literal_eval(info)
			student_dict = data
			student.append(student_dict)
			update_global_id(student_dict['id'])
		db_file.close()
	except FileNotFoundError as error:
		print(error)


#This is to init the db at the startup
program_int()

	
#Get and process the user input
while(True):
	get_user_info()


#Funtion to print the user Info
print_student_info()

