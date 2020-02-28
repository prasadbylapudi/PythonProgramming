'''file1=open('test.txt')
contents=file1.readlines()
file1.close()
print(contents)'''

'''This can make your code messy, and if you have to open
and modify multiple files, you could lose track of which files you have opened.'''
#by using the with keyword we can open multiple files at once
'''with open('test.txt') as f:
    contents=f.readlines()

print(contents)
'''

with open('test.txt') as f,open('test1.txt') as f1,open('test2.txt') as f2:
    contents ,contents1,contents2=f.readlines(),f1.readlines(),f2.readlines()

print(contents,"\n")
print(contents1,"\n")
print(contents2,"\n")


