
if __name__ == '__main__':
    list_of_dicts = list()

    n = int(input("Введите количество студентов: "))
    for i in range(n):
        d = dict()

        d['Фамилия и инициалы'] = input("Введите ФИО: ")
        d['Номер группы'] = int(input("Введите номер группы: "))
        d['Успеваемость'] = input("Введите оценки: ")

        list_of_dicts.append(d)

    list_of_dicts = sorted(list_of_dicts, key=lambda x: x["Фамилия и инициалы"])

    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Фамилия и инициалы",
            "Номер группы",
            "Успеваемость"
        )
    )
    print(line)

    for idx, d in enumerate(list_of_dicts, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
                d.get('Фамилия и инициалы', ''),
                d.get('Номер группы', ''),
                d.get('Успеваемость', '')
            )
        )

    print(line)

    is_find = False

    print("\nДвоишники:\n")
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Фамилия и инициалы",
            "Номер группы",
            "Успеваемость"
        )
    )
    print(line)

    idx =1
    for item in list_of_dicts:
        if 2 in list(map(int, item['Успеваемость'].split())):
            is_find = True
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    d.get('Фамилия и инициалы', ''),
                    d.get('Номер группы', ''),
                    d.get('Успеваемость', '')
                )
            )

            print(line)
            idx += 1

    if not is_find:
        print("Нет двоишников!")