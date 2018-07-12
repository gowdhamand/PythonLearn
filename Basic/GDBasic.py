
# coding: utf-8

# Function Testing

# In[1]:


def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * x

def div(x,y):
    if y == 0:
        print('Y cant be zero')
        return 0
    else:
        return x/y
    
    
x = 10
y = 2

print(x , '+' , y , '=' , add(x,y))
print(x , '-' , y , '=' , sub(x,y))
print(x , '*' , y , '=' , mul(x,y))
print(x , '/' , y , '=' , div(x,y))


# Loop Learn Testing

# In[2]:


def numReturn():
    i = 0;
    while i < 5:
        print(i);
        i += 1;
        
numReturn()


# In[3]:


def forLoopTesting(sList):
    for x in sList:
        print(x)

x = ['gowdhaman', 'karthiga', 'shaara']
forLoopTesting(x)

'''Testing range'''
for z in range(1,11):
    print(z)


# Some File Operation

# In[4]:


text = 'Gowdhaman! Please write some file. Following line is going to be new line \n This is going to be new file'


'''writing to a file'''
saveFile = open('gdTesting.txt','w')
saveFile.write(text)
saveFile.close()


# In[5]:


'''appending someting to a file'''
appendMe = '\nI am adding more information to a file'

appendFile = open('gdTesting.txt','a')
appendFile.write(appendMe)
appendFile.close()


# In[6]:


'''read from a file'''
readMe = open('gdTesting.txt','r').read()
print(readMe)

'''read to list'''
readList = open('gdTesting.txt','r').readlines()
print(readList)


# Creating Class

# In[7]:


class calculator:
    
    def add(x,y):
        return x + y

    def sub(x,y):
        return x - y

    def mul(x,y):
        return x * x

    def div(x,y):
        if y == 0:
            print('Y cant be zero')
            return 0
        else:
            return x/y
        
print(calculator.add(10,20))
print(calculator.sub(10,20))


# In[8]:


'''get user input'''
x = input('what is your name?')
print('Hello', x)


# Basic Statistics Stuff (Mean, Standard dev)

# In[9]:


import statistics

exampleList = [1,2,3,4,9,10,2, 3,2,2,2,2]

print('Mean :',statistics.mean(exampleList))
print('Median :',statistics.median(exampleList))
print('StdDev :',statistics.stdev(exampleList))
print('varience',statistics.variance(exampleList))


# Creating and importing modules

# In[10]:


import sys

print(sys.version)


# In[11]:


import statistics as s

exampleList = [1,2,3,4,9,10,2, 3,2,2,2,2]

print('Mean :',s.mean(exampleList))
print('Median :',s.median(exampleList))
print('StdDev :',s.stdev(exampleList))
print('varience',s.variance(exampleList))


# In[12]:


'''if we dont wanted to reference is eachtime'''
from statistics import variance

exampleList = [1,2]
print(variance(exampleList))


# In[14]:


'''if we want more stuff'''
from statistics import variance as v, mean

exampleList = [1,2]
print('variance :',variance(exampleList))
print('mean :',mean(exampleList))

'''with ref'''
print('###########')
print('variance :',v(exampleList))
print('mean :',m(exampleList))


# List and Tuples

# In[15]:


'''Tuples'''
x = 1,2,3,4
x = (1,2,3,4)

'''List'''
y = [1,2,3,4]

print(x[1])

'''Tuples can be generated faster and iterated fater'''

'''example of tuple'''
def exampleFunction():
    return 1,2

x,y = exampleFunction()

'''if you wanted to create immutable stuff...you can create using tuple...list can be mutable'''


# In[16]:


x = [1,2,3,3,4,1,2,3,3,4,5,5,5,7]

'''add something'''
x.append(2)

'''insert--> first param is position and 2nd one is the value'''
x.insert(2,99)

'''remove--> give element position'''
'''x.remove(0) is not working'''
x.remove(x[2])


print(x)
print('index of 5 :',x[5])
print('index of last element :', x[-1])
print('index of last 2nd element :', x[-2])
print('Eelement from 1:5 :', x[1:5])
print('Eelement from 1: :', x[5:])
print('Index of which provides you the position :', x.index(1))
print('Count number of 2 in list :', x.count(2))
x.sort()
print('Sorting the list :', x)


# In[17]:


y = ['Gowdhaman', 'Shaara', 'Karthiga']

y.sort()
print(y)

