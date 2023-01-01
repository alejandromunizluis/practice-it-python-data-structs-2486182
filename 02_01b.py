from collections import deque

def main():
    #add code here
    storage = deque(maxlen=5)
    storage.append("apple")
    storage.append("pears")
    storage.append("orange")
    storage.append("strawberry")
    storage.append("pineapple")
    print(storage)
    storage.append("coconut")
    storage.appendleft("peach")
    print(storage)
    return storage

if __name__ == "__main__":
    main()