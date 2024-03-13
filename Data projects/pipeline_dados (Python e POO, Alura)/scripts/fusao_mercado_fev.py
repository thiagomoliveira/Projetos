from processamento_dados import Dados


path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extract

dados_empresaA = Dados.leitura_dados(path_json, 'json')
print('Nome das colunas na tabela da empresa A:')
print(dados_empresaA.nome_colunas)

print(f'Quantidade de linhas na tabela da empresa A: {dados_empresaA.qtd_linhas}\n')

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print('Nome das colunas na tabela da empresa B:')
print(dados_empresaB.nome_colunas)
print(f'Quantidade de linhas na tabela da empresa B: {dados_empresaB.qtd_linhas}\n')

#Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print('Nome das colunas na tabela final:')
print(dados_fusao.nome_colunas)
print(f'Quantidade de linhas na tabela final: {dados_fusao.qtd_linhas}\n')

#Load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f'O arquivo final está pronto e foi salvo no caminho: {path_dados_combinados}')

