import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Função para registrar o rendimento e as despesas
def registrar_dados():
    # Obter o rendimento mensal
    rendimento = float(input("Informe o valor que você ganha por mês: "))

    # Lista para armazenar as despesas
    despesas = []

    while True:
        # Perguntar o nome e valor da despesa
        nome_despesa = input("Informe o nome da despesa (ou 'sair' para finalizar): ")
        if nome_despesa.lower() == 'sair':
            break
        valor_despesa = float(input(f"Informe o valor de '{nome_despesa}': "))
        
        # Adicionar a despesa à lista
        despesas.append({'Nome da Despesa': nome_despesa, 'Valor da Despesa': valor_despesa})
    
    # Criar DataFrame para salvar os dados
    df = pd.DataFrame(despesas)
    df['Rendimento'] = rendimento

    # Salvar a planilha em CSV
    data_atual = datetime.datetime.now().strftime("%Y-%m")
    df.to_csv(f'planilha_gastos_{data_atual}.csv', index=False)
    print(f"Planilha de gastos salva como 'planilha_gastos_{data_atual}.csv'")

    return df, rendimento

# Função para exibir o gráfico de despesas
def exibir_grafico(despesas_df):
    plt.figure(figsize=(10, 6))
    plt.bar(despesas_df['Nome da Despesa'], despesas_df['Valor da Despesa'], color='teal')
    plt.xlabel("Despesas")
    plt.ylabel("Valor (R$)")
    plt.title("Gráfico de Despesas do Mês")
    plt.xticks(rotation=45)
    plt.show()

# Função para gerar o relatório geral
def gerar_relatorio(despesas_df, rendimento):
    total_despesas = despesas_df['Valor da Despesa'].sum()
    saldo_final = rendimento - total_despesas

    print("\n--- Relatório Geral ---")
    print(f"Rendimento mensal: R$ {rendimento:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")
    print(f"Saldo final: R$ {saldo_final:.2f}")

    if not despesas_df.empty:
        maior_despesa = despesas_df.loc[despesas_df['Valor da Despesa'].idxmax()]
        print(f"Maior despesa: {maior_despesa['Nome da Despesa']} - R$ {maior_despesa['Valor da Despesa']:.2f}")

# Executar as funções
despesas_df, rendimento = registrar_dados()
exibir_grafico(despesas_df)
gerar_relatorio(despesas_df, rendimento)
