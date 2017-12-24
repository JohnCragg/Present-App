class Person(object):
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


    def say_hello(self):
        print ("hello %s %s !" % (self.first_name, self.last_name))

    def print_email_provider(self):
        separated = self.email.split("@")
        print (separated[0])
