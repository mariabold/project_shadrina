import atexit

from helpers import get_random_quiz_questions, ask_question, check_answer, check_max_score
from questions import question_list


# Конфигурация - количество вопросов для квиза.
NUMBER_OF_QUESTIONS = 10
# Счет, который надо набрать за игру.
MAX_SCORE = 7

def main():
    # Переменная для сохранения состояния счета.
    score = 0
    # Выбираем N случайных цитат.
    questions = get_random_quiz_questions(question_list, NUMBER_OF_QUESTIONS)

    print(f'\nВам будет предложено {NUMBER_OF_QUESTIONS} вопросов. Ваша задача дать как минимум {MAX_SCORE} правильных ответов.\n')

    # Для каждого из вопросов выводим текст с цитатой и сверяем ответ.
    for i, question in enumerate(questions):
        print(f'Ваш счет: {score}.\nВопрос №{i+1}')
        user_answer = ask_question(question)

        # Если ответ правильный, добавляем 1 балл ко счету.
        if check_answer(question, user_answer):
            score = score + 1

        # Проверяем, если пользователь уже достиг максимального счета.
        if check_max_score(score, MAX_SCORE):
            print('Поздравляю, вы выиграли!\n')
            break

        # Если уже последний вопрос, и максимальный счет еще не достигнут.
        if i == len(questions) - 1:
            print('Сожалею, вы проиграли!\n')
            user_input = input("Хотите повторить?  (y/n): ")

            # Если пользователь хочет начать заново, запускаем функцию сначала.
            if user_input.lower() == "y":
                main()
            else:
                break


@atexit.register
def goodbye():
    """
    Обработчик выхода из программы.
    """
    print('\nСпасибо за игру и до новых встреч!')


if __name__ == "__main__":
    main()
