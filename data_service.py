"""модуль призначено для роботи з файлами вхідних данних"""



def get_dovidniks():
    """повертає список показників рядків балансу з файла 'dovidnik.txt'
    
    Returns:
        dovidniks_list : список показників рядків балансу
    """
    
    with open('./data/dovidnik.txt', encoding='utf-8') as dovidnik_file:
        from_file = dovidnik_file.read().splitlines()
    
    #накопичування елеменів довідника
   
    dovidniks_list = []

    for line in from_file:
        line_list = line.split(';')
        dovidniks_list.append((line_list))
    
    return dovidniks_list
   
def get_pokazniky():
    """повертає список балансу підприємства з файла 'pokaznik.txt' 
    
    Returns:
        pokazniky_list : список балансу підприємства 
    """

    with open('./data/pokaznik.txt', encoding='utf-8') as pokaznik_file:
        from_file = pokaznik_file.readlines()

    #накопичувач балансу підприємства

    pokazniky_list = []

    for line in from_file:
        line_list = line.split(';')
        pokazniky_list.append(line_list)
    
    return pokazniky_list

def show_dovidniks(dovidniks):
    """виводить елементи довідника на екран

    Args:
        dovidniks (list): список елементів
    """

    kol_lines = 0

    for dovidnik in dovidniks:
            print("Код рядка:{:3} Показник:{:30}" .format(dovidnik[0], dovidnik[1]))
            kol_lines +=1

        
def show_pokazniky(pokazniky):
    """виводить показники балансу підприємства на екран

    Args:
        pokazniky (list): список балансу підприємства
    """


    kol_line = 0

    for pokaznik in pokazniky:
            print("Підрозділ банку:{:5} Код рядку балансу:{:5} На початок 1 кв:{:5} На початок 2 кв:{:5} На початок 3 кв:{:5} На початок 4 кв:{:5} На кінець року:{:5}".format(pokaznik[0], pokaznik[1], pokaznik[2], pokaznik[3], pokaznik[4], pokaznik[5], pokaznik[6]))
            kol_line +=1
  
        
        
#dovidniks = get_dovidniks()
#show_dovidniks(dovidniks)

#pokazniky = get_pokazniky()
#show_pokazniky(pokazniky)