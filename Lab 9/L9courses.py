#
#   purpose: provide a course catalog that contains the course number, time, room, and instructor
#   author: zachary morrison
#   date written: 12/09/2020
#   Version: 1.0.0
#

#   creating dictionaries
classes = ("CS101", "CS102", "CS103", "NT110", "CM241")
rooms = {
    classes[0]: 3004,
    classes[1]: 4501,
    classes[2]: 6755,
    classes[3]: 1244,
    classes[4]: 1411
}
instructors = {
    classes[0]: "Haynes",
    classes[1]: "Alvarado",
    classes[2]: "Rich",
    classes[3]: "Burke",
    classes[4]: "Lee"
}
times = {
    classes[0]: "8:00am",
    classes[1]: "9:00am",
    classes[2]: "10:00am",
    classes[3]: "11:00am",
    classes[4]: "11:00pm"
}


def find_course_info():
    going = True
    count = 0
    while (going and count < 3):
        name = str(
            input("enter the course key for which you'd like information: "))
        if name in classes:
            print("Class: " + classes[classes.index(name)] + "\nRoom: " + str(
                rooms[name]) + "\nInstructor: " + instructors[name] + "\nTime: " + times[name] + "\n")
            going = False
        else:
            print("It looks like the course number that you entered doesn't belong to any courses in our catalog... try again!\n")
            going = True
            count += 1
        if count == 3:
            print("You have entered an incorrect value too many times. Bye!!!")


print("Welcome to the course catalog!\n==============================\n")
find_course_info()
