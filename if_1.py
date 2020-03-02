def main():
    age = int(input("Введите Ваш возраст: "))   
    if age < 7:
        print ("Вы учитесь в детском саду")
    elif 7 <= age <= 17:
        print ("Вы учитесь в школе")
    elif 17 < age <= 24:
        print ("Вы учитесь в ВУЗе")
    else:
        print ("Вы работаете")

if __name__ == "__main__":
    main()