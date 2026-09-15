# atividade-eng-software
CRUD TaskFlow (Gerenciador de Estudo e Tarefas)
Projeto desenvolvido em Python para a disciplina de Algoritmos e Programação e documentado para a disciplina de Gestão Ágil de Projetos.
Objetivo
Este projeto visa gerenciar o fluxo de estudos e tarefas acadêmicas por meio de um sistema CRUD no terminal, auxiliando estudantes na organização de suas pendências.
Tipos de Dados
 * Título da Tarefa: string
 * Matéria/Assunto: string
 * Prioridade (1 a 3): int
 * Prazo (dias restantes): int
 * Horas Estimadas: float
 * Descrição: string
Funcionalidades
 * Cadastrar nova tarefa
 * Listar tarefas pendentes
 * Atualizar status e detalhes da tarefa
 * Remover tarefa concluída ou cancelada
Requisitos
Requisitos Funcionais
 * RF01 - O sistema deve permitir o cadastro de novas tarefas com suas especificações.
 * RF02 - O sistema deve exibir a lista de tarefas cadastradas.
 * RF03 - O sistema deve permitir a alteração das informações de uma tarefa existente.
 * RF04 - O sistema deve permitir a exclusão de tarefas do banco de dados.
Regras de Negócio
 * RN01 - O nível de prioridade deve ser estritamente 1 (Baixa), 2 (Média) ou 3 (Alta). Se o usuário digitar um valor fora desse intervalo, o sistema deve rejeitar a inserção e alertar sobre o limite.
 * RN02 - O campo de título da tarefa deve ter no mínimo 3 caracteres. Caso contrário, o sistema deve notificar que o nome é muito curto para identificação.
 * RN03 - O tempo estimado de dedicação (horas) não pode ser nulo nem negativo (\le 0). O sistema deve exigir um valor positivo.
 * RN04 - O sistema deve calcular automaticamente a urgência com base nos dias restantes do prazo. Se os dias forem menores ou iguais a 2, o sistema deve etiquetar a tarefa como "Urgente"; se for maior que 2, como "No Prazo".
Requisitos Não Funcionais
 * RNF01 - A execução do projeto deve ocorrer via linha de comando (CLI/Terminal).
 * RNF02 - O fluxo de navegação do menu no terminal deve ser intuitivo e baseado em escolhas numéricas.
 * RNF03 - O sistema deve armazenar os dados localmente sem dependência de APIs externas ou internet.
 * RNF04 - O projeto deve ser codificado exclusivamente na linguagem Python.
Por que esta proposta é boa para defender na faculdade?
 * Justificativa do Tema: Um gerenciador de tarefas acadêmicas faz sentido no contexto de alunos de programação/gestão, sendo uma aplicação útil para o próprio dia a dia dos estudantes.
 * Diferencial dos Dados: Utiliza tipos variados (texto para descrições, inteiros para prioridades/prazos e float para horas de estudo), o que demonstra domínio sobre diferentes estruturas na hora da avaliação do código.
 * Lógica das Regras: A validação da RN04 faz uma checagem de intervalo diferente da original, permitindo criar um alerta visual no terminal ("Urgente" vs "No Prazo") que valoriza muito a nota de apresentação.
Por que a ideia deste negócio?
 * Resolução de um problema real: É um sistema voltado para a rotina de estudantes, o que torna a defesa do projeto fácil de explicar para os professores.
 * Complexidade ideal para CRUD: Permite trabalhar com entradas de texto, números inteiros, decimais e lógica condicional sem complicar excessivamente o código.
Por que a escolha destes Tipos de Dados?
 * Título da Tarefa (string): Aceita caracteres alfanuméricos, permitindo nomes completos e variados para os deveres (ex: "Trabalho de BD 1").
 * Matéria/Assunto (string): Categoria textual que facilita a organização e possibilita futuras implementações de filtros de busca no terminal.
 * Prioridade (int): O uso de números inteiros (1, 2 ou 3) simplifica a validação por intervalo no código e economiza memória em comparação com palavras ("baixa", "alta").
 * Prazo (int): Representa os dias restantes em números inteiros, o que permite fazer cálculos matemáticos diretos para descobrir se a tarefa está perto do fim.
 * Horas Estimadas (float): Necessita de casas decimais para registrar frações de tempo reais (ex: 1.5 horas de estudo).
 * Descrição (string): Texto livre para observações mais detalhadas do aluno.
Por que a lógica destas Regras de Negócio?
 * RN01 (Prioridade 1 a 3): Evita a entrada de dados inválidos no sistema (como prioridade 0 ou 99), garantindo que a escala de importância permaneça consistente.
 * RN02 (Título \ge 3 caracteres): Impede o salvamento de tarefas com nomes vazios ou de apenas uma letra, o que poluiria a exibição da lista no terminal.
 * RN03 (Horas Estimadas > 0): Validação matemática essencial. Não faz sentido registrar uma tarefa que demande 0 ou menos horas para ser concluída.
 * RN04 (Classificação de Urgência): É o principal diferencial lógico do projeto. Aplica a estrutura de decisão (if/else) para gerar a etiqueta "Urgente" ou "No Prazo" automaticamente, dispensando o usuário de ter que digitar esse status manualmente.


