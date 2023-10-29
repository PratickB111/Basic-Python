# showing the data types of python

# normal string data type
var = "Hello python!"
print(type(var)) # type() function to check the type of data type
print(var)

# setting specific data type for string in python
nextVar = str("hello python coders")
print(nextVar)

# integer data type
var = 1000 # re-declaring the variable
print(type(var)) # type() function to check the data type
print(var)

# setting specific data type for integer in python
nextVar = int(2000)
print(nextVar)

# floating point data type
var = 2.1432 # re-declaring 
print(type(var))
print(var) # display the variable data

# setting specific data type for floating point data in python
nextVar = float(14.76)
print(nextVar)

# complex data type
var = 2j # 'j' denotes that the value is a complex number
print(type(var)) # use of type() function
print(var) # display the data

# setting specific data type for complex in python
nextVar = complex(23j)
print(nextVar)

# list in python
var = ["Google", "Microsoft", "Meta", "Amazon", "SpaceX"]
print(type(var))
print(var)

# setting specific data type for list in python
nextVar = list(("Mobile", "Tablet", "Laptop", "Desktop", "Mainframe", "Super computer"))
print(nextVar)

# tuple in python
var = ("Google", "Amazon", "Goldman Sachs", "PaloAlto") # re-declaring var 
print(type(var))
print(var)

# setting specific data type for tuple in python
nextVar = tuple(("Cherry", "Strawberry", "Berries"))
print(nextVar)

# range in python
var = range(10) # range in python starts with 0
print(type(var))
print(var)

# dictionary in python aka hash map or hash table in other languages
var = {
  "First Name" : "Pratick",
  "Last Name" : "Baraik",
  "Designation" : "Python Dev" 
}
print(type(var))
print(var)

# setting specific data type for dictionary in python
nextVar = dict(
            Language = "Python",
            Duration = "2 Months"
          )
print(nextVar)

# set or array in python
var = {
  "Pen",
  "Pencil",
  "Paper"
}
print(type(var))
print(var)

# setting specific data type for set in python
nextVar = set(("Eat", "Sleep", "Code", "Repeat"))
print(nextVar)

# frozenset in python
var = frozenset({
  "Bard",
  "Bing",
  "GPT"
})
print(type(var))
print(var)

# boolean in python
var = False
print(type(var))
print(var)
var = True # re-declared
print(var)

# setting specific data type for boolean in python
nextVar = bool(10)
print(nextVar)

# bytearray data type in python
var = bytearray(4) # declaring bytearray
print(type(var))
print(var)

# memoryview data type in python
var = memoryview(bytes(3))
print(var)

# none type in python
var = None
print(type(var))
print(var)