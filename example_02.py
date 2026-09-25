from study_plan import study_plan_parser

program = """
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
"""

tree = study_plan_parser(program)

print(tree.pretty())