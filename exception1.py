"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    while True:
        try:    
            questions = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Как тебе погода?": "Погода ужасная"}
            while True:
                user_say = input('Задай мне вопрос: ')
                if user_say == "Как дела?":
                    print(questions["Как дела?"])
                elif user_say == "Что делаешь?":
                    print(questions["Что делаешь?"])
                elif user_say == "Как тебе погода?":
                    print(questions["Как тебе погода?"])
        except KeyboardInterrupt:
            print("Пока!")   
        break
if __name__ == "__main__":
    ask_user()