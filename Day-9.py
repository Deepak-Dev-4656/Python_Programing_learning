text = "thid is high level programing language"
word = ["i", "love", "python"]

print(text.upper())
print(text.split())
print(",".join(word))
print(text.replace("thid","this"))
user_input = input("Enter a text: ")
if user_input == user_input[::-1]:
    print("pelindrom")
else:
    print("not pelindrom")