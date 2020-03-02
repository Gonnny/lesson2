def main():
    s_1 = input("Введите первую строку: ")
    s_2 = input("Введите вторую строку: ")
    if type(s_1) == str and type(s_2) == str:
        print('Это строки')
    else:
        print('0')
    
    if len(s_1) == len(s_2):
        print('1')
    elif len(s_1) > len(s_2):
        print('2')
        
    if len(s_1) != len(s_2) and s_2 == 'learn':
        print('3')


if __name__ == "__main__":
    main()