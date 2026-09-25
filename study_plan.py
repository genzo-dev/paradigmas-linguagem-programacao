from lark import Lark

grammar = r"""
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
"""

parser = Lark(grammar, parser="lalr")

def study_plan_parser(program):
    return parser.parse(program)