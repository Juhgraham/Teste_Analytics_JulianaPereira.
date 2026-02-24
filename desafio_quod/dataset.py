# Simulação, Limpeza e Análise de Dados de Vendas
# Tema: Produtos de Skincare


import pandas as pd 
import numpy as np 
import random
from datetime import datetime, timedelta


# Cria o dataset

mapa_produtos = {
    "Hidratante Facial": "Hidratação",
    "Protetor Solar": "Proteção",
    "Sérum Vitamina C": "Tratamento",
    "Gel de Limpeza": "Limpeza",
    "Ácido Hialurônico": "Tratamento",
    "Tônico Facial": "Limpeza"
}

lista_produtos = list(mapa_produtos.keys())

# Função que gera datas aleatórias em 2023
def gerar_data_aleatoria():
    data_inicio = datetime(2023, 1, 1)
    data_fim = datetime(2023, 12, 31)
    delta = data_fim - data_inicio
    dias_aleatorios = random.randint(0, delta.days)
    return data_inicio + timedelta(days=dias_aleatorios)

# Cria registros (como vai ficar o dataset)
dados = []

for i in range(50):

    produto_escolhido = random.choice(lista_produtos)
    
    registro = {
        "ID": i + 1,
        "Data": gerar_data_aleatoria(),
        "Produto": produto_escolhido,
        "Categoria": mapa_produtos[produto_escolhido],
        "Quantidade": random.randint(1, 8),
        "Preço": round(random.uniform(30, 250), 2)
    }
    
    dados.append(registro)

# Criando DataFrame
df = pd.DataFrame(dados)

# Inserindo valores faltantes propositalmente
df.loc[3, "Preço"] = np.nan
df.loc[12, "Quantidade"] = np.nan

# Inserindo duplicata propositalmente
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)



# Limpeza dos dados


# Remover duplicatas
df = df.drop_duplicates()

# Tratamento de valores faltantes
df["Quantidade"] = df["Quantidade"].fillna(df["Quantidade"].median())
df["Preço"] = df["Preço"].fillna(df["Preço"].mean())

df["Preço"] = df["Preço"].round(2)

# Conversão de tipos
df["Data"] = pd.to_datetime(df["Data"])
df["Quantidade"] = df["Quantidade"].astype(int)
df["Preço"] = df["Preço"].astype(float)


# Salva o dataset já limpo


df.to_csv("data_clean.csv", index=False, float_format="%.2f")

print("Dataset limpo salvo como data_clean.csv")


# Análise dos dados

# Criando coluna de Total de Vendas (faturamento)
df["Total_Vendas"] = df["Quantidade"] * df["Preço"]

# Total de vendas por produto(faturamento)
total_financeiro_produto = (
    df.groupby("Produto")["Total_Vendas"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal de vendas (R$) por produto:")
print(total_financeiro_produto)


# Produto com maior venda financeira
produto_maior_valor = total_financeiro_produto.idxmax()
valor_total = total_financeiro_produto.max()

print("\nProduto com maior valor total vendido:")
print(produto_maior_valor)
print(f"Valor total: R$ {valor_total:.2f}")


# Total de vendas (quantidade)
total_quantidade_produto = (
    df.groupby("Produto")["Quantidade"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal de unidades vendidas por produto:")
print(total_quantidade_produto)


# Produto com maior quantidade vendida
produto_mais_unidades = total_quantidade_produto.idxmax()
quantidade_total = total_quantidade_produto.max()

print("\nProduto com maior número de vendas (unidades):")
print(produto_mais_unidades)
print(f"Quantidade total vendida: {quantidade_total}")