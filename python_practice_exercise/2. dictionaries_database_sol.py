""" 
Make a database of dictionaries which hold id, name , course of students
1. Take input for id, name and course.
2. Store that to dictionary.
3. Append the dictionary to array.
"""

if __name__ == "__main__":
    l1 = []
    run = True

    while run:
        choice = input('press n/N to stop: ')
        if choice == 'n' or choice == 'N':
            run = False
        else:
            d1 = {'id': input('enter your id: '),
                  'name': input('enter your name: '),
                 'course': input('enter course name: ')}
            l1.append(d1)
print(l1) # display list of dictionaries
