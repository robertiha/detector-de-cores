# Detector de Cores em Imagens

É um software desenvolvido em Python utilizando a biblioteca **Tkinter** para a interface gráfica e a biblioteca **ColorThief** para extração de cores. 
O programa permite que o usuário selecione uma imagem e, em seguida, detecta as 10 cores predominantes nessa imagem, exibindo-as em formato de retângulos coloridos e seus respectivos códigos hexadecimais. 
Além disso, o usuário pode copiar os códigos hexadecimais para a área de transferência com um único clique.

---

## Resumo das Melhorias no `main2.py`

### 1. **Redimensionamento e Centralização da Imagem**
   - A imagem é redimensionada mantendo a proporção original e centralizada no `Label`, garantindo que ela se ajuste ao espaço disponível sem distorções.

### 2. **Uso de Laços `for` para Simplificar a Criação de Retângulos e Rótulos**
   - Substituiu a criação manual de retângulos e rótulos por um laço `for`, reduzindo a repetição de código e facilitando a manutenção.

### 3. **Adição de um Botão para Copiar Códigos Hexadecimais**
   - Um botão "Copy" foi adicionado para copiar todos os códigos hexadecimais gerados para a área de transferência, utilizando a biblioteca `pyperclip`.

### 4. **Melhoria na Interface Gráfica**
   - A interface foi aprimorada com um título mais centralizado, botões compactos e uma organização mais eficiente dos elementos.

### 5. **Uso de Listas para Armazenar Cores e Rótulos**
   - As cores e rótulos são armazenados em listas, permitindo manipulação dinâmica e simplificada.

### 6. **Simplificação do Processamento de Cores**
   - O processamento das cores foi simplificado com o uso de listas e laços `for`, eliminando a necessidade de código repetitivo.

### 7. **Melhoria na Organização e Modularidade do Código**
   - O código foi reorganizado para ser mais modular e legível, com funções específicas para cada tarefa.

### 8. **Adição da Biblioteca `pyperclip` para Funcionalidade de Cópia**
   - A biblioteca `pyperclip` foi adicionada para permitir a cópia dos códigos hexadecimais para a área de transferência.
