if __name__ == '__main__':
    if __name__ == '__main__':
        list_of_dicts = list()

        for i in range(2):
            d = dict()

            d['Фамилия и инициалы'] = input("Введите ФИО: ")
            d['Номер группы'] = int(input("Введите номер группы: "))
            d['Успеваемость'] = list(map(int, input("Введите оценки: ").split()))

            list_of_dicts.append(d)

        list_of_dicts = sorted(list_of_dicts, key=lambda x: x["Фамилия и инициалы"])

        is_find = False

        for item in list_of_dicts:
            if item['Успеваемость'].__contains__(2):
                print(f'Двоишники:\n {item["Фамилия и инициалы"]}\nГруппа: {item["Номер группы"]}\n\n')
                is_find = True

        if not is_find:
            print("Нет двоишников!")