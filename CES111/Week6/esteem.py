question_1_2_4_6_7_value_count = 0
question_3_5_8_9_10_value_count = 0

def main():
    print("For each of the questions asked please respond with A for strongly agree, a for agree, D for strongly disagree and d for disagree.")
    print("")
    total_count_positive = 0
    total_count_negative = 0
    question_1 = input("I feel that I am a person of worth, at least on an equal plane with others. ")
    total_count_positive += question_1_2_4_6_7(question_1)
    question_2 = input("I feel that I have a number of good qualities. ")
    total_count_positive += question_1_2_4_6_7(question_2)
    question_3 = input("All in all, I am inclined to feel that I am a failure.")
    total_count_negative += question_3_5_8_9_10(question_3)
    question_4 = input("I am able to do things as well as most other people.")
    total_count_positive += question_1_2_4_6_7(question_4)
    question_5 = input("I feel I do not have much to be proud of. ")
    total_count_negative += question_3_5_8_9_10(question_5)
    question_6 = input("I take a positive attitude toward myself. ")
    total_count_positive += question_1_2_4_6_7(question_6)
    question_7 = input("On the whole, I am satisfied with myself. ")
    total_count_positive += question_1_2_4_6_7(question_7)
    question_8 = input("I wish I could have more respect for myself. ")
    total_count_negative += question_3_5_8_9_10(question_8)
    question_9 = input("I certainly feel useless at times. ")
    total_count_negative += question_3_5_8_9_10(question_9)
    question_10 = input("At times I think I am no good at all. ")
    total_count_negative += question_3_5_8_9_10(question_10)
    final_score = total_count_positive - total_count_negative
    print(f"Your score is {final_score}. A score below 15 may indicate problematic low self-esteem.")
    return final_score

def question_1_2_4_6_7(user_response_to_question):
    if user_response_to_question == "A":
        value_of_qeustion = 3
    elif user_response_to_question == "a":
        value_of_qeustion = 2
    elif user_response_to_question == "D":
        value_of_qeustion = 0
    elif user_response_to_question == "d":
        value_of_qeustion = 1
    updated_total = question_1_2_4_6_7_value_count + value_of_qeustion
    return updated_total

def question_3_5_8_9_10(user_response_to_question):
    if user_response_to_question == "A":
        value_of_qeustion = 0
    elif user_response_to_question == "a":
        value_of_qeustion = 1
    elif user_response_to_question == "D":
        value_of_qeustion = 3
    elif user_response_to_question == "d":
        value_of_qeustion = 2
    updated_total = question_3_5_8_9_10_value_count + value_of_qeustion
    return updated_total

main()