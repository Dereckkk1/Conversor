import requests

def obter_taxa_de_cambio(origem, destino):
    """Consulta a taxa de câmbio entre duas moedas usando a AwesomeAPI"""
    url = f"https://economia.awesomeapi.com.br/json/last/{origem}-{destino}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        raise Exception("Erro ao consultar taxa de câmbio.")

    dados = resposta.json()
    par = f"{origem}{destino}"
    return float(dados[par]["bid"])

def converter_moeda(valor, origem, destino):
    """Converte um valor de uma moeda para outra"""
    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero.")

    taxa = obter_taxa_de_cambio(origem, destino)
    return valor * taxa

def main():
    print("=== Conversor de Moedas ===")
    try:
        valor = float(input("Informe o valor a ser convertido: "))
        origem = input("Moeda de origem (ex: USD): ").upper()
        destino = input("Moeda de destino (ex: BRL): ").upper()

        resultado = converter_moeda(valor, origem, destino)
        print(f"{valor:.2f} {origem} equivale a {resultado:.2f} {destino}")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
