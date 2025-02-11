class Robot:
    def __init__(self,name,version,function):
           self.name = name
           self.version = version
           self.function = function
    def intro(self):
          intro=(f"Hello,I am {self.name}, \n"
                 f"I am version{self.version},\n"
                 f"My Funtion is to{self.function}.")
          return intro
robot1=Robot("GaurdianBot","1.0"," Provide Security monitoring")
robot2=Robot("AssistBot","2.0"," Help with household Chores")
print(robot1.intro())
print(robot2.intro())
