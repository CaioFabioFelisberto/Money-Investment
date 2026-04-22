# 📈 Simulador de Investimentos Inteligente

Um simulador web desenvolvido em Python que permite visualizar o crescimento do patrimônio através de juros compostos, comparando diferentes modalidades de investimento e o impacto da inflação no poder de compra.

---

## 🚀 Sobre o Projeto
Este projeto foi desenvolvido para transformar cálculos financeiros complexos em visualizações interativas e fáceis de entender. O objetivo é fornecer uma ferramenta onde o usuário possa comparar o rendimento real (acima da inflação) de diversos ativos de renda fixa, visualizando não apenas o saldo final, mas a composição detalhada do seu patrimônio.

## 🛠️ Tecnologias Utilizadas

### **Backend**
* **Python 3.x**: Linguagem principal.
* **Flask**: Micro-framework web para roteamento e integração.
* **NumPy**: Processamento de dados e cálculos matemáticos vetorizados de alta performance.

### **Frontend & Visualização**
* **Plotly**: Criação de gráficos dinâmicos e interativos (Linhas, Barras e Rosca).
* **HTML5 & CSS3**: Estrutura e estilo visual.
* **GitHub Copilot**: Utilizado como assistente de IA para a geração e otimização do design CSS, garantindo uma interface moderna e responsiva.

---

## 📊 Visualizações Disponíveis

### 1. Corrida de Investimentos
Compara a evolução temporal entre a Poupança, Tesouro Selic e CDBs com taxas diferenciadas.
<img width="1901" height="937" alt="image" src="https://github.com/user-attachments/assets/acac347c-ce22-4251-bca0-10dbeaaa5665" />


### 2. Composição de Patrimônio
Um gráfico de rosca que separa o que foi **Aporte Direto** do que foi **Juros Acumulados**, evidenciando o poder do tempo sobre o dinheiro.
<img width="1895" height="940" alt="image" src="https://github.com/user-attachments/assets/d56fc660-1eb0-4f4c-9850-0f861d3f4493" />


### 3. Comparativo vs Inflação
Permite entender se o rendimento do investimento está superando a inflação (IPCA) no período selecionado.
<img width="1890" height="941" alt="image" src="https://github.com/user-attachments/assets/57e3864b-988f-49fb-b752-e33a9df59830" />


---

## 📁 Estrutura do Projeto

```text
├── app.py           # Configuração do Flask e definição das rotas (GET/POST)
├── funcs.py         # Lógica de negócio, cálculos NumPy e gerador de gráficos Plotly
├── templates/       # Páginas HTML do sistema
│   ├── index.html   # Menu Principal
│   ├── accumulated.html
│   ├── heritage.html
|   └── savings.html
└── requirements.txt # Dependências para rodar o projeto
```
Como Executar:

Clone este repositório:

```
git clone [https://github.com/CaioFabioFelisberto/Money-Investment](https://github.com/CaioFabioFelisberto/Money-Investment)
```
Instale as dependências:

```
pip install -r requirements.txt
```
Inicie a aplicação:

```
python app.py
```
Acesse no navegador:
```
http://127.0.0.1:5000
```
