import pandas as pd

def coletar_dados():
    print("Digite os dados separados por vírgula (Nome, Idade, Alimentos Favoritos, Consumo Semanal). Exemplo:")
    print("Ana,25,Pizza,3\nBruno,30,Sushi,5\nCarla,28,Chocolate,2\nDavi,22,Lasanha,4\nElena,27,Churrasco,6")
    print("\nDigite os dados (um por linha) e digite 'fim' para finalizar:")

    dados_lista = []
    while True:
        entrada = input()
        if entrada.lower() == 'fim':
            break
        partes = entrada.split(",")
        if len(partes) == 4:  # Agora esperamos Nome, Idade, Alimentos e Consumo Semanal
            dados_lista.append(partes)
        else:
            print("Entrada inválida! Certifique-se de seguir o formato: Nome, Idade, Alimentos Favoritos, Consumo Semanal")

    # Criar DataFrame
    colunas = ["Nome", "Idade", "Alimentos_Favoritos", "Consumo_Semanal"]
    dados = pd.DataFrame(dados_lista, columns=colunas)

    return dados

def analisar_habitos(dados):
    try:
        # Converter Idade e Consumo_Semanal para números
        dados["Idade"] = pd.to_numeric(dados["Idade"], errors="coerce")
        dados["Consumo_Semanal"] = pd.to_numeric(dados["Consumo_Semanal"], errors="coerce")

        # Calcular a média de idade
        media_idade = dados["Idade"].mean()
        print(f"\nMédia de idade: {media_idade:.2f} anos")

        # Encontrar o alimento mais consumido (baseado na soma de consumo semanal)
        alimento_mais_consumido = dados.groupby("Alimentos_Favoritos")["Consumo_Semanal"].sum().idxmax()
        print(f"\nAlimento mais vezes consumido na semana: {alimento_mais_consumido}")

        # Exibir a tabela de dados estilo DataFrame
        print("\nTabela de dados:")
        print(dados)

    except Exception as e:
        print(f"Erro ao analisar os dados: {e}")

# Executar a coleta e análise
dados_coletados = coletar_dados()
analisar_habitos(dados_coletados)
