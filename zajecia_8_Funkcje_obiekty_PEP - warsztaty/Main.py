class User: # tworzymy klasę o nazwie "User"
    def __init__(self, firstname, lastname): # przy tworzeniu obiektu będą wymagane dwa parametry: firstname, lastname
        self.firstname = firstname # parametr firstname zapiszemy wewnątrz obiektu jako właściwość firstname
        self.lastname = lastname # parametr lastname zapiszemy wewnątrz obiektu jako właściwość lastname

    def print_hello(self): #ta metoda nie używa parametrów, tylko obiektu, w którym jest zadeklarowana
        print("Hello {} {}".format(self.firstname, self.lastname))

    def print_bye(self): #ta metoda nie używa parametrów, tylko obiektu, w którym jest zadeklarowana
        print("Bye {} {}".format(self.firstname, self.lastname))

user1 = User("Ewa", "Nowak")
user2 = User("Jan", "Kowalski")

user1.print_hello()
user2.print_hello()
user1.print_bye()
user2.print_bye()