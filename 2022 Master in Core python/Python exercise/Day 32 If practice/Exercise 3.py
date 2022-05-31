# Check if input is vowel or not
# Vowel is a e i o u

input = str(raw_input("Enter the character: "))
vowel = ["a","e","i","o","u"]

if input in vowel:
    print("Your letter is a vowel.")
else:
    print("Your letter is not vowel.")