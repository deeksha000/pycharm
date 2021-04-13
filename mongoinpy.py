import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client["fullstack"]
collection = database['students']
students = [student["mark"] for student in collection.find({})]  # can add an if statement after the for loop
# for student in students:
#   print(student)
print(students)
