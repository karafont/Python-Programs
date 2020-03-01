def getTestName():
    testName = input(
        "Please enter the name of the math test you would like to input: ")

    if testName != "ACT" and testName != "act" and testName != "SAT" and testName !=  "sat" and testName != "Accuplacer" and testName != "accuplacer":
        print("You have entered an invalid test name. Please enter either",
              "ACT, SAT, or Accuplacer.")

        testName = input(
            "Please enter the name of the math test you would like to input: ")

    return testName


def getTestScore(testName):
    testScore = float(input("Please enter the test score: "))

    if testName == "ACT" or testName == "act":
        if testScore < 1 or testScore > 36:
            print("You have entered an invalid score. ACT scores must be between",
                  "1-36. Please re-enter valid score.")

            testScore = float(input("Please enter the test score: "))

    elif testName == "SAT" or testName == "sat":
        if testScore < 200 or testScore > 800:
            print("You have entered an invalid score. SAT scores must be between",
                  "200-800. Please re-enter valid score.")

            testScore = float(input("Please enter the test score: "))

    elif testName == "Accuplacer" or testName == "accuplacer":
        if testScore < 20 or testScore > 120:
            print("You have entered an invalid score. Accuplacer scores must be between",
                  "20-120. Please re-enter valid score.")

            testScore = float(input("Please enter the test score: "))

    return testScore


def getMathCourse():

    mathCourse = input(
        "Please enter the math course number the student wants to take: ")

    if mathCourse.isdigit:
        if len(mathCourse) != 4:
            print("Error. The math course number must be four digits.")

            mathCourse = input(
                "Please enter the math course number the student wants to take: ")

    else:
        print("Error. The math course number must be four numeric digits.")

        mathCourse = input(
            "Please enter the math course number the student wants to take: ")

    return mathCourse


def needDevMath(testName, testScore):
    need_dev_math = False

    if testName == "ACT":
        if testScore < 19:
            need_dev_math = True

        elif testScore >= 19:
            need_dev_math = False

    if testName == "SAT":
        if testScore <= 450:
            need_dev_math = True

        elif testScore > 450:
            need_dev_math = False

    if testName == "Accuplacer":
        if testScore < 92:
            need_dev_math = True

        elif testScore >= 92:
            need_dev_math = False

    return need_dev_math


def ok_to_take(mathCourse):
    print("The student is cleared to take Math", mathCourse + ".")


def print_which_math(mathCourse):
    if mathCourse == "1000":
        print("The student must also take Math 0815.")

    elif mathCourse == "1010":
        print("The student must also take Math 0825.")

    elif mathCourse == "1530":
        print("The student must also take Math 0835.")

    elif mathCourse == "1630":
        print("The student must also take Math 0845.")

    else:
        print("The student is required to take a developmental math course." +
              "They are restricted from registering for MATH 1000, MATH 1010, MATH 1530, and MATH 1630.")


def main():
    testName = getTestName()
    testScore = getTestScore(testName)
    mathCourse = getMathCourse()
    need_dev_math = needDevMath(testName, testScore)
  
    if need_dev_math == False:
        ok_to_take(mathCourse)

    if need_dev_math == True:
        print_which_math(mathCourse)

main()
