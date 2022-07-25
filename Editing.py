list = []

while True:
    
    choice = input('Do you want to Read, Write, or Delete?\n')
    
    if choice == 'r' or choice == 'R':
        read = open("text.txt", "r")
        print(read.read())
        read.close()

    elif choice == 'w' or choice == 'W':
        write = open("text.txt", "w+")
        text = input('What do you want to write?\n')
        line = int(input('What line do you want to write in?\n'))
        list.insert(line, text + "\n")
        write.writelines(list)
        write.close()
        

    elif choice == 'd' or choice == 'D':
        delete = open("text.txt", "w")
        delete.write('')
        delete.close()
        list = []
    