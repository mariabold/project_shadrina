import random

def get_random_quiz_questions(questions_list, number_of_questions):
    """
    Функция возвращает заданное число случайных уникальных вопросов с 4 возможными ответами из списка.
    """
    if len(questions_list) < number_of_questions:
        raise Exception('В списке недостаточно вопросов для выбора 8 уникальных.')
    selected_questions = random.sample(questions_list, number_of_questions)

    return selected_questions


def check_answer(question, user_answer):
    """
    Функция проверяет, является ли ответ правильным для переданного вопроса.
    """
    is_answer_correct = user_answer == str(question['correct_answer'])

    return is_answer_correct


def ask_question(question):
    """
    Функция выводит текст вопроса в консоль, ожидает ответа пользователя и возвращает ответ.
    """
    print(f'\nКому принадлежит цитата \"{question["question"]}"')
    for i, answer in enumerate(question['answers']):
        print(f'{i+1}. {answer}')
    print('\nНапишите ответ цифрой от 1 до 4:')
    user_answer = input()
    return user_answer


def check_max_score(user_score, max_score):
    """
    Функция проверяет, достиг ли пользователь максимального счета.
    """
    is_max_score_reached = user_score == max_score

    return is_max_score_reached
