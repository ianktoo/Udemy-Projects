# The idea here is to calculate number of courses and units left
# based on the number of courses the student has taken and the numbers of semesters

'''
Example:
    You are a university student enrolled in a program.
    You want know how many units you have left
    you know the duration of your course and how many semesters you have completed
    And how many semesters per course.


'''

class MyMajor:
    """
    Attributes:
        course_duration (int): The course duration in years
        number_of_semester (int): The number of semesters per year.
        target_units (int): The number of units you are required to complete.
    """
    def __init__(self,
                 course_duration = 2,
                 number_of_semester = 3,
                 target_units = 36,
                 units_per_course = 3,
                 extra_units=0,
                 completed_semesters=0,
                 program_name='Computer Science'):
        # Initialize
        self.course_duration = course_duration
        self.number_of_semester = number_of_semester
        self.total_courses = target_units / units_per_course
        self.target_units = target_units
        self.units_per_course = units_per_course
        self.total_semesters = number_of_semester * course_duration
        self.completed_semesters = completed_semesters


    def remaining_units(self, courses_completed):
        """
        This function calculates the remaining units needed to complete a program.
        This class makes assumptions

        :exception TypeError: If courses_completed is negative.
        :param courses_completed: Specify the number of courses completed.
        :return: Number of units needed to complete a program
        """
        if not isinstance(courses_completed, int):
            raise TypeError('Courses completed must be a number')

        if courses_completed > self.total_courses or courses_completed < 0:
            raise ValueError(f'Invalid number of coursed completed. '
                             f'Must be 0 or less that or equal to {self.total_courses}')
        return self.target_units - (courses_completed * self.units_per_course)


    def remaining_semesters(self):
        return self.total_semesters - self.completed_semesters

    def __str__(self):
        return(f'Courses completed: {self.total_courses}\n'
              f'Remaining semesters: {self.remaining_semesters()}')


cs = MyMajor(completed_semesters=2)
print(cs.remaining_units(4), 'remaining units.')
print(cs.__str__())