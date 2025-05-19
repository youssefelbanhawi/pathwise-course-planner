import json
from planner.planner import plan_schedule

# Load course catalog
with open("courses.json", "r") as file:
    courses = json.load(file)

# Required courses
required = ["SE 310", "SE 320", "SE 311", "ECE 211"]

# Generate schedule
schedule = plan_schedule(courses, required)

# Print result
for term, classes in schedule.items():
    print(term)
    for course in classes:
        print(f"  - {course}: {courses[course]['name']}")
