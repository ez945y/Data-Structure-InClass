class Student():
    def __init__(self):
        self.name = ''
        self.score = 0
        self.id = 0
        self.next = None

def insert_f():
    global head
    global ptr
    global current
    global prev
    ptr = Student()
    ptr.next = None
    ptr.name = input('Student name : ')
    ptr.score = eval(input('Student score: '))
    print()

    prev = head
    current = head.next
    while current != None and current.score >= ptr.score:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr

def delete_f():
    global head
    global current
    global prev
    del_name = ''
    if head.next == None:
        print(' Have no record!\n')
    else:
        del_name = input(' Delete student name: ')
    prev = head
    current = head.next
    while current != head and del_name != current.name:
        prev = current
        current = current.next
    if current != head :
        prev.next = current.next
        current = None
        print('\n Student %s record deleted\n' % del_name)
    else:
        print('\n Student %s not found\n' % del_name)

def modify_f():
    global head
    global current
    global prev
    if head.next == None:
        print(' Have no record! \n')
    else:
        modify_name = input(' Modify student name: ')
    prev = head
    current = head.next
    while current != None and modify_name != current.name:
        prev = current
        current = current.next
    if current != None:
        print('\n Student name: %s' % current.name)
        print(' Student score: %d\n' % current.score)
        prev.next = current.next
        current = None
        newscore = eval(input(' Please enter new score: '))
        newsname = eval(input(' Please enter new name: '))
        newid = eval(input(' Please enter new id: '))
        ptr = Student()
        ptr.next = None
        ptr.name = newname
        ptr.score = newscore
        ptr.id = newid
        prev = head
        current = head.next
        while current != None and current.score >= ptr.score:
            prev = current
            current = current.next
        ptr.next = current
        prev.next = ptr
        print(' Data updated successfully!\n')
    else:
        print('\n Student %s not found!\n' % modify_name)

def display_f():
    global head
    global current
    global prev
    count = 0
    if head.next == None:
        print(' Have no record! \n')
    else:
        print('%s          %s' % ('Name', 'Score'))
        for i in range(20):
            print('-', end = '')
        print()
        current = head.next
        while current != None:
            print('%s            %d' % (current.name, current.score))
            count = count + 1
            current = current.next
        for i in range(20):
            print('-', end = '')
        print()
        print('Total %d record(s) found\n' % count)

def main():
    global head
    global current
    global prev 
    option = int(input(' Your option is：'))
    print()
    if option == 1:
        insert_f()
    elif option == 2:
        delete_f()
    elif option == 3:
        modify_f()
    elif option == 4:
        display_f()
    elif option == 0:
        sys.exit('Goodbye!')

ptr = None
current = None
prev = None

head = Student()
head.next = None

main()