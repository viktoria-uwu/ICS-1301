"""розрахунок аналізів середніх ринкових цін на основні продуктів споживчого кошика
"""

from data_service import get_dovidniks, get_pokazniky

#накопичувач аналізів ринкових цін
analiz = {
    'balance_name' : '',         # назва підрозділу балансу
    'pokaznik' : '',             # показник
    'beginning_year' : 0.0 ,     # на початок року
    'beginning2_sum' : 0.0 ,     # на початок 2 кв. сума, т.грн
    'beginning2_temp' : 0.0 ,    # на початок 2 кв. темп росту %
    'beginning3_sum' : 0.0 ,     # на початок 3 кв. сума, т.грн
    'beginning3_temp' : 0.0 ,   # на початок 3 кв. темп росту %
    'beginning4_sum' : 0.0 ,    # на початок 4 кв. сума, т.грн
    'beginning4_temp' : 0.0 ,   # на початок 4 кв. темп росту %
    'end_year_sum' : 0.0 ,      # на кінець року сума, т.грн
    'end_year_temp' : 0.0 ,     # на кінець року темп росту %
}

def create_analiz_list():
    """формування списку аналізу даних по підприємству на основі вхідних файлів
    """

    def get_balance_name(balance_code):
        """повертає назву підприємства по його коду

        Args:
            balance_code ([type]): код підприємства
        """
        
        for dovidnik in dovidniks:
            if int(balance_code) == int(dovidnik[0]):
                return dovidnik[1]
        
        return 'назва не знайдена'

    analiz_list = []

    dovidniks = get_dovidniks()
    pokazniky = get_pokazniky()

    #послідовна обробка рядків масиву 'pokazniky'
    for pokaznik in pokazniky:

        analiz_work = analiz.copy()

        analiz_work['balance_name'] = pokaznik[0]
        analiz_work['pokaznik'] = get_balance_name(pokazniky[1])
        analiz_work['beginning_year'] = pokaznik[2]
        analiz_work['beginning2_sum'] = pokaznik[3]
        analiz_work['beginning2_temp'] = int(analiz_work['beginning2_sum']) / int(analiz_work['begininng_year']) * 100
        analiz_work['beginning3_sum'] = pokaznik[4]
        analiz_work['beginning3_temp'] = int(analiz_work['beginning3_sum']) / int(analiz_work['begininng_year']) * 100
        analiz_work['beginning4_sum'] = pokaznik[5]
        analiz_work['beginning4_temp'] = int(analiz_work['beginning4_sum']) / int(analiz_work['begininng_year']) * 100
        analiz_work['end_year_sum'] = pokaznik[6]
        analiz_work['end_year_temp'] = int(analiz_work['end_year_temp']) / int(analiz_work['begininng_year']) * 100

        analiz_list.append(analiz_work)

    return analiz_list

    