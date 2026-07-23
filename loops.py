print("for loop")
for i in range(1, 6):
    print(i)
print("while loop")
count = 1 
while count <= 5:
    print(count)
    count += 1
print("break statement")
for i in range(1,10):
    if i == 4:
        print("loop stopped at",i)
        break 
    print(i)
print("continue statement")
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

print("nested loops")
for i in range(1,6):
    for j in range(1,6):
        print(f"i={i}, j={j}")
print("loop with else")
for i in range(1,10):
    print(i)
else:
    print("loop completed successfully")
print("while loop with else")
x = 1
while x <= 9:
    print(x)
    x += 1 
else:
    print("while loop completed successfully")