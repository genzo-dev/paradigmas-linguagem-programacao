# Atividade - DSL e EBNF

A atividade em questão consiste na criação de uma DSL (Domain Specific Language ou Linguagem Específica de Domínio), passando desde a definição do domínio até a construção e análise da linguagem criada.

A atividade exige certos pontos:

- Definir o domínio e o objetivo da linguagem: explicar para que a DSL foi criada, qual problema ela pretende resolver e onde poderia ser utilizada.
- Justificar a escolha da linguagem: durante a apresentação, explicar por que o domínio escolhido é adequado para uma DSL e quais seriam suas possíveis aplicações.
- Definir os tokens da linguagem, como palavras-chave, números, textos, símbolos etc.
- Criar a gramática em EBNF, começando pela regra start e detalhando as demais regras sintáticas.
- Testar a gramática no Lark, utilizando exemplos de programas válidos
- Apresentar pelo menos uma derivação de uma string válida, mostrando passo a passo como a sentença é gerada a partir da regra inicial.
- Apresentar a árvore de análise sintática (pretty()) de pelo menos um exemplo e explicar se a estrutura gerada faz sentido.
- Explicar as principais decisões de sintaxe tomadas durante a criação da linguagem.

Além disso, a tarefa exige certos pontos na sua entrega:

- Objetivo e descrição da DSL;
- Gramática em EBNF;
- Exemplos de strings válidas;
- Árvore de análise (pretty()) de pelo menos um exemplo;
- Uma derivação de uma string válida;
- Justificativa das decisões de sintaxe.

Tais pontos da entrega serão contemplados posteriormente.

Obs.: A atividade também possui pontos opcionais relacionados a tipagem, eles não serão contemplados.

---

## Objetivo da DSL

A **StudyPlan** foi criada para permitir que estudantes estruturem suas rotinas de aprendizagem de forma declarativa e textual. O problema que ela pretende resolver é a fragmentação da organização: em vez de usar planilhas complexas ou calendários genéricos, o aluno escreve um roteiro simples dizendo o que vai estudar, qual a prioridade e quanto esforço (medido em *Pomodoros*) será dedicado.

## Onde poderia ser utilizada

Pode ser integrada a aplicativos de produtividade, extensões de VS Code para programadores que estudam, ou scripts que leem o arquivo `.study` e geram eventos automáticos para disparar timers de foco.

## Justificativa da Linguagem

O domínio de organização de estudos é perfeito para uma DSL porque linguagens de propósito geral (como Python ou TypeScript) seriam muito verbosas para simplesmente listar tarefas. Por outro lado, interfaces gráficas (GUIs) podem ser lentas para quem prefere digitar. A **StudyPlan** oferece o meio-termo ideal: uma sintaxe enxuta, legível por humanos (semelhante ao JSON ou CSS, mas focada em estudo) que abstrai toda a lógica de programação, focando apenas no "o que" e "quanto" estudar.

## Tokens da Linguagem

**Palavras-chave: `Materia`,`Topico`,`Prioridade`,`Estudar`,`Revisar`.**

**Identificadores/Literais: `STRING`** textos entre aspas para nomes, `NUMERO` inteiros que definem quantidades.

**Enums:** `Alta`, `Media`, `Baixa` para prioridade. `Pomodoro`, `Pomodoros` para unidades de tempo.

**Símbolos:**

| `{` | Início de bloco |
| --- | --- |
| `}` | Fim de bloco |
| `:` | Atribuição de valor |
| `;` | Fim de instrução |

## Gramática em EBNF

A gramática abaixo foi feita pronta para ser utilizada no Lark.

> [!NOTE]
>
> Determinações semânticas do Lark
>
> Regras (não-terminais): começam com letras minúsculas;
> Tokens (terminais): começam com letras maiúsculas;
>

```ebnf
start: materia+

materia: "Materia" STRING "{" prioridade? topico+ "}"

prioridade: "Prioridade" ":" NIVEL ";"

topico: "Topico" STRING "{" acao+ "}"

acao: TIPO_ACAO ":" NUMERO UNIDADE ";"

NIVEL: "Alta" | "Media" | "Baixa"
TIPO_ACAO: "Estudar" | "Revisar"
UNIDADE: "Pomodoro" | "Pomodoros"

%import common.ESCAPED_STRING -> STRING
%import common.INT -> NUMERO
%import common.WS
%ignore WS
```

## Exemplos de Strings Válidas

### Exemplo 1

Criação de uma matéria

```ebnf
Materia "Paradigmas de Linguagens" {
    Prioridade: Alta;
    Topico "Lark e EBNF" {
        Estudar: 3 Pomodoros;
    }
    Topico "Arvore Sintatica" {
        Revisar: 1 Pomodoro;
    }
}
```

### Exemplo 2

Criação de múltiplas matérias:

```ebnf
Materia "TypeScript" {
    Prioridade: Media;
    Topico "Generics" {
        Estudar: 2 Pomodoros;
    }
}
Materia "NestJS" {
    Topico "Injecao de Dependencia" {
        Revisar: 2 Pomodoros;
    }
}
```

## Derivação da Linguagem

A **StudyPlan** está sendo derivada mais à esquerda, buscando criar uma ordem determinística para demonstrar melhor a construção da sentença.

### Derivação

Para facilitar a derivação, utilizaremos o exemplo 1 de strings válidas:

