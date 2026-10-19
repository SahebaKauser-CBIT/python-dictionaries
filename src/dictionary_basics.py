
# Python Dictionary Basics

# Creating a dictionary
student = {
    "name": "Saheba",
    "age": 21,
    "course": "Python"
}

print("Original Student Details:")
print(student)

# Accessing dictionary values
print("\nStudent Name:", student["name"])
print("Student Age:", student["age"])

# Adding a new key-value pair
student["city"] = "Hyderabad"

# Updating an existing value
student["age"] = 22

print("\nUpdated Student Details:")
for key, value in student.items():
    print(f"{key}: {value}")

# Removing a key-value pair
student.pop("city")

print("\nAfter Removing City:")
print(student)
