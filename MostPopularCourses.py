"""
Filtering Out The Most Popular Courses For PyTec LMS
Taking Action On Other Courses To Make It Better
To Be Used In PyTec LMS Project
"""

# Mimicing Courses Database (Name, Ratings)
courses_db = [("Learn Python By Building Real World Projects", 9), ("Automate The Boring Stuff With Python", 10), ("Learn ML By Building Real World Projects", 8.2), ("Learn PyGame By Building Real World Projects", 2.5), ("Why Git & Github?", 3.2)]

# Function: Course Rating Filter
def course_rating_filter(courses, max_rating):

    # Creating A List Of Filtered Courses
    filtered_courses = []

    for course in courses:
        if course[1] >= max_rating:
            filtered_courses.append(course[0])

    return filtered_courses

# Main Program
if __name__ == "__main__":
    user_choice_rating = int(input("Enter Your Rating Choice (1 ~ 10): "))

    print("Most Popular Courses Nowadays: ", course_rating_filter(courses_db, user_choice_rating))