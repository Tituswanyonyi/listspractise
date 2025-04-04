users = ['John','Osama', 'Sammy']
data =['mechanics','Rolls','Kiwi']
print('John' in users)
print('John' in data)
print(users[1])
print(data[-1])
print(users.index('Sammy'))
print('')
print(users[0:2])
print (users[0:])
print ('')
print(len(users))
print('')
#Append method
users.append('Elsa')
print(users)
#adding other lists
users +=['Patrick', 'Owen']
print(users)
users.extend(['Robert','Sang'])
print(users)
print ('')
#Passing pre-existing list
users.extend(data)
print(users)
print('')
#Adding item at specific position
users.insert(0, 'Amos')
print(users)
print('')
#using bracket method
users[3:3] = ['Philip']
print (users)
print ('')
#slicing method
users[0:3] =['Ken', 'Dorine']
print(users)
print('')
#Remove feature
users.remove('mechanics')
print (users)
print('')
#pop method, removes the last item
users.pop()
print(users)
print('')
#deleting
del users[0]
print(users)
print('')
#Clear method: Clears items from a list
data.clear()
print (data)
print('')
#sort method arranges the list alphabetically
users.sort()
print (users)
print('')
#Reverse method
nums = [9,7,5,3]
nums.reverse()
print(nums)
nums.sort(reverse=True)
print(nums)
print('')
#Copy function
numscopy= nums.copy()
mynum = list(nums)
newnum = nums[0:5]
print(numscopy)
print(mynum)
print(newnum)
print('')
#creating a new list using list
mynewlist =list([4,'Neil','mechanization'])
print(mynewlist)
print ('')
#TUPLES LESSON
mytuple = tuple((4,'Sam','Rhys'))
newtuple= (3, 'Sketch', 'Handy')
print(mytuple)
print(newtuple)
print(type(mytuple))