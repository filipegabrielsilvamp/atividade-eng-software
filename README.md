
CRUD — Gerenciador de Estudos e Tarefas

Etapa 1 — Planejamento e implementação inicial

Projeto desenvolvido em Python para a disciplina de Algoritmos e Programação e documentado para a disciplina de Gestão Ágil de Projetos.

1. Seleção da Aplicação

Nome do projeto: Gerenciador de Estudos e Tarefas.

Descrição: O projeto consiste no desenvolvimento de um sistema executado no terminal, destinado a auxiliar estudantes na organização de suas atividades acadêmicas, permitindo o cadastro, a consulta, a atualização e a exclusão de tarefas.

Objetivo: Desenvolver uma aplicação simples que coloque em prática os conceitos fundamentais de lógica de programação, utilizando variáveis, tipos de dados, operadores, estruturas condicionais e estruturas de repetição.

2. Criação das Variáveis e Tipos de Dados

O sistema utilizará variáveis para armazenar as informações das tarefas durante a execução do programa.

- Título da tarefa: "str" — armazena o nome da atividade.
- Matéria/assunto: "str" — identifica a disciplina ou o conteúdo relacionado.
- Prioridade: "int" — representa o nível de prioridade, de 1 a 3.
- Prazo: "int" — indica a quantidade de dias restantes para a conclusão.
- Horas estimadas: "float" — representa o tempo previsto para a realização da tarefa.
- Descrição: "str" — contém informações complementares sobre a atividade.
- Status: "str" — indica se a tarefa está pendente, concluída ou cancelada.
- Urgência: "str" — classifica a tarefa como urgente ou dentro do prazo.
- Opção do menu: "int" — armazena a escolha realizada pelo usuário.

3. Implementação das Operações do CRUD

O sistema será organizado em quatro operações principais:

Create — Cadastrar tarefa: Solicitar ao usuário os dados de uma nova tarefa, verificando se as informações respeitam as regras estabelecidas.

Read — Consultar tarefas: Exibir as informações das tarefas cadastradas para que o usuário possa acompanhar suas atividades acadêmicas.

Update — Atualizar tarefa: Permitir a alteração dos dados ou do status de uma tarefa já cadastrada.

Delete — Excluir tarefa: Permitir a remoção de uma tarefa selecionada pelo usuário.

A navegação será realizada por meio de um menu numérico no terminal, facilitando a escolha das operações disponíveis.

4. Regras de Negócio

- RN01 — Validação da prioridade: O sistema deverá aceitar somente os valores 1, 2 e 3, correspondentes às prioridades baixa, média e alta.
- RN02 — Validação do título: O título deverá possuir pelo menos três caracteres para ser aceito.
- RN03 — Validação das horas estimadas: O tempo previsto para a realização da tarefa deverá ser maior que zero.
- RN04 — Classificação da urgência: O sistema deverá classificar automaticamente como "Urgente" as tarefas com prazo menor ou igual a dois dias. Quando o prazo for superior a dois dias, a tarefa será classificada como "No Prazo".
- RN05 — Validação das opções: O sistema deverá verificar se a opção selecionada no menu corresponde a uma operação disponível, informando ao usuário quando houver uma escolha inválida.

5. Requisitos Funcionais

- RF01: Permitir o cadastro de tarefas acadêmicas.
- RF02: Permitir a consulta das tarefas cadastradas.
- RF03: Permitir a atualização dos dados e do status das tarefas.
- RF04: Permitir a exclusão de tarefas cadastradas.
- RF05: Classificar automaticamente a urgência das tarefas conforme o prazo informado.
- RF06: Validar os dados de entrada de acordo com as regras de negócio.

6. Requisitos Não Funcionais

- RNF01: O sistema deverá ser executado por meio do terminal ou da linha de comando (CLI).
- RNF02: A navegação deverá utilizar um menu numérico simples e intuitivo.
- RNF03: A implementação deverá ser realizada exclusivamente em Python.
- RNF04: O código deverá respeitar os conteúdos e as estruturas de programação permitidos para a primeira etapa.
- RNF05: Os dados deverão ser mantidos durante a execução do programa, conforme os recursos de armazenamento autorizados pelo professor. A persistência após o encerramento poderá ser implementada em uma etapa posterior, caso seja permitida.

7. Tecnologias e Recursos Utilizados

- Linguagem: Python.
- Ambiente de execução: Terminal ou linha de comando.
- Conceitos de programação: Variáveis, tipos de dados, operadores aritméticos, relacionais e lógicos, estruturas condicionais ("if", "elif" e "else") e estruturas de repetição ("while" e "for").
- Armazenamento: Definido de acordo com as estruturas de dados autorizadas para esta etapa.

8. Justificativa da Escolha do Tema

O tema foi escolhido por abordar uma necessidade comum entre estudantes: organizar tarefas, acompanhar prazos e estabelecer prioridades. A aplicação permite relacionar a lógica de programação a uma situação prática do cotidiano acadêmico.

Além disso, o projeto apresenta complexidade adequada para a etapa inicial da disciplina, pois envolve diferentes tipos de dados, validação de informações, cálculos simples e tomada de decisões por meio de estruturas condicionais.

9. Justificativa dos Tipos de Dados e das Regras de Negócio

A utilização de diferentes tipos de dados permite representar adequadamente as informações de cada tarefa. Os tipos "str" e "int" serão utilizados para armazenar textos e valores inteiros, enquanto "float" permitirá registrar estimativas de tempo com casas decimais.

As regras de negócio foram definidas para evitar informações inválidas e tornar o sistema mais consistente. A validação da prioridade mantém uma escala padronizada, a validação do título facilita a identificação das atividades, e a exigência de horas positivas impede o registro de estimativas incompatíveis com o objetivo do sistema.

A classificação automática da urgência constitui um recurso importante do projeto, pois demonstra a aplicação de condições lógicas para gerar informações úteis ao usuário sem exigir que ele determine manualmente essa classificação.

Resultado esperado: Uma aplicação em Python que permita gerenciar tarefas acadêmicas por meio de um menu no terminal, aplicando os conceitos fundamentais de algoritmos e programação.