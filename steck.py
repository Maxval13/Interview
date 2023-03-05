class Steck:

    def __init__(self):
        self.list_el = []

    def isEmpty(self):
        if not len(self.list_el):
            return True
        return False

    def push(self, el):
        self.list_el.append(el)

    def pop(self):
        return self.list_el.pop()

    def peek(self):
        return self.list_el[-1]

    def size(self):
        return len(self.list_el)


def balance(text):
    stecks = Steck()
    for item in text:
        if item in '({[':
            stecks.push(item)
        elif item in ')}]':
            if not stecks.size():
                return 'Несбалансированно'
            open_bracket = stecks.pop()
            if open_bracket == '(' and item == ')':
                continue
            if open_bracket == '{' and item == '}':
                continue
            if open_bracket == '[' and item == ']':
                continue
            return 'Несбалансированно'
    if stecks.isEmpty() and stecks.size() == 0:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'
