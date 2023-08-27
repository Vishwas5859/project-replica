import json
class admin_panel:
    def __init__(self):
        self.module_details = {}
        self.trainer_details = {}
        self.batch_details = {}
        self.student_details = {}
        self.count = 0
    
    
    def admin_login(self,username, password):
        if username == "Admin" and password == "Admin":
            return True
        else:
            return False

    def add_module(self):
        self.count = self.count+1
        module_name = input("Enter module name: ")
        module_duration = input("Enter module durayion: ")
        topic_list = []
        topic_size = int(input("Enter topic size: "))
        for i in range(1,topic_size+1):
            topic = input(f"Enter topic {i} name")
            topic_list.append(topic)
        module_items = {"module_name":module_name,"duration":module_duration,"topic":topic_list} 
        self.module_details[self.count] = module_items
        with open("add_module.json","w") as f:
            json.dump(self.module_details,f,indent = 4)
        return self.module_details 
    
    def read_module_details(self):
        with open("add_module.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print (f" Module_id: {k} || Modules_details {v}")  
            print("*"*100)   


    def add_trainer(self):
        self.count = self.count+1
        trainer_name = input("Enter tariner name: ")
        trainer_gender = input("Enter trainer gender: ")
        qualification = input("Enter qualification: ")
        experience = input("Enter experience: ")
        mob = input("Enter mob No. : ")
        email = input("Enter email id: ")
        password = input("Enter the password: ")
        
        traniner_data = {"trainer name": trainer_name,"gender":trainer_gender,"qualification":qualification, "experience":experience, "mob No":mob, "password":password, "email_id":email}
        self.trainer_details[self.count] = traniner_data
        with open("add_trainer.json","w") as f:
            json.dump(self.trainer_details,f,indent = 4)
        return self.trainer_details
    

    def add_batch(self):
        self.count = self.count+1
        module_name = input("Enter module name: ")
        trainer_name = input("Enter trainer name: ")
        student_data = input("enter student data: ")
        batch_data = {"module_name":module_name,"trainer_name":trainer_name,"student_data":student_data}
        self.batch_details[self.count] = batch_data
        with open("add_batch.json","w") as f:
            json.dump(self.batch_details,f,indent = 4)
        return self.batch_details
    

    def read_trainer_details(self,trainer_json):
        with open("add_trainer.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print (f" trainer_id: {k} || trainer_details {v}")  
            print("*"*100)  


    def add_student(self):
        self.count = self.count+1
        student_size = int(input("Enter the student: "))
        student_list = []
        for i in range(1, student_size+1):
            print(f"Enter the details of student {i} :")    
            name = input(f"Enter the name of student {i} :")
            gender = input(f"Enter the gender of student {i} :")    
            qualification = input(f"Enter the qualification of student {i} :")
            age = input(f"Enter the age of student {i} :")
            experience = input(f"Enter the experience of student {i} :")
            mob = input(f"Enter the mob.no of student {i} :")
            password = input(f"Enter the password of student {i} :")
            student_data = {"name":name, "gender": gender,"qualification": qualification,"age":age,"experience":experience,"mon.no":mob,"password":password}
            student_list.append(student_data)
        self.student_details[self.count] = student_list
        with open("add_student.json","w") as f:
            json.dump(self.student_details,f,indent = 4)
        return self.student_details
    

    def read_student_details(self):
        with open("add_student.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print (f" Batch_id: {k} || Batch_students {v}")  
            print("*"*100)  

    def upadate_trainer_details(self):
        with open("add_trainer.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print (f" trainer_id: {k} || trainer_details {v}")  
            print("*"*100)
        
        id = input("Enter trainer id which you want to update: ")
        field = input("Enter the filed you want to update: ") 
        updated_value = input("Enter the updated value: ")
        data[id][field] = updated_value 
        with open("add_trainer.json","w") as f:
            json.dump(data,f,indent = 4)
        return data


    def remove_module(self):
        with open("add_module.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Module_ID : {k} || Module_details : {v}")
            print("*"*100)
        id = input("Enter module no. which you want to del: ")
        del data[id]
        return data    

    





x = admin_panel()
#print(x.admin_login("Admin","Admin"))
# print(x.add_module())
# print(x.add_module())   
# print(x.add_trainer())
t = "trainer.json"
(x.read_trainer_details(t))  
#print(x.add_student()) 
#print(x.read_student_details())
# print(x.upadate_trainer_details())



