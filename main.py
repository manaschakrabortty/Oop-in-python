# import user

from user import User
from post import Post

#USER ONE 
app_user_one=User("mans@cc.com", "Manas Chakrabortty", "pwd1", "devops engineer")
app_user_one.get_user_info()


#USER ONE CHANGE JOB TITLE
app_user_one.change_job_title("devops trainer")
app_user_one.get_user_info()


#USER TWO 
app_user_two=User("purbasa@cc.com", "purbasa Chakrabortty", "pwd12", "dataengineer")
app_user_two.get_user_info()



new_post=Post("on a secriot mission todat", app_user_two.name)
new_post.get_post_info()