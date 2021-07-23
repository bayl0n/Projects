# create a stack using a list

class Stack:
    def __init__(self):
        self.__stack = list()

    def __str__(self):
        return str(self.__stack)

    def push(self, value):
        self.__stack.append(value)
        return self.__stack[len(self.__stack) -1]

    def pop(self):
        if len(self.__stack) > 0:
            temp = self.__stack[len(self.__stack) - 1] 
            self.__stack.pop(len(self.__stack) - 1)
            return temp
        else:
            return None

    def top(self):
        if len(self.__stack) > 0:
            return self.__stack[len(self.__stack) - 1]
        else:
            return None


if __name__ == "__main__":
    myStack = Stack()

    print(myStack.push("Banana"))
    print(myStack.pop())
    print(myStack.top())
    print(myStack)
