#Object Composition

class Computer:
    def __init__(self):
        self.users={}

    def addUser(self,user):
        self.users[user.name]=user

    def printUsers(self):
        for user in self.users.values():
            print("User name: {} has {} access".format(user.name,user.access))


class User:
    def __init__(self,name,access):
        self.name=name
        self.access=access



c1=Computer()
c1.addUser(User("Vaibhav","admin"))
c1.addUser(User("Riya","public"))
c1.addUser(User("Zeal","public"))

c1.printUsers()
