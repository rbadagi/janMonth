PYTHON STRING METHODS - REAL WORLD EXAMPLES

1. upper()
text = "python"
print(text.upper())  # PYTHON

2. lower()
text = "PYTHON"
print(text.lower())  # python

3. title()
name = "raghavendra badagi"
print(name.title())

4. strip()
text = "  hello  "
print(text.strip())

5. isdigit()
pin = "1234"
print(pin.isdigit())

6. isalpha()
word = "Python"
print(word.isalpha())

7. alphanumeric (isalnum())
username = "user123"
print(username.isalnum())

8. startswith() / endswith()
file = "program.py"
print(file.startswith("pro"))
print(file.endswith(".py"))

9. find()
text = "hello world"
print(text.find("world"))

10. count()
text = "banana"
print(text.count("a"))

11. replace()
card = "1234-5678-9012-3456"
print(card.replace("9012-3456", "XXXX-XXXX"))

12. split()
data = "John,25,Bangalore"
print(data.split(","))

13. join()
skills = ["Python", "SQL", "Automation"]
print(", ".join(skills))

14. zfill()
invoice = "45"
print(invoice.zfill(6))

15. format()
name = "Raghavendra"
age = 30
print("My name is {} and age is {}".format(name, age))

16. f-string
print(f"My name is {name} and age is {age}")

--- Mini Project Snippet ---
full_name = "Raghavendra Badagi"
username = full_name.lower().replace(" ", "_")
print(username)
