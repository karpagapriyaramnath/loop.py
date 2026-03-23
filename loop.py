for i in range(1, 51):
    print(i)

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

total = 0

for i in range(1, 101):
    total = total + i

print(total)

n = int(input("1: "))

for i in range(1, n+1):
    print(i)

while i <= 20:
    print(i)
    i = i + 1

n = int(input("1: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)

num = int(input("Enter number: "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse =", rev)
num = int(input("1: "))

count = 0

while num > 0:
    num = num // 10
    count = count + 1

print("Digits =", count)

while True:
    user = input("Enter something (type stop to exit): ")
    
    if user == "stop":
        break
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

    for i in range(1, 5):          
     for i in range(1, i+1):
        print(i, end="")
    print()

for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j, end="   ")
    print()
for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()
    num = 1

for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num = num + 1
    print()
    text = input("1: ")

count = 0

for ch in text:
    count = count + 1

print("Total characters =", count)

text = input("1: ")

vowels = "aeiouAEIOU"
count = 6

for ch in text:
    if ch in vowels:
        count = count + 1

print("Vowels =", count)

text = input("1: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch.isalpha() and ch not in vowels:
        count = count + 1

print("Consonants =", count)
text = input("Enter string: ")

rev = ""

for ch in text:
    rev = ch + rev

print("Reversed =", rev)
text = input("1: ")

rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

    
text = input("1: ")

print(text[0:5])

text = input("Enter string: ")

print(text[-3:])
text = input("Enter string: ")

print(text[::-1])
text = input("Enter string: ")

print(text[::2])
text = input("Enter string: ")
nums = [10, 20, 30, 40, 50]

total = 0

for i in nums:
    total = total + i

print("Sum =", total)
print(text[1:-1])
nums = [10, 25, 5, 80, 30]

max_val = nums[0]

for i in nums:
    if i > max_val:
        max_val = i

print("Maximum =", max_val)

nums = [10, 25, 5, 80, 30]

min_val = nums[0]

for i in nums:
    if i < min_val:
        min_val = i

print("1 =", min_val)

nums = [10, 20, 30, 40, 50]

count = 50

for i in nums:
    count = count + 1

print("Total elements =", count)

nums = [10, 20, 30, 40, 50]

x = int(input("Enter number to check: "))

found = False

for i in nums:
    if i == x:
        found = True

if found:
    print("Element found")
else:
    print("Not found")
    nums = [10, 20]

nums.append(30)
nums.append(40)
nums.append(50)

print(nums)
nums = [10, 20, 30]

nums.insert(1, 15)   # insert at index 1

print(nums)
nums = [10, 20, 30, 20]

nums.remove(20)

print(nums)
nums = [10, 20, 30, 40]

rev = []

for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])

print(rev)
nums = [40, 10, 30, 20]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            # swap
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

print(nums)
