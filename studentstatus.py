
student_status = input("Enter student status (True/False): ").casefold() == "true"
print("\nStatus is: student!" if student_status else "\nStatus is: not student!")
