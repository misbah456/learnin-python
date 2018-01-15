from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename} dawg")
print(txt.read())

print("Type that jawn again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
