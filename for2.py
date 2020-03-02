#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

def main():

    school = [
        {'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '4b', 'scores': [5,4,3,4,4]},
        {'school_class': '4c', 'scores': [5,3,5,5,5]},
    ]
    print(school[0]['scores'])

    scores_sum0 = 0
    for score in school[0]['scores']:
        scores_sum0 += score
    scores_avg0 = scores_sum0 / len(school[0]['scores'])
    print(f"Средняя оценка {scores_avg0}")

    scores_sum1 = 0
    for score in school[1]['scores']:
        scores_sum1 += score
    scores_avg1 = scores_sum1 / len(school[1]['scores'])
    print(f"Средняя оценка {scores_avg1}")

    scores_sum2 = 0
    for score in school[2]['scores']:
        scores_sum2 += score
    scores_avg2 = scores_sum2 / len(school[2]['scores'])
    print(f"Средняя оценка {scores_avg2}")

    scores_avg_all = (scores_avg0 + scores_avg1 + scores_avg2) / len(school)
    print(scores_avg_all)

if __name__ == "__main__":
    main()