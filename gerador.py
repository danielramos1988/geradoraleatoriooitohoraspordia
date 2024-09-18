import datetime
import random

class GetHour:
    # Definindo horários de início e intervalos aleatórios
    _starthours = [8, 9]  # Horários de início possíveis
    _startMinuts = [30, 45]  # Minutos de início possíveis
    _diffMinuts = [0, 15]  # Diferença de minutos aleatórios
    _defaultDay = datetime.timedelta(hours=8)  # Duração padrão do dia (8 horas)

    @staticmethod
    def get(day, month):
        # Obtém a data atual
        now = datetime.datetime.now()
        # Cria um objeto de data para o dia e mês fornecidos
        date = datetime.datetime(now.year, month, day)

        # Gera aleatoriamente a hora de início e minutos
        startHour = random.randint(GetHour._starthours[0], GetHour._starthours[1])
        starMinuts = random.randint(GetHour._startMinuts[0], GetHour._startMinuts[1])
        diffMinuts = random.randint(GetHour._diffMinuts[0], GetHour._diffMinuts[1])

        # Define o primeiro intervalo
        interval1 = datetime.datetime(date.year, date.month, date.day, startHour, starMinuts)
        # Define o segundo intervalo adicionando 4 horas e a diferença de minutos
        interval2 = interval1 + datetime.timedelta(hours=4, minutes=diffMinuts)

        # Gera nova diferença de minutos para o terceiro intervalo
        diffMinuts = random.randint(GetHour._diffMinuts[0], GetHour._diffMinuts[1])
        interval3 = interval2 + datetime.timedelta(hours=1, minutes=diffMinuts)

        # Gera nova diferença de minutos para o quarto intervalo
        diffMinuts = random.randint(GetHour._diffMinuts[0], GetHour._diffMinuts[1])
        interval4 = interval3 + datetime.timedelta(hours=4, minutes=diffMinuts)

        # Calcula o tempo total dos intervalos
        time = ((interval2 - interval1) + (interval4 - interval3))

        # Se o tempo total não for igual ao padrão, ajusta o último intervalo
        if time != GetHour._defaultDay:
            interval4 += (GetHour._defaultDay - time)

        # Recalcula o tempo total após o ajuste
        time = ((interval2 - interval1) + (interval4 - interval3))

        # Retorna a representação de string dos intervalos
        if date.weekday() == 5 or date.weekday() == 6:  # Verifica se é sábado ou domingo
            return date.strftime('%A')  # Retorna o dia da semana
        else:
            return f"{interval1.strftime('%H:%M')} - {interval2.strftime('%H:%M')} - {interval3.strftime('%H:%M')} - {interval4.strftime('%H:%M')} > {time}"

if __name__ == "__main__":
    # Solicita ao usuário o número do mês
    monthNumber = input("Enter the month number: ")
    
    # Verifica se o número do mês é válido
    if monthNumber.isdigit() and (1 <= int(monthNumber) <= 12):
        monthNumber = int(monthNumber)
        # Itera pelos dias do mês, gerando e imprimindo as horas
        for day in range(1, datetime.datetime.now().monthrange(datetime.datetime.now().year, monthNumber)[1] + 1):
            print(f"{day:02} = {GetHour.get(day, monthNumber)}")
    else:
        print("Invalid month!")  # Mensagem de erro para mês inválido
