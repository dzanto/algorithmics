n = int(input())
courses = []
for course in range(n):
    courses.append(input())
unique_courses = set(courses)
for course in courses:
    if course in unique_courses:
        print(course)
        unique_courses.discard(course)
