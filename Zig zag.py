#zigzag
print("Nishanth M Y,USN:1AY24AI078,SEC:O")
lines = 9
max_spaces = lines 
for i in range(lines):
    if i <= max_spaces:
        spaces = i
    else:
        spaces = lines - i - 1
    print(" " * spaces + "*" * 8)
