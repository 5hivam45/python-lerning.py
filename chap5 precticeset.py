# PROBLEM:1
# words = {
#     "madad":"help",
#     "billi":"cat",
#     "kursi":"chair"  
# }

# word = input("Enter the word you want meaning of :")
# print(words[word]) #OUTPUT WILL BE = if print billi output "cat"

# PROBLEM:2
# s = set()
# n = input("Enter number:")
# s.add(int(n))
# n = input("Enter number:")
# s.add(int(n))
# n = input("Enter number:")
# s.add(int(n))
# n = input("Enter number:")
# s.add(int(n))
# n = input("Enter number:")
# s.add(int(n))
# n = input("Enter number:")
# s.add(int(n))
# n = input("Enter number:")
# s.add(int(n))
# n = input("Enter number:")
# s.add(int(n))
# print(s)  #OUTPUT WILL BE = {1, 2, 3, 4}


# # PROBLEM:3
# s = set()
# s.add(18)
# s.add("18")
# print(s)  #OUTPUT WILL BE = {18, '18'}

# PROBLEM:4
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(s) #OUTPUT WILL BE = {20, '20'}
# print(len(s)) #> **Set does not consider the data type; if the values are equal, it stores them only once.**


# # PROBLEM:5
# s = {} #what is the type of 's'
# print(type(s)) #output will be =<class 'dict'>


# PROBLEM:6
d = {}
name = input("Enter friend name:")
lang = input("Enter language name:")
d.update({name:lang})
name = input("Enter friend name:")
lang = input("Enter language name:")
d.update({name:lang})
name = input("Enter friend name:")
lang = input("Enter language name:")
d.update({name:lang})
name = input("Enter friend name:")
lang = input("Enter language name:")
d.update({name:lang})  #OUTPUT WILL BE = {'ishan': 'c', 'somil': 'c++', 'raj': 'python', 'shivang': 'java script'}
print(d)


