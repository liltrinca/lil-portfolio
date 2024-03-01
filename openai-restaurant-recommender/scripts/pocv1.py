import seaborn as sns
import matplotlib.pyplot as plt

from datetime import datetime

def get_estabelecimentos(df, radius):
    num = df["estabelecimento"].drop_duplicates().shape[0]

    return f"Total de estabelecimentos num raio de {radius} km: {num}"

def get_ticket_medio(df):
    m = round(df["val_transacao_consumo"].mean(),2)

    return f"Valor do ticket médio: {m}"

def get_valor_mediano_tickets(df):
    M = round(df["val_transacao_consumo"].median(),2)

    return f"Valor mediano dos tickets: {M}"

def get_numero_transacoes(df):
    t = df.shape[0]
    
    return f"Numero de transações: {t}"


def get_quantidade_clientes(df):
    clientes = df["beneficiado"].drop_duplicates().shape[0]

    return f"Quantidade de clientes: {clientes}"


def plot_heatmap(df):
    fig, ax = plt.subplots(figsize=(6,5))
    df['hora'] = df.apply(lambda x: datetime.strftime(datetime.strptime(x['dat_transacao'], '%Y-%m-%dT%H:%M:%S.000Z'), '%H'), axis=1)
    df2 = df.groupby(['cd_dia_da_semana','ds_dia_da_semana','hora'], as_index=False)['val_transacao_consumo'].mean().sort_values(['cd_dia_da_semana'])
    df3 = df2.pivot_table(index='ds_dia_da_semana', columns='hora', values='val_transacao_consumo')
    df3 = df3.reindex(['Sun','Mon','Tue','Wed','Thu','Fri','Sat'])
    g = sns.heatmap(df3, annot=False, cmap='Greens')
    g.set(xlabel='Hora',ylabel='Dia da semana')

    return g


def plot_line(df):
    df_agg = df.groupby(['ds_dia_da_semana','cd_dia_da_semana'])[['val_transacao_consumo']].mean().reset_index().sort_values(['cd_dia_da_semana'])

    fig, ax = plt.subplots(figsize=(10,3))
    plt.title("Valor médio por dia da semana")
    plt.xlabel('Dia da semana')
    plt.ylabel('Valor médio')
    plt.grid(True)
    plt.plot(df_agg['ds_dia_da_semana'], df_agg['val_transacao_consumo'], linestyle = "-", color="green")

    return fig


def plot_hist(df):
    x = df['val_transacao_consumo'].tolist()
    fig, axs = plt.subplots(figsize=(5,4))

    plt.title('Distribuição de Tickets')
    plt.xlabel('Valor')
    plt.ylabel('Quantidade')
    axs.hist(x, bins = [0, max(x)/4, max(x)/3, max(x)/2, 2*max(x)/3, 3*max(x)/4, max(x)],
             edgecolor='black', linewidth=1, color='lightgreen')
    plt.grid(True)
    return fig



# # Minimo 3 estabelecimentos, baseado nas transações
# Parametrizar por km
# Rodar powercenter por chunk size