"""
Python List Practice - Part 1
-----------------------------
Question 1:
fruits1 = ["apple", "banana"]
fruits2 = ["orange", "mango"]

1. fruits1 ko fruits2 se extend karo
2. Fir fruits1 print karo
"""

fruits1 = ["apple", "banana"]
fruits2 = ["orange", "mango"]

fruits1.extend(fruits2)
print(fruits1)


"""
Question 2:
shopping = ["milk", "bread", "eggs", "bread", "butter", "cheese"]

1. Sort the list - alphabetically sort karo
2. Remove "milk" - milk ko list se hatao
3. Count "bread" - bread kitni baar hai count karo
4. Reverse the list - list ko ulta karo
"""

shopping = ["milk", "bread", "eggs", "bread", "butter", "cheese"]

shopping.sort()
shopping.remove("milk")
count = shopping.count("bread")
shopping.reverse()

print(shopping)
print("Bread count:", count)


"""
Question 3:
books = ["Python", "Java", "C++", "Python", "JavaScript", "Java", "Python"]

1. Books list sort karo
2. "Python" kitni baar hai count karo
3. "Java" ki position find karo
4. List reverse karo
"""

books = ["Python", "Java", "C++", "Python", "JavaScript", "Java", "Python"]

books.sort()
python_count = books.count("Python")
java_position = books.index("Java")
books.reverse()

print("Sorted and reversed books:", books)
print("Python count:", python_count)
print("Java position:", java_position)


"""
Question 4:
data = [15, 3, 8, 20, 3, 15, 8, 3]

1. List sort karo
2. Reverse sort karo (descending order)
3. Number 3 kitni baar aaya hai count karo
4. Number 15 ki position find karo
"""

data = [15, 3, 8, 20, 3, 15, 8, 3]

data.sort()
print("Sorted:", data)

data.sort(reverse=True)
print("Descending:", data)

count_3 = data.count(3)
print("Count of 3:", count_3)

position_15 = data.index(15)
print("Position of 15:", position_15)
