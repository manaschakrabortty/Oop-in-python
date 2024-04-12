class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name=name
        self.password=password
        self.current_job_title= current_job_title


    def change_password(self, new_password) :
        self.password=new_password

    def change_job_title (self, new_job_title):
        self.current_job_title= new_job_title
    
    def get_user_info(self):
        print(f"User {self.name} Currently work as {self.current_job_title}. you can contact them at{self.email }\n THANK YOU")

#USER ONE 
app_user_one=User("mans@cc.com", "Manas Chakrabortty", "pwd1", "devops engineer")
app_user_one.get_user_info()


#USER ONE CHANGE JOB TITLE
app_user_one.change_job_title("devops trainer")
app_user_one.get_user_info()


#USER TWO 
app_user_two=User("purbasa@cc.com", "purbasa Chakrabortty", "pwd12", "dataengineer")
app_user_two.get_user_info()
