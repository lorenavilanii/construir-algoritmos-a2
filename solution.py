import datetime
import requests


def cotar():
    cotacoes = []
    dia = datetime.date.today()

    for i in range(365):
        data = dia - datetime.timedelta(days=i)
        data_formatada = data.strftime("%m-%d-%Y")

        url = (
            "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
            "CotacaoDolarDia(dataCotacao=@dataCotacao)"
            f"?@dataCotacao='{data_formatada}'&$format=json"
        )

        
