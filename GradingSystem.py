# grading_system.py

def grading_system():
    # Collect student details
    name = input("Enter student's full name: ")
    exam_score = int(input("Enter exam score: "))
    assessment_score = int(input("Enter assessment score: "))
    fee_paid = int(input("Enter fee paid (out of 100): "))

    # Initialize status
    exam_pass = exam_score >= 25
    assessment_pass = assessment_score >= 15
    total_score = exam_score + assessment_score

    # Determine outcome
    certificate = False
    condoned = False
    failed = False
    repeated = False

    # Requirement 1: Pass both components
    if exam_pass and assessment_pass:
        if fee_paid == 100:
            certificate = True

    # Requirement 2: Condoned case
    elif total_score == 39 and (exam_score >= 25 or assessment_score >= 15):
        condoned = True
        if fee_paid == 100:
            certificate = True

    else:
        failed = True
        if not exam_pass and not assessment_pass:
            repeated = True

    # Generate report
    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Exam Score: {exam_score} ({'Pass' if exam_pass else 'Fail'})")
    print(f"Assessment Score: {assessment_score} ({'Pass' if assessment_pass else 'Fail'})")
    print(f"Total Score: {total_score}")
    print(f"Fee Paid: {fee_paid}/100")

    if certificate:
        print("Outcome: Certificate issued ✅")
    elif condoned:
        print("Outcome: Student condoned (no certificate unless fees fully paid).")
    elif repeated:
        print("Outcome: Failed both components ❌ → Student repeated.")
    elif failed:
        print("Outcome: Failed ❌")
    else:
        print("Outcome: No clear status (check inputs).")

    print("-----------------------\n")


# Run program
if __name__ == "__main__":
    grading_system()
