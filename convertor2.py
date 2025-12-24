import requests

def api():
    url = 'https://api.exchangerate-api.com/v4/latest/BRL'
    return requests.get(url).json()['rates']

def definir():
    return input("Moeda (USD, EUR, CAD, GBP): ").upper()

def valor_brl ():
    return float(input("Digite o valor em reais: "))

def converter (valor, taxa):
    return valor * taxa

def main():
    rates = api()
    moeda = definir()
    valor = valor_brl()
    taxa = rates[moeda]
    resultado = converter(valor, taxa)
    print (resultado)
main()
