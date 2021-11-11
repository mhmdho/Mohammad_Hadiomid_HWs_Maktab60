# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:38:56 2021

@author: Lenovo
"""

print('\n ......Question 1...... \n')
class Opus:
    def __init__(self, title, owners):
        self.title = title
        self.owners = owners
    
    def is_valid(self, owner):
        if type(self.owners).__name__ == 'list':
            for o in self.owners:
                if type(o).__name__ != owner:
                    return False
                else:
                    return True
        else:
            if type(self.owners).__name__ != owner:
                return False
            else:
                return True

    def __str__(self):
        return f'This is an Opus object'

    def __repr__(self):
        return f'Opus(' + self.title + ',' + str(self.owners.name) + ')'                
    

class Paper(Opus):
    def __init__(self, title, owners, mag_name, year):
        super().__init__(title, owners)
        self.mag_name = mag_name
        self.year = year
        self.owner = 'Researcher'

    def owners_count(self):
        if type(self.owners).__name__ == 'list':
            return len(self.owners)
        else:
            return 1
    
    
    def is_valid(self):
        return super().is_valid(self.owner)

    def __str__(self):
        return f'This is a Paper object'

    def __repr__(self):
        return f'Opus(' + self.title + ',' + str(self.owners) + ')'

        
class Poetry(Opus):
    def __init__(self, title, owners, formatting):
        super().__init__(self, title, owners)
        self.formatting = formatting
        self.owner = 'Poet'
        if type(self.owners).__name__ == 'list':
            return f'You entered wrong information (Two Poetry)'


    def is_valid(self):
        return super().is_valid(self.owner)


class Book(Opus):
    book_count = 0
    def __init__(self, title, owners, ISBN, publication):
        super().__init__(title, owners)
        self.ISBN = ISBN
        self.publication = publication
        self.owner = 'Author'
        Book.book_count += 1

    def owners_count(self):
        if type(self.owners).__name__ == 'list':
            return len(self.owners)
        else:
            return 1
        
    def __del__(self):
        Book.book_count -= 1

    def is_valid(self):
        return super().is_valid(self.owner)


class Human:
    def __init__(self, name, Email, sex):
        self.name = name
        self.Email = Email
        self.sex = sex

    def __str__(self):
        return f'This is a Human object'

    def __repr__(self):
        return f'Human(' + self.name + ',' + self.Email + ',' + self.sex + ')'

class Researcher(Human):
    def __init__(self, name, Email, sex, field, university):
        super().__init__(name, Email, sex)
        self.field = field
        self.university = university


class Poet(Human):
    def __init__(self, name, Email, sex, style):
        super().__init__(name, Email, sex)
        self.style = style


class Author(Human):
    def __init__(self, name, Email, sex, author_code, genre):
        super().__init__(name, Email, sex)
        self.author_code = author_code
        self.genre = genre



a = Author('JK', 'asd@gmail.com', 'F', 10034, 'Siencefiction')
a2 = Author('ali', 'ali@gmail.com', 'M', 10044, 'Siencefiction')

b = Book('harry', a , 4315, 'jungle')
b2 = Book('ha22rry', a2 , 438615, 'junrfgle')

b.is_valid()

b.__str__()
b.__repr__()
print(b)

a.__str__()
a.__repr__()
print(a)

c= Paper('res', 'moha', 'isi', 1900)
c.__str__()
c.__repr__()
