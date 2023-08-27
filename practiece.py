
import json
class admin_panel:
    
    def __init__(self):
        self.module_details = {}
        self.trainer_details = {}
        self.student_details = {}
        self.count = 0 
        
    def admin_login(self,username,password):
        if username == 'admin' and password == 'admin':
            return True
        else:
            return False
        
    def add_module(self):
        self.count = self.count+1
        module_name = input("Enter the module name: ")
        module_duration = input("Enter the module duration: ")
        topic_size = int(input("Enter the topic size: "))
        topic_list = []
        for i in range(1,topic_size+1):
            topic = input(f"Enter the topic {i} name ")
            topic_list.append(topic)
        module_data = {"module name": module_name,"module duration":module_duration,"topic":topic_list}
        self.module_details[self.count] = module_data
        
        with open('add_modulenew.json','w') as f:
            json.dump(self.module_details,f,indent = 4)
        return self.module_details  
    
    def read_module_details(self):
        with open("add_modulenew.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Module_iD  {k} || Module_details {v}")
            return data    
    
    def add_trainer(self):
        self.count = self.count+1
        trainer_name = input("Enter trainer name: ")
        gender = input("enter trainer gender: ")
        qualification = input("Enter trainer qualifcation: ")
        experience = input("Enter the trainer experience: ")
        mob_no = input("Enter the mobile_no. of trainer: ")
        email_id = input("Enter the Email_ID of trainer: ")
        trainer_password = input("Enter the password of trainer: ")
        trainer_data = {"name":trainer_name,"gender":gender,"qualification":qualification,"experience":experience,"mob.No":mob_no,"mail_ID":email_id,"password":trainer_password}
        self.trainer_details[self.count] = trainer_data
        with open("add_trainernew.json",'w') as f:
            json.dump(self.trainer_details,f,indent = 4)
        return self.trainer_details    
          
    
    def read_trainer_details(self):
        with open("add_trainernew.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Trainer_ID :{k} || Trainer_details :{v}")
            print("*"*100) 
        
    
    def add_student(self):
        self.count = self.count+1
        student_size = int(input("Enter the size of students to add: "))
        student_list = []
        for i in range(1,student_size+1):
            print(f"Enter the student details {i}")
            name = input(f"Enter the name of student {i}: ") 
            age = input(f"Enter the age of student {i}: ")
            qualification = input(f"Enter the qualfication of student {i}: ")
            Mob_No = input(f"Enter the contact number of student {i}: ") 
            student_data = {"name":name,"age":age,"qualification":qualification,"mob_no":Mob_No}
            student_list.append(student_data)
        self.student_details[self.count] = student_list
        with open("add_student_new.json",'w') as f:
            json.dump(self.student_details,f,indent=4)
        return self.student_details        
    
    def read_student_details(self):
        with open("add_student_new.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print (f" Batch_id: {k} || Batch_students {v}")  
            print("*"*100)  

    def update_trainer_details(self):
        with open("add_trainernew.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Trainer_ID : {k} || Trainer_Details : {v}")
            print("*"*100) 

        print(f"You can update trainer details here!")
        id = input("Enter trainer ID which you want to update: ")
        field = input("Enter which filed to update: ")
        update_value = input("Enter updated value: ")
        data[id][field] = update_value
        with open("add_trainernew.json",'w') as f:
            json.dump(data,f,indent=4)
        return data

    def remove_trainer(self):
        with open("add_trainernew.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Trainer_ID : {k} || Trainer Details : {v}")
            print("*"*100)
        print("You can remove Trainer_id here!")
        id = input("Enter the trainer id which you want to del: ")
        del data[id]
        with open("add_trainernew.json",'w') as f:
            json.dump(data,f,indent=4)
        return data


                          
    
            
               
                   
            
    
    
x = admin_panel()
#print(x.add_module())   
#print(x.read_module_details())
# print(x.add_trainer())   
# print(x.add_trainer())
#print(x.read_trainer_details()) 
#print(x.add_student())  
#print(x.read_student_details()) 
#print(x.update_trainer_details()) 
# print(x.remove_trainer())       
            
            
          


