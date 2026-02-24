# PARTE 1.2: ANÁLISE EXPLORATÓRIA DE DADOS
# Objetivo: Criar visualizações e identificar padrões nos dados de vendas.

import pandas as pd
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil')

def carregar_e_preparar_dados(caminho='data_clean.csv'):
    """Carrega o dataset ."""
    df = pd.read_csv(caminho)
    df['Data'] = pd.to_datetime(df['Data'])
    
    # Recalcula o Total de Vendas 
    df['Total_Vendas'] = df['Quantidade'] * df['Preço']
    return df

def gerar_grafico_tendencia(df):
    """Cria um gráfico de linha (tendência de vendas mensal)."""

    # Agrupa pelo mês e soma o Total_Vendas
    vendas_mensais = df.resample('ME', on='Data')['Total_Vendas'].sum()
    
    # Cria o gráfico
    plt.figure(figsize=(10, 5))
    vendas_mensais.plot(kind='line', marker='o', color='navy', linewidth=2)
    
    # Personaliza o gráfico, eixo e titulo.
    plt.title('Tendência de Vendas Mensais (2023)', fontsize=14, pad=15)
    plt.xlabel('Meses do Ano', fontsize=12)
    plt.ylabel('Faturamento Total (R$)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Salva imagem
    plt.tight_layout()
    plt.savefig('tendencia_vendas_2023.png')
    print("Gráfico 'tendencia_vendas_2023.png' salvo com sucesso.")
    plt.close()

def extrair_insights_simples(df):
    """Identifica e descreve os insights."""
    
    print("\n" + "="*40)
    print("IDENTIFICAÇÃO DE INSIGHTS")
    print("="*40)
    
    # Insight 1: Produto com maior faturamento
    faturamento_produto = df.groupby('Produto')['Total_Vendas'].sum().sort_values(ascending=False)
    top_produto = faturamento_produto.index[0]
    
    print(f"Insight 1: O produto '{top_produto}' é o produto que gera o maior faturamento total no ano de 2023.")
    
    # Insight 2: Mês com mais vendas
    vendas_por_mes = df.resample('ME', on='Data')['Quantidade'].sum()
    mes_pico = vendas_por_mes.idxmax().strftime('%B')

    print(f"\nInsight 2: Observou-se um pico de demanda no mês de {mes_pico},que registrou o maior volume de unidades vendidas no período.")

    # Insight 3: Produto mais procurado (Quantidade)
    quantidade_produto = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
    top_produto_quantidade = quantidade_produto.index[0]
    print(f"\nInsight 3: Percebe-se que o produto mais procurado e vendido é o {top_produto_quantidade}', liderando o volume total de unidades.")

    # Insight 4: Mês com mais venda do Protetor Solar
    vendas_protetor = df[df['Produto'] == 'Protetor Solar']
    if not vendas_protetor.empty:
        vendas_protetor_mensal = vendas_protetor.resample('ME', on='Data')['Quantidade'].sum()
        mes_pico_protetor = vendas_protetor_mensal.idxmax().strftime('%B')
        print(f"\nInsight 4: O 'Protetor Solar' teve seu maior pico de vendas no mês de {mes_pico_protetor}, possivelmente devido a fatores climáticos.")
    
    print("="*40)

if __name__ == "__main__":
    # fluxo da execução
    try:
        dados_vendas = carregar_e_preparar_dados()
        gerar_grafico_tendencia(dados_vendas)
        extrair_insights_simples(dados_vendas)
    except Exception as e:
        print(f"Erro ao processar a análise: {e}")