```ebnf
Materia "Paradigmas de Linguagens" {
    Prioridade: Alta;
    Topico "Lark e EBNF" {
        Estudar: 3 Pomodoros;
    }
    Topico "Arvore Sintatica" {
        Revisar: 1 Pomodoro;
    }
}
```

#### Derivação passo a passo

| **Passo** | **Forma sentencial** | **Não-terminal escolhido** | **Produção aplicada** |
| --- | --- | --- | --- |
| 00 | `start` | `start` | `start → materia+` |
| 01 | `materia` | `materia` | `materia → "Materia" STRING "{" prioridade? topico+ "}"` |
| 02 | `"Materia" STRING "{" prioridade topico topico "}"` | `STRING` | `STRING → "Paradigmas de Linguagens"` |
| 03 | `"Materia" "Paradigmas de Linguagens" "{" prioridade topico topico "}"` | `prioridade` | `prioridade → "Prioridade" ":" NIVEL ";"` |
| 04 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" NIVEL ";" topico topico "}"` | `NIVEL` | `NIVEL → "Alta"` |
| 05 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" topico topico "}"` | `topico` | `topico → "Topico" STRING "{" acao+ "}"` |
| 06 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" STRING "{" acao "}" topico "}"` | `STRING` | `STRING → "Lark e EBNF"` |
| 07 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" acao "}" topico "}"` | `acao` | `acao → TIPO_ACAO ":" NUMERO UNIDADE ";"` |
| 08 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" TIPO_ACAO ":" NUMERO UNIDADE ";" "}" topico "}"` | `TIPO_ACAO` | `TIPO_ACAO → "Estudar"` |
| 09 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" "Estudar" ":" NUMERO UNIDADE ";" "}" topico "}"` | `NUMERO` | `NUMERO → 3` |
| 10 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" "Estudar" ":" 3 UNIDADE ";" "}" topico "}"` | `UNIDADE` | `UNIDADE → "Pomodoros"` |
| 11 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" "Estudar" ":" 3 "Pomodoros" ";" "}" topico "}"` | `topico` | `topico → "Topico" STRING "{" acao+ "}"` |
| 12 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" "Estudar" ":" 3 "Pomodoros" ";" "}" "Topico" STRING "{" acao "}" "}"` | `STRING` | `STRING → "Arvore Sintatica"` |
| 13 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" "Estudar" ":" 3 "Pomodoros" ";" "}" "Topico" "Arvore Sintatica" "{" acao "}" "}"` | `acao` | `acao → TIPO_ACAO ":" NUMERO UNIDADE ";"` |
| 14 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" "Estudar" ":" 3 "Pomodoros" ";" "}" "Topico" "Arvore Sintatica" "{" TIPO_ACAO ":" NUMERO UNIDADE ";" "}" "}"` | `TIPO_ACAO` | `TIPO_ACAO → "Revisar"` |
| 15 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" "Estudar" ":" 3 "Pomodoros" ";" "}" "Topico" "Arvore Sintatica" "{" "Revisar" ":" NUMERO UNIDADE ";" "}" "}"` | `NUMERO` | `NUMERO → 1` |
| 16 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" "Estudar" ":" 3 "Pomodoros" ";" "}" "Topico" "Arvore Sintatica" "{" "Revisar" ":" 1 UNIDADE ";" "}" "}"` | `UNIDADE` | `UNIDADE → "Pomodoro"` |
| 17 | `"Materia" "Paradigmas de Linguagens" "{" "Prioridade" ":" "Alta" ";" "Topico" "Lark e EBNF" "{" "Estudar" ":" 3 "Pomodoros" ";" "}" "Topico" "Arvore Sintatica" "{" "Revisar" ":" 1 "Pomodoro" ";" "}" "}"` | — | **Derivação completa** |

## Árvore de Análise Sintática (`pretty()`)

Vamos rodar o exemplo 1 no Lark e imprimir com `tree.pretty()`, a estrutura gerada será essa:

```ebnf
start
  materia
    "Paradigmas de Linguagens"
    prioridade  Alta
    topico
      "Lark e EBNF"
      acao
        Estudar
        3
        Pomodoros
    topico
      "Arvore Sintatica"
      acao
        Revisar
        1
        Pomodoro
```

Agora com o exemplo 2:

```ebnf
start
  materia
    "TypeScript"
    prioridade  Media
    topico
      "Generics"
      acao
        Estudar
        2
        Pomodoros
  materia
    "NestJS"
    topico
      "Injecao de Dependencia"
      acao
        Revisar
        2
        Pomodoros
```

# Justificativa das Decisões de Sintaxe

| **Decisão** | **Justificativa** |
| --- | --- |
| Uso de chaves `{}` | Escolhido devido a familiaridade para desenvolvedores C-like (como JS, TS, Java, C++), defininido visualmente o escopo de uma matéria ou tópico. |
| Strings com aspas para nomes | Permite que as matérias e tópicos possuam espaços, evitando escrever tudo em *CamelCase* ou *snake_case* |
| Ponto e vírgula `;` | Ao final de cada regra simples, o ponto e vírgula evita ambiguidades no parser caso o usuário escreva várias ações na mesma linha. |
| Forte apelo declarativo | A própria linguagem diz o que é o estudo, e não como o computador deve processá-lo (sem `if`, `for` ou variáveis). |