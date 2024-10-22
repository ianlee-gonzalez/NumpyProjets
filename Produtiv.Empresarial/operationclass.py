import numpy as np
import matplotlib.pyplot as plt

class IntArray:
    def __init__(self, int_array):
        if not isinstance(int_array, np.ndarray) or int_array.dtype != int:
            raise ValueError("Input must be a NumPy array of integers")
        
        self.int_array = int_array

    def display(self):
        print(self.int_array)

    def salary(self):
        array_shape = self.int_array.shape  # Pegamos a forma (dimensão) do array
        money_for_product = np.full(array_shape, 7)  # Supomos 7 unidades monetárias por produto
        salaries = self.int_array * money_for_product

        print(f"People made {self.int_array} products and this is their salaries {salaries}")

        # Agora mostramos o gráfico de salários
        x = np.arange(len(self.int_array))  # Índices de funcionários
        plt.figure(figsize=(10, 6))
        
        plt.bar(x, salaries, color='green', label='Salário Total')
        
        plt.title('Salário Total dos Funcionários com Base na Produção', fontsize=16)
        plt.xlabel('Funcionário (ID)', fontsize=12)
        plt.ylabel('Salário (Unidades Monetárias)', fontsize=12)
        plt.grid(axis='y')
        
        for i, salary in enumerate(salaries):
            plt.text(i, salary + 1, str(salary), ha='center', fontsize=10)
        
        plt.legend()
        plt.show()

def show_data(self):
    x = np.arange(1, len(self.int_array) + 1)  # Ajusta os IDs para começar de 1
    plt.figure(figsize=(10, 6))  # Ajustar o tamanho da figura

    # Melhorar a aparência do gráfico
    plt.plot(x, self.int_array, marker='o', color='b', label='Produtos por mês')
    
    # Adicionar título mais descritivo
    plt.title('Produtividade Empresarial', fontsize=16)

    # Nome mais claro para os eixos
    plt.xlabel('Funcionário (ID)', fontsize=12)
    plt.ylabel('Quantidade de Produtos', fontsize=12)

    # Adicionar grades para melhor visualização
    plt.grid(True)

    # Adicionar uma legenda explicando o gráfico
    plt.legend()

    # Adicionar rótulos nos pontos (quantidade de produtos)
    for i, value in enumerate(self.int_array):
        plt.text(i + 1, value + 0.5, str(value), ha='center', fontsize=10)  # Ajusta a posição do texto

    # Salvar o gráfico como um arquivo de imagem
    plt.savefig('produtividade_empresarial.png', format='png', dpi=300)  # Salva o gráfico com 300 dpi

    # Mostrar o gráfico final
    plt.show()

