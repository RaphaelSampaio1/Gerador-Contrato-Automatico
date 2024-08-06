from fpdf import FPDF

class Gerador_Pdf:
    def __init__(self):
        # Função para perguntas personalizadas
        def interacao_personalizada(valor):
            tam = len(valor) + 1
            print('\n')
            print('-' * tam)
            print(f'\033[1m{valor}')
            print('-' * tam)

        # Funçãor para resposta do usuario
        def input_personalizado(prompt):
            interacao_personalizada(prompt)
            return input('>> ')

        # função para gerar PDF
        def gerar_pdf():
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial","B")
            pdf.image('template.png', x=0, y=0)

            # Posição de inserção de valores
            pdf.text(115, 146, self.descricao_proj)
            pdf.text(115, 160, str(self.horas_estimadas))
            pdf.text(115, 175, str(self.valor_hora))
            pdf.text(115, 190, self.prazo_entrega)
            pdf.text(115, 205, str(self.valor_total))

            # Criando PDF
            pdf.output(f"Orçamento_{self.descricao_proj}.pdf")
            interacao_personalizada('📃 PDF GERADO')


        # absorver valores de contrato
        self.descricao_proj = input_personalizado('Descreva a descrição do projeto :')
        self.horas_estimadas = int(input_personalizado('Quantas horas (aproximadamente) levará esse projeto :'))
        self.valor_hora = int(input_personalizado('Qual o valor da sua hora (R$):'))
        self.prazo_entrega = input_personalizado('Defina prazo estimado de entrega:')

        self.valor_total = self.horas_estimadas * self.valor_hora
        gerar_pdf()

Gerador_Pdf()