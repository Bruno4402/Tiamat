![Ilum Escola de Ciência, CNPEM](https://pages.cnpem.br/workshopbioimagens/wp-content/uploads/sites/166/2023/06/logo-ilum.png)


<h1 align="center">Tiamat</h1>

**Nome:** Bruno Bini Camargo  | **Turma:** T26 <br>
**Instituição:** Ilum Escola de Ciência, CNPEM, Campinas

Repositório para armazenar a entrega do Tiamat, projeto final da disciplina de Aprendizado de Máquina, do 2° semestre do curso de Ciência e Tecnologia na Ilum.

<p align="center">
  <img src="Brasão%20da%20Casa%20Onurb.png" alt="Brasão da Casa Onurb" width="300">
</p>

## 🚀 Sobre o projeto

Este projeto utiliza dados do ranking das melhores 500 escolas no ENEM 2025 para investigar a capacidade de diferentes algoritmos de Aprendizado de Máquina em prever a média nacional (com redação). Foram avaliados modelos lineares, baseados em vizinhos e baseados em árvores, incluindo Regressão Linear, Lasso, Ridge, k-NN, Árvore de Decisão, Floresta Aleatória e Gradient Boosting.

Além da comparação tradicional por divisão treino-teste, também foram empregadas técnicas de validação cruzada, otimização de hiperparâmetros com Optuna e análise de interpretabilidade por meio de Permutation Importance.

---

## 📈 Principais resultados

- O Gradient Boosting foi selecionado como modelo final após apresentar o menor RMSE entre todos os algoritmos avaliados.
- Modelos baseados em árvores superaram consistentemente modelos lineares e o k-NN.
- A validação cruzada confirmou a robustez e a capacidade de generalização do modelo selecionado.
- A técnica de Permutation Importance revelou que indicadores de desempenho acadêmico foram muito mais relevantes para as previsões do que variáveis relacionadas à localização geográfica das escolas.

---

## :open_file_folder: Arquivos do repositório

* :page_facing_up: **.gitignore**: Contém informações para ignorar arquivos desnecessários no Git.
* :memo: **Tiamat.ipynb**: Contém o notebook Jupyter do projeto.
* 💹 **Enem_Acompanhamento_de_escolas_2025.xlsx**: Contém dataset utilizado no projeto.
* :balance_scale: **LICENSE**: Contém informações da licença desse projeto, a GNU General Public License v2.0.
* :book: **README.md**: Contém a documentação principal do projeto.
* :open_file_folder: **gradient_boosting_hpc/**: Pasta que contém os scripts e arquivos de configuração para a execução do modelo de Gradient Boosting usando recursos de Computação de Alto Desempenho (HPC).
    * :page_facing_up: **gb_19966.out**: Arquivo de log com o resultado e a saída gerada pela execução do job no cluster.
    * :page_facing_up: **gradient_boosting_optuna.py**: Script Python que executa o treinamento do Gradient Boosting utilizando o Optuna para a otimização de hiperparâmetros.
    * :page_facing_up: **job_gb.sh**: Script de shell (Bash) utilizado para submeter e gerenciar a execução do trabalho do Gradient Boosting no cluster HPC.
    * :page_facing_up: **trials_gradient_boosting_csv**: Arquivo estruturado que armazena o histórico e os resultados de cada tentativa (trial) do Gradient Boosting realizada pelo Optuna.
* :open_file_folder: **random_forest_hpc/**: Pasta que contém os scripts e arquivos de configuração para a execução do modelo Floresta Aleatória em ambiente de Computação de Alto Desempenho (HPC).
    * :page_facing_up: **job_rf.sh**: Script de shell (Bash) utilizado para submeter e gerenciar a execução do trabalho da Floresta Aleatória no cluster HPC.
    * :page_facing_up: **random_forest_optuna.py**: Script Python que executa o treinamento da Floresta Aleatória utilizando o Optuna para a otimização de hiperparâmetros.
    * :page_facing_up: **rf_19963.out**: Arquivo de log com o resultado e a saída gerada pela execução do job no cluster.
    * :page_facing_up: **trials_random_forest.csv**: Arquivo estruturado que armazena o histórico e os resultados de cada tentativa (trial) da Floresta Aleatória realizada pelo Optuna.
 
---

## 🖥️ Ferramentas usadas no projeto

- **Jupyter Lab** para desenvolvimento do código.
  - **Módulos** utilizados em Python: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn e Optuna.
- **IA** para resolução de dúvidas de sintaxe, correção de bugs e lógicas dos modelos, auxílio na elaboração de gráficos complexos, uso do HPC e análise diagnóstica da atividade, indicando melhorias.

---

## ▶️ Como executar

### Requisitos

- Python 3.11 ou superior
- Ambiente de execução de Notebooks (VS Code, JupyterLab, Jupyter Notebook, etc.)
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Optuna

### Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO> **mudar isso depois de deixar público**
cd Tiamat
```

Instale as dependências necessárias:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn optuna
```

### Execução

1. Abra o arquivo `Tiamat.ipynb` na sua IDE de preferência.
2. Certifique-se de selecionar o kernel do Python onde as dependências foram instaladas.
3. Execute as células sequencialmente para reproduzir os resultados apresentados no trabalho.

---

## ⚡ Uso do cluster Heisenberg

Parte deste projeto utilizou recursos de Computação de Alto Desempenho (*High Performance Computing* – HPC) por meio do cluster **Heisenberg**, infraestrutura computacional disponibilizada pela Ilum Escola de Ciência para atividades acadêmicas e científicas que demandam elevado poder de processamento.

O uso do cluster foi fundamental para a otimização dos modelos de Floresta Aleatória e Gradient Boosting, possibilitando a execução de centenas de trials com validação cruzada por meio do módulo Optuna. A utilização do HPC permitiu expandir significativamente o espaço de busca dos hiperparâmetros e reduzir o tempo total necessário para a realização dos experimentos.

Os scripts utilizados nessas execuções encontram-se nos diretórios:

```text
random_forest_hpc/
gradient_boosting_hpc/
```
Essas pastas incluem scripts de treinamento, arquivos de submissão dos jobs, históricos de trials e logs completos das execuções.

---

## 📚 Fundamentação metodológica

Os conceitos teóricos, estratégias de modelagem e procedimentos metodológicos empregados neste trabalho foram fundamentados nos materiais didáticos e notebooks Jupyter disponibilizados ao longo da disciplina de Aprendizado de Máquina da Ilum Escola de Ciência, ministrada pelo Prof. Daniel Roberto Cassar, complementados pela documentação oficial das bibliotecas utilizadas e pelas referências citadas no notebook do projeto.
