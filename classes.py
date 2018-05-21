# Classes & Objects

class Person:
    __name = ''
    __email = ''
    __address = ''
    
    def __init__(self,name,email,address):
        self.__name = name
        self.__email = email
        self.__address = address
    
    def set_address(self, address):
        self.__address = address
    
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def get_address(self):
        return self.__address
    
    def toString(self):
        return '{} can be contacted at {} live at {}'.format(self.__name,self.__email,self.__address)
    
#brad = Person('Brad Traversy','Brad@gmail','123 Something St.')
# brad.set_name('Brad Traversy')
# brad.set_email('brad@gmail.com')

#print(brad.get_name())
#print(brad.toString())

class Customer(Person):
    __balance = 0
    
    def __init__(self,name,email,address,balance):
        self.__name=name
        self.__email=email
        self.__address=address
        self.__balance=balance
        super(Customer, self).__init__(name,email,address)
        
    def set_balance(self,balance):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
        
    def toString(self):
        return '{} has a balance of {} can be contacted at {} live at {}'.format(self.__name,self.__balance,self.__email,self.__address)
    
john = Customer('John Doe', 'jdoe@gmail','123 @Something st',100)

john.set_balance(4000)

print(john.toString())

Uzuki = Customer('Shimamura Uzuki','ganbarimasu@gmail.com','tiedofxbyproducer',100)
print(Uzuki.toString())