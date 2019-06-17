
from Grades_fun import average
from Grades_fun import median
from Grades_fun import variation
from Grades_fun import deviation


def main():

    subject = ['polski', 'angielski', 'fizyka']
    list_of_grades = []

    grade = None
    print('Write 0 to finish the entering of grades')
    while grade != 0:

        try:

            grade = float(input('Input grade from 1 to 6: '))

            if (grade > 0 and grade < 7):

                list_of_grades.append(float(grade))

            elif grade == 0:

                break

            else:

                print('Wrong grade, try again')

        except ValueError:
            print('Wrong data')

    print('koniec')

    print(list_of_grades)
    print('Average of grades is: {}'.format(round(average(list_of_grades)), 2))
    print('Median of grades is: {}'.format(median(list_of_grades)))
    print('Variation of grades is: {}'.format(round(variation(list_of_grades, average(list_of_grades)), 2)))
    print('Standard Deviation of grades is: {}'.format(round(deviation(list_of_grades, (variation(list_of_grades, average(list_of_grades)))), 2)))


main()