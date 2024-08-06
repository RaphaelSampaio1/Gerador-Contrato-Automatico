# Gerador-Contrato-Automatico

Gerador de contratos personalizados

## Descrição

Este projeto consiste em um script Python que utiliza a biblioteca `fpdf` para gerar PDFs personalizados de orçamento de projetos. O script interage com o usuário para obter detalhes do projeto e cria um PDF com essas informações.

## Funcionalidades

### Interação Personalizada
O script possui uma função para criar uma interação personalizada com o usuário, exibindo perguntas formatadas com um estilo específico.

### Input Personalizado
A função de input personalizada exibe a pergunta formatada e recebe a resposta do usuário.

### Geração de PDF
A função principal do script gera o PDF com base nas informações fornecidas pelo usuário. Ela adiciona uma página ao PDF, insere uma imagem de template e posiciona os valores fornecidos nos locais apropriados.

### Valores do Contrato
O script coleta os seguintes dados do usuário:
- Descrição do Projeto
- Horas Estimadas para Completar o Projeto
- Valor da Hora
- Prazo de Entrega

O valor total do projeto é calculado multiplicando o número de horas estimadas pelo valor da hora.

## Tecnologias Utilizadas

- **Python e FPDF**: Para o desenvolvimento do backend e geração do PDF.
- **FPDF**: Biblioteca utilizada para criar documentos PDF.

## Execução

### Passo a Passo

1. **Instalar Dependências**
   - Certifique-se de ter a biblioteca `fpdf` instalada. Você pode instalá-la usando o pip:
     ```bash
     pip install fpdf
     ```

2. **Baixar os Arquivos Necessários**
   - Baixe o script Python e a imagem de template (`template.png`) que será usada como fundo no PDF.

3. **Executar o Script**
   - Execute o script Python. Ele fará perguntas interativas para coletar os dados do projeto.
   - O script irá gerar um PDF com as informações fornecidas.

4. **Visualizar o PDF Gerado**
   - O PDF será salvo no diretório atual com o nome `Orçamento_<Descrição do Projeto>.pdf`.

### Estrutura do Projeto

- `gerador_pdf.py`: O script principal para gerar o PDF.
- `template.png`: A imagem de template usada como fundo no PDF.

### Exemplo de Uso

```bash
python gerador_pdf.py
```

O script irá solicitar os seguintes dados:
- Descrição do Projeto
- Horas Estimadas
- Valor da Hora
- Prazo de Entrega

Após fornecer essas informações, o PDF será gerado e salvo no diretório atual.

## Como Funciona

1. **Coleta de Dados**
   - O script solicita ao usuário a descrição do projeto, horas estimadas, valor da hora e prazo de entrega.
   
2. **Cálculo do Valor Total**
   - O valor total do projeto é calculado multiplicando o número de horas estimadas pelo valor da hora.

3. **Geração do PDF**
   - O script cria um novo PDF, adiciona uma página e insere a imagem de template.
   - As informações fornecidas pelo usuário são posicionadas no PDF em locais específicos.
   - O PDF é salvo com um nome baseado na descrição do projeto.

## Considerações Finais

Este script é uma ferramenta útil para freelancers e profissionais que precisam gerar orçamentos personalizados rapidamente. Com pequenas modificações, ele pode ser adaptado para atender a diferentes necessidades e formatos de documentos.

Entre em contato comigo :
 - [LinkeIn](https://www.linkedin.com/in/raphael-sampaio-52475622b/)
 - [E-mail](mailto:raphaelsantos.jan@gmail.com)
