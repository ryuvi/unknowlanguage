
### **Roadmap para Desenvolvimento da Linguagem de Programação**

---

#### **1. Definição da Ideia e Escopo da Linguagem**

Antes de começar, é importante definir claramente qual é o **objetivo principal** da linguagem, **quem será o público-alvo** e **como ela será usada**. Algumas perguntas para se fazer:

- Qual será o propósito da linguagem? (ex: acadêmico, scripts, automatização, etc.)
- Quais paradigmas ela vai seguir? (imperativo, funcional, lógico, etc.)
- Quais serão os principais recursos da linguagem? (variáveis, loops, funções, etc.)
- Qual será a sintaxe básica?

**Dica**: Não precisa ser uma definição complexa, mas é bom ter um guia claro para as decisões que virão a seguir.

---

#### **2. Escolha do Nome para a Linguagem**

É sempre bom escolher um nome no início do projeto para começar a se referir à sua linguagem.

- **Dica**: Tente algo que seja **curto**, **memorável** e que tenha **significado** em relação à proposta da linguagem. Se você ainda não tem um nome, pode usar um nome provisório até ter uma ideia melhor.

---

#### **3. Implementação do Lexer (Analisador Léxico)**

O **lexer** (ou tokenizer) será responsável por dividir o código da linguagem em **tokens**. Isso envolve:

- Definir os **tokens** necessários (ex: palavras-chave, operadores, números, identificadores, parênteses).
- Criar as **regras regulares** para capturar cada tipo de token.

Passos:
1. Defina todos os **tokens** principais da linguagem.
2. Implemente o lexer com o **PLY** (ou outra ferramenta de sua escolha).
3. Teste o lexer para garantir que ele está reconhecendo corretamente os tokens.

---

#### **4. Definição da Gramática (Parser)**

O **parser** vai pegar os tokens gerados pelo lexer e transformá-los em uma **árvore de sintaxe abstrata** (AST). Aqui, você vai definir as **regras gramaticais** (como será a estrutura do programa, como as expressões são formadas, etc.).

- **Definir regras gramaticais**:
  - Como é a estrutura de um comando `assign`?
  - Como as expressões aritméticas são formadas?
  - Quais são as estruturas de controle (ex: `if`, `while`, etc.)?

Passos:
1. Defina as regras gramaticais principais (use a **notação BNF** ou outra forma de gramática).
2. Implemente o parser com **PLY** ou outra ferramenta de parsing.
3. Conecte o parser ao lexer para gerar a AST.
4. Teste a gramática e ajuste as regras conforme necessário.

---

#### **5. Construção do Executor (Interpretador)**

O **executor** (ou interpretador) será responsável por **executar** o programa representado pela AST. Ele vai iterar pela árvore e executar os comandos de acordo com o que foi definido nas regras de sintaxe.

Passos:
1. Implemente a execução de comandos básicos (`assign`, `show`).
2. Implemente a execução de expressões aritméticas e variáveis.
3. Adicione suporte para variáveis no ambiente de execução.
4. Teste a execução de comandos simples.

---

#### **6. Extensão da Linguagem com Funções e Controle de Fluxo**

Depois de implementar as funcionalidades básicas de variáveis e operações, você pode começar a **expandir** a linguagem com características mais complexas, como **funções** e **controle de fluxo**.

- **Funções**: Suporte para a definição e chamada de funções.
- **Controle de fluxo**: Estruturas como `if`, `else`, `while`, `for`, etc.
- **Escopo de variáveis**: Variáveis locais e globais.

Passos:
1. Adicione a capacidade de **definir e chamar funções**.
2. Implemente **estruturas condicionais** (`if`, `else`).
3. Implemente **loops** (`while`, `for`).
4. Teste o comportamento de escopo de variáveis e controle de fluxo.

---

#### **7. Tratamento de Erros e Depuração**

A próxima etapa é **melhorar o tratamento de erros** na linguagem. Isso pode envolver:

- **Mensagens de erro** amigáveis para o usuário.
- **Depuração**: Ferramentas ou técnicas para ajudar a depurar programas escritos na sua linguagem.

Passos:
1. Implemente **erros de sintaxe** e **erros de execução**.
2. Melhore as mensagens de erro para torná-las mais amigáveis.
3. Adicione funcionalidades de **depuração** (como exibir o valor das variáveis durante a execução).

---

#### **8. Adição de Bibliotecas e Módulos**

Para tornar a linguagem mais útil, você pode adicionar suporte a **bibliotecas padrão** (como funções matemáticas, manipulação de strings, etc.).

- **Entrada/Saída**: Leitura de arquivos, interação com o usuário, etc.
- **Bibliotecas padrão**: Funções matemáticas, manipulação de listas/arrays, etc.

Passos:
1. Defina as bibliotecas principais que sua linguagem vai oferecer.
2. Adicione suporte para bibliotecas externas.
3. Teste essas bibliotecas com programas de exemplo.

---

#### **9. Compilador ou Otimização**

Se você decidir criar um **compilador** em vez de um interpretador, o passo seguinte será converter o código fonte em código de máquina ou código intermediário.

- **Otimização**: Se você optar por compilar, pode incluir otimizações (como remoção de código redundante, otimização de loops, etc.).

Passos:
1. Implemente a **conversão para código intermediário** (se necessário).
2. Adicione **otimizações** (como simplificação de expressões).
3. Gere o **código de máquina** ou **bytecode**.

---

#### **10. Documentação e Exemplos**

Após ter uma versão estável da linguagem, **documente** a linguagem e forneça exemplos para que outras pessoas possam aprender e usar.

- **Manual do usuário**: Como usar a linguagem, exemplos de sintaxe, melhores práticas.
- **Documentação técnica**: Como a linguagem é implementada internamente (opcional).
- **Exemplos**: Exemplos práticos de código na linguagem.

---

#### **11. Testes e Feedback**

O último passo é garantir que sua linguagem funcione conforme o esperado.

- **Testes unitários**: Teste funções individuais e módulos.
- **Testes de integração**: Teste a interação entre o lexer, parser e executor.
- **Feedback de usuários**: Se você planeja lançar sua linguagem, peça feedback de outros desenvolvedores.

