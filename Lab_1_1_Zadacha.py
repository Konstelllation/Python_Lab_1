if __name__ == '__main__':
    school = {'1a':20, '2b': 24, '11a': 15, '11b': 10}
    school ['2b'] = 21  # Изменение во 2b классе
    school ['2a'] = 16  # Новый класс
    del school ['11b']  # Класс был расформирован
    S = sum(school.values())
    print (school,'\n',"Общее количество учеников в школе :",S)
