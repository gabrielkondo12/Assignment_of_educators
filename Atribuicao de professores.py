import pandas as pd

# Carregar a planilha com as escolas e o número de vagas
escolas = pd.read_excel('Vagas.xlsx')

# Carregar a planilha com os professores e suas escolhas
professores = pd.read_excel('Atribuição Ordenado.xlsx')

# Criar uma coluna de vagas restantes para cada escola (Uma cópia)
escolas['vagas_restantes'] = escolas['vagas']

# Criar uma lista para armazenar os professores atribuídos
atribuidos = []

# Loop através de cada professor classificado
for i, professor in professores.iterrows():
    # Loop através das escolhas do professor
    for j, escola in enumerate(professor[['1ª opção', '2ª opção', '3ª opção']]):
        # Verificar se há vagas na escola
        if escolas.loc[escolas['escola'] == escola, 'vagas_restantes'].values[0] > 0:
            # Atribuir a escola ao professor
            atribuidos.append([i+1, professor['professor'], escola])
            # Decrementar o número de vagas restantes na escola
            escolas.loc[escolas['escola'] == escola, 'vagas_restantes'] -= 1
            # Sair do loop
            break
    # Verificar se o professor foi atribuído
    if len(atribuidos) <= i:
        # Adicionar o professor à lista de professores não atribuídos
        atribuidos.append([i+1, professor['professor'], 'Nenhuma das escolhas foi atendida'])

# Converter a lista de professores atribuídos em um DataFrame
resultados = pd.DataFrame(atribuidos, columns=['Ordem', 'Professor', 'Escola'])

# Salvar a planilha de resultados
resultados.to_excel('---------resultados----------.xlsx', index=False)



""" O método loc é um método de seleção de dados em um DataFrame do Pandas. 
Ele permite selecionar linhas de um DataFrame baseado em um critério de seleção, como por exemplo,
selecionar uma linha específica ou selecionar todas as linhas onde uma determinada condição é verdadeira. """

