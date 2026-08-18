empty_list=[]
marks_list=[95,96,97,98,99]
print(marks_list)
sample_marks=[10,20,30]*2
print(len(marks_list))
a=marks_list[0]
b=marks_list[-1]
print(f'The first number of the lits is {a} and the last no of the list is {b}')
c=marks_list[0:3]
d=marks_list[::-1]
print(f'The first three number is the list are {c} and the reverse order of the numbers are {d}')
def match_marks(mark_list):
    count = 0
    matched_marks = []
 
    for mark in mark_list:
        mark_text = str(mark)
 
    if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)
    print("Marks with first and last digit same:", matched_marks)
    return count
same_digit_count = match_marks([88, 72, 99, 65, 77])
print("Number of matching marks:", same_digit_count)
total = 0
for mark in marks:
    total += mark
average = total / len(marks)
print("Sum of marks:", total)
print("Average marks:", average)
print("Smallest mark is:", marks[0])
print("Largest mark is:", marks[-1])
print("")
print("===== STUDENT MARKS LIST ANALYZER =====")
print("Sorted Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Lowest Mark:", marks[0])
print("Highest Mark:", marks[-1])
print("=======================================")

