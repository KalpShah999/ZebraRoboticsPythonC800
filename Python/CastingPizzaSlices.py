totalNumberOfSlices = (int)(input("Enter the TOTAL number of slices: "))
numberOfStudent = (int)(input("Enter the TOTAL number of students: "))
numberOfSlicesPerStudent = totalNumberOfSlices // numberOfStudent
slicesLeftOver = totalNumberOfSlices % numberOfStudent
print("Each student will get " + (str)(numberOfSlicesPerStudent) + " slices, and there will be " + (str)(slicesLeftOver) + " slices left over.")