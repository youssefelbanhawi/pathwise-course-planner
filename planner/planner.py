def can_take(course, completed, catalog):
    return all(prereq in completed for prereq in catalog[course]["prereqs"])

def plan_schedule(catalog, required_courses, max_credits_per_term=15):
    schedule = {}
    completed = set()
    term_order = ["Fall", "Spring"] * 4  # Plan for 4 semesters
    i = 0

    while required_courses:
        term = term_order[i]
        semester = []
        credits = 0
        still_needed = []

        for course in required_courses:
            info = catalog[course]
            if (term in info["offered"]
                and can_take(course, completed, catalog)
                and credits + info["credits"] <= max_credits_per_term):
                semester.append(course)
                completed.add(course)
                credits += info["credits"]
            else:
                still_needed.append(course)

        schedule[f"Semester {i+1} ({term})"] = semester
        required_courses = still_needed
        i += 1

    return schedule
