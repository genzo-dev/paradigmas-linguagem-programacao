# Atividade - DSL e EBNF

A atividade em questão consiste na criação de uma DSL (Domain Specific Language ou Linguagem Específica de Domínio), passando desde a definição do domínio até a construção e análise da linguagem criada.

Para uma especificação melhor da atividade em questão, acesse o [ATIVIDADE.md](ATIVIDADE.md).

## Objetivo da DSL

A **StudyPlan** foi criada para permitir que estudantes estruturem suas rotinas de aprendizagem de forma declarativa e textual. O problema que ela pretende resolver é a fragmentação da organização: em vez de usar planilhas complexas ou calendários genéricos, o aluno escreve um roteiro simples dizendo o que vai estudar, qual a prioridade e quanto esforço (medido em *Pomodoros*) será dedicado.

## Onde poderia ser utilizada

Pode ser integrada a aplicativos de produtividade, extensões de VS Code para programadores que estudam, ou scripts que leem o arquivo `.study` e geram eventos automáticos para disparar timers de foco.

## Exemplo de Sintaxe

```text
materia "Paradigmas de Linguagens" {
    topico "Construcao de DSL" prioridade alta;
}
estudar "Paradigmas de Linguagens" por 2 pomodoros;
```

## Como rodar os exemplos

> [!IMPORTANT]
> Requisitos:
>
> Python 3.x

1. Crie a ```.venv```:
```bash
python -m venv .venv
```

2. Inicie o ambiente:

No Windows
```bash
.venv\Scripts\activate
```

No Linux
```bash
source .venv/bin/activate
```

3. Agora instale a biblioteca Lark:
```bash
pip install lark
```

4. Rode os exemplos:
```bash
python example_01.py
```

ou

```bash
python example_02.py
```