
from collections import namedtuple

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    #check if they can take a certain order, given their car's capacity.
    drivers = namedtuple('drivers', ['name', 'car', 'capacity'])
    d = drivers('Iris', 'Toyota Prius', 7)
    return print(d.name)

if __name__ == "__main__":
    main()