from study_plan import study_plan_parser

program = """
Materia "Paradigmas de Linguagens" {
    Prioridade: Alta;
    Topico "Lark e EBNF" {
        Estudar: 3 Pomodoros;
    }
    Topico "Arvore Sintatica" {
        Revisar: 1 Pomodoro;
    }
}
"""

tree = study_plan_parser(program)

print(tree.pretty())