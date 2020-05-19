from datetime import datetime
import math

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def calculate_total(start, end):
    
    FIXED_TAX = 0.36
    DAYTIME_TAX = 0.09
    DAYTIME_START = 6
    DAYTIME_END = 22

    diff = (end - start).total_seconds() // 60

    # Se o horário de início da ligação estiver entre 6h e 22h, calcular a conta utilizando a taxa diurna
    if DAYTIME_START <= start.hour < DAYTIME_END:

        # Caso o horário final da ligação for maior que 22h, a conta será calculada apenas do início 
        # da ligação até as 22h
        if end.hour > DAYTIME_END:
            end = datetime(end.year, end.month, end.day, DAYTIME_END)

        timeDiff = end - start
        minutes = timeDiff.total_seconds() // 60

        return (minutes * DAYTIME_TAX) + FIXED_TAX

    # Se a ligação for apenas noturna, retornar a taxa permanente apenas
    else:
        return FIXED_TAX


def classify_by_phone_number(records):
    
    answer = []
    dict_record = {}
    total = 0

    # A lista de entrada foi ordenada para que os registros com o campo "source" iguais fiquem agrupados
    ordered_records = sorted(records, key=lambda k: k['source'])
    source = ordered_records[0]['source']

    for record in ordered_records:

        start = datetime.fromtimestamp(record['start'])
        end = datetime.fromtimestamp(record['end'])

        total_record = calculate_total(start, end)

        if record['source'] == source:
            total += total_record
                
        else:
            dict_record = {'source': source, 'total': round(total, 2)}
            answer.append(dict_record)
            source = record['source']
            total = total_record

    dict_record = {'source': source, 'total': round(total, 2)}
    answer.append(dict_record)

    answer = sorted(answer, key=lambda k: k['total'], reverse=True)
    
    return answer
