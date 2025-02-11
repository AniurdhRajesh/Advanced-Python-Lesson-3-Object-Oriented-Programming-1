class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose
    
    def introduce(self):
        print(f"Hello, I am {self.name}, a {self.model} model robot.")
        print(f"My purpose is to {self.purpose}.")

robot1 = Robot("RoboHelper", "XJ-300", "assist humans in daily tasks")
robot2 = Robot("AutoServe", "YZ-200", "serve food and beverages")

robot1.introduce()
robot2.introduce()
