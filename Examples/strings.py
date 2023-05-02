# Some string examples
def print_strings(a1, a2):
    print(a1)
    print(a2)
    print(id(a1))
    print(id(a2))
    print()


s1 = "A"
s2 = "B"
print_strings(s1, s2)
# Result makes sense ... two different memory locations

s1 = "A"
s2 = "A"
print_strings(s1, s2)
# Result somewhat surprising ... same memory location!  Python is optimizing!

s2 = "B"
print_strings(s1, s2)
# Result is ... I don't know ... s2 is now in a new memory location!

s1 = "AAaa"
s2 = "AAaa"
print_strings(s1, s2)
# Still optimizing, even with multi-character strings

s1 = "A"
s2 = s1
print_strings(s1, s2)
# Now, this kinda makes sense, right? Same memory locations
