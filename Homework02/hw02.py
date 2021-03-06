#Homework 2
# Won Yong Ha (woha)
# You’re working at the computer science department administrative office.
# It’s the start of the semester. New courses have been introduced along
# with the old ones and new course ids have been assigned. Your boss wants
# you to store them together.

# 1 Create two lists
course_name = ['Python', 'Java', 'C++', 'Data Structures', 'Algorithms', 'HTML', 'SQL', 'Networks']
course_id = ['B200', 'B201', 'B202', 'A200', 'A201', 'A202', 'C200', 'C201']

# 2 Using course id as key, map both lists into a dictionary named course_list.
course_list = dict()
course_list = {}
j = 0
for i in course_name:
    course_list[i] = course_id[j]
    j += 1

# Your manager wants you to print the course id against course name and post
# it on the wall for quick reference.

# 3 Print each course id with it’s course name 
print(course_list)

# Your manager wants to check if a course id is present in the dictionary.
# You are considerate. So you write a function that does it for him whenever he
# need to check if a certain id is present or not.

# 4 Write a function named key_exists() that takes in a key value as an
# argument and checks if it is present in the dictionary or not.
def key_exists(curr_key):
    for key, value in course_list.items():
        if key == curr_key:
            return True
    return False

# 5 The management decided that MongoDb is the future and so it has to be added
# to the curriculum.
course_list['C321'] = 'MongoDb'
print(course_list)

# Your manager wants to know the total number of courses that are being provided
# for this Fall semester.

# 6 Write a function to count the number of items in the dictionary. Print the 
# count.
def count_len(dict):
    return len(dict)

print(count_len(course_list))

# Your manager wants to know the list of course ids so that he does not duplicate
# a course id in the future.

# 7 Extract the keys from the dictionary[Hint: create a Set with only the keys 
# from the dictionary].Print the list of keys.
keys_list = []
for value in course_list.values():
    keys_list.append(value)
print(keys_list)

# The manager wants the list of course ids in alphabetical order.

# 8 Sort the keys_list and store it back into keys_list and print it. What
# property of sets are we manipulating here? 
keys_list = sorted(keys_list)
print(keys_list)
