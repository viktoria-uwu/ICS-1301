"""головний модуль додатку
виводить розрахункову таблицю, зберігає розрахунок у файл
показує на екрані первинні дані
"""

import os
from process_data import create_analiz, format_analiz
from data_service import show_dovidniks, show_pokazniky, get_dovidniks, get_pokazniky

MAIN_MENU = \
"""
~~~~~~~~~ ОБРОБКА АНАЛІЗІВ СЕРЕДНІХ РИНКОВИХ ЦІН НА ОСНОВІ ПРОДУКТІВ СПОЖИВЧОГО КОШИКА ~~~~~~~~~~

1 - вивід динаміки капіталу на екран
2 - запис результату в файл
3 - вивід показників балансу
4 - вивід довідника довідника показників балансу
0 - завершити роботу
--------------------------------------------------------------------------------------------------
"""
TITLE = "АНАЛІЗ ДИНАМІЧНИХ ОБОРОТНИХ КОШТІВ ТА ОБОРОТНОГО КАПІТАЛУ ПІДПРИЄМСТВА"
HEADER = \
'''
=============================================================================================================================================================================
|                          |          |                 |       На початок 2 кв.     |       На початок 3 кв.     |       На початок 4 кв.     |       На кінець року       | 
| Назва підрозділу балансу | Показник | На початок року |============================|============================|============================|============================|
|                          |          |                 | сума, т.грн | темп росту % | сума, т.грн | темп росту % | сума, т.грн | темп росту % | сума, т.грн | темп росту % |
=============================================================================================================================================================================
'''
FOOTER = \
'''
==============================================================================================================================================================================
'''

enter = "Для проодовження натисніть <Enter>"

def show_analiz(analiz_list):
    """виводить сформовані аналізи на екран у вигляді таблиці

    Args:
        analiz_list ([type]): список аналізів оборотних коштів та оборотного капіталу
    """
    
    print(f'\n\n{TITLE:^90}')
    print(HEADER)
    
    for analiz in analiz_list:
        print(f"{analiz['balance_name']:25}",
              f"{analiz['pokaznik']:20}",
              f"{analiz['start_year']:>15}",
              f"{analiz['beginning2_sum']:>10.2f}",
              f"{analiz['beginning2_temp']:>10.2f}",
              f"{analiz['beginning3_sum']:>11.2f}",
              f"{analiz['beginning3_temp']:>11.2f}",
              f"{analiz['beginning4_sum']:>12.2f}",
              f"{analiz['beginning4_temp']:>12.2f}",
              f"{analiz['end_year_sum']:>13.2f}",
              f"{analiz['end_year_sum']:>13.2f}"
              )
    
    print(FOOTER)


def write_analiz(analiz_list):
    """пише список аналізу даних по підприємству у файл

    Args:
        analiz_list ([type]): список аналізів
    """
    
    with open('./data/analiz.txt', "w") as analiz_file:
        for analiz in analiz_list:
            line = \
                f"{(analiz['balance_name']) + ';':20}"   + \
                f"{(analiz['pokaznik']) + ';':20}"       + \
                f"{(analiz['start_year'])  + ';':5}" + \
                f"{(analiz['beginning2_sum']) + ';':5}"  + \
                f"{(analiz['beginning2_temp']) + ';':5}" + \
                f"{(analiz['beginning3_sum']) + ';':5}"  + \
                f"{(analiz['beginning3_temp']) + ';':5}" + \
                f"{(analiz['beginning4_sum']) + ';':5}"  + \
                f"{(analiz['beginning4_temp']) + ';':5}" + \
                f"{(analiz['end_year_sum']) + ';':5}"    + \
                f"{(analiz['end_year_temp']) + ';':5}"   + '\n'
                
            analiz_file.write(line)
        
        print("Файл заявок сформовано ...")
    

while True:
    
    # вивід головного меню
    os.system('cls')
    print(MAIN_MENU)
    command_number = input(">>  Введіть номер команди: ")

    # обробка команд користувача
    if command_number == '0':
        print("\nПрограма завершила роботу")
        exit(0)
    
    elif command_number == '1':
        print(TITLE)
        print(HEADER)
        for item in create_analiz():
            print(format_analiz(item))
        print(FOOTER)
        enter = input("Для проодовження натисніть <Enter>")
    
    elif command_number == '2':
        print("Запис результату в файл...")
        analiz_list = create_analiz()
        show_analiz(analiz_list)
        enter = input("Для проодовження натисніть <Enter>")
    
    elif command_number == '3':
        pokazniky = get_pokazniky()
        show_pokazniky(get_pokazniky())
        enter = input("Для проодовження натисніть <Enter>")
    
    elif command_number == '4':
        dovidniks = get_dovidniks()
        show_dovidniks(get_dovidniks())
        enter = input("Для проодовження натисніть <Enter>")
        
