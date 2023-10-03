import pandas as pd
import os

def limpar_tela():
    print("\nPressione Enter para limpar a tela.")
    input()
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

vendas_df = pd.read_excel("Vendas.xlsx")
gerentes_df = pd.read_excel("Gerentes.xlsx")
vendas_df = vendas_df.merge(gerentes_df)


vendas = vendas_df[['Produto', 'Quantidade']].groupby('Produto').sum()
vendas_ordenados = vendas.sort_values(by='Quantidade', ascending=False)
maior_vendas = vendas_ordenados.head(5)
menor_vendas = vendas_ordenados.tail(5)

faturamentos = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum()
faturamentos_ordenados = faturamentos.sort_values(by='Valor Final', ascending=False)
maior_faturamentos = faturamentos_ordenados.head(5)
menor_faturamentos = faturamentos_ordenados.tail(5)


gerente_vendas = vendas_df[['Gerente', 'Quantidade']].groupby('Gerente').sum()
gerente_vendas_ordenados = gerente_vendas.sort_values(by='Quantidade', ascending=False)
gerente_maior_vendas = gerente_vendas_ordenados.head(5)
gerente_menor_vendas = gerente_vendas_ordenados.tail(5)


gerente_faturamentos = vendas_df[['Gerente', 'Valor Final']].groupby('Gerente').sum()
gerente_faturamentos_ordenados = gerente_faturamentos.sort_values(by='Valor Final', ascending=False)
gerente_maior_faturamentos = gerente_faturamentos_ordenados.head(5)
gerente_menor_faturamentos = gerente_faturamentos_ordenados.tail(5)


print("\nProdutos mais vendidos...\n\n", maior_vendas)
limpar_tela()
print("\nProdutos menos vendidos...\n\n", menor_vendas)
limpar_tela()
print("\nProdutos com maior faturamento...\n\n", maior_faturamentos)
limpar_tela()
print("\nProdutos com menor faturamento...\n\n", menor_faturamentos)
limpar_tela()
print("\nGerentes com mais vendas...\n\n", gerente_maior_vendas)
limpar_tela()
print("\nGerentes com menos vendas...\n\n", gerente_menor_vendas)
limpar_tela()
print("\nGerentes com mais faturamento...\n\n", gerente_maior_faturamentos)
limpar_tela()
print("\nGerentes com menos faturamento...\n\n", gerente_menor_faturamentos)
limpar_tela()

