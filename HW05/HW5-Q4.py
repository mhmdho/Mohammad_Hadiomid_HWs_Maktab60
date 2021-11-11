# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:53:42 2021

@author: Lenovo
"""

def add_to_list_in_dict(thedict, listname, element):
    try: 
        thedict[listname] #check the list name to be exist
        l = thedict[listname]
        print("\n%s already has %d elements." % (listname, len(l)))
    except Exception: # if the list does not exist it raise and creat the list
        print('\nThe list does not Exist...')
        thedict[listname] = []
        print("Created %s." % listname)
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))
    


d = {'class1':['Ali', 'Hosein', 'Omid'], 'class2':['Hadi', 'Hassan', 'Akbar']}
#d = input('Enter your dictionary:')
lst_name = input('Enter list name:')
e = input('Enter your Elemnt:')

add_to_list_in_dict(d, lst_name, e)
print('\n', lst_name, 'elemnt(s) is:', d[lst_name])
