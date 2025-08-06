import datetime
import calendar

WEEKDAYS_PT = {
    0: 'segunda',
    1: 'terça',
    2: 'quarta',
    3: 'quinta',
    4: 'sexta',
    5: 'sábado',
    6: 'domingo'
}

PERIODOS = {
    'semestral': 180,
    'anual': 360
}


def get_dia_da_semana(data):   
    return WEEKDAYS_PT[data.weekday()]


def gerar_aulas(periodo, dias, diasNaoLetivos):
    periodo_dias = PERIODOS[periodo]
    
    dataInicial = datetime.date.today()
    dataFinal = dataInicial + datetime.timedelta(days=periodo_dias)
    dataTerminoDasAulas = datetime.date(dataInicial.year, 12, 23)
    
    dataFinal = min(dataFinal, dataTerminoDasAulas)
    
    proximoDia = dataInicial

    aulas = 0
    while proximoDia <= dataFinal:
        diaSemana = get_dia_da_semana(proximoDia)
        diaStr = proximoDia.strftime('%d/%m/%Y')
        if diaSemana in dias and diaStr not in diasNaoLetivos:
            print(f'Aula: {diaStr}')
    
        proximoDia += datetime.timedelta(days=1)
        aulas += 1
    
    diaInicialStr = dataInicial.strftime('%d/%m/%Y')
    diaFinalStr = dataFinal.strftime('%d/%m/%Y')
    print(f'De {diaInicialStr} a {diaFinalStr}, têm {aulas} aulas')
    
    
if __name__ == '__main__':
    periodo = 'semestral'
    dias = {'quinta', 'sexta'}
    diasNaoLetivos = {'15/08/2025', '09/10/2025'}
    gerar_aulas(periodo, dias, diasNaoLetivos)

