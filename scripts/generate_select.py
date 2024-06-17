import os
from itertools import product
from pathlib import Path
from typing import List, Tuple

import black
from jinja2 import Template
from pydantic import BaseModel

try:
    template_path = (
        Path(__file__).parent.parent / "sqldev/sql/_expression_select_gen.py.jinja2"
    )
    destiny_path = Path(__file__).parent.parent / "sqldev/sql/_expression_select_gen.py"
except Exception as e:
    print(f"Error accessing file paths: {e}")


number_of_types = 4


class Arg(BaseModel):
    name: str
    annotation: str


arg_groups: List[Arg] = []

signatures: List[Tuple[List[Arg], List[str]]] = []

for total_args in range(2, number_of_types + 1):
    arg_types_tuples = product(["model", "scalar"], repeat=total_args)
    for arg_type_tuple in arg_types_tuples:
        args: List[Arg] = []
        return_types: List[str] = []
        for i, arg_type in enumerate(arg_type_tuple):
            if arg_type == "scalar":
                t_var = f"_TScalar_{i}"
                arg = Arg(name=f"entity_{i}", annotation=t_var)
                ret_type = t_var
            else:
                t_type = f"_T{i}"
                t_var = f"_TCCA[{t_type}]"
                arg = Arg(name=f"__ent{i}", annotation=t_var)
                ret_type = t_type
            args.append(arg)
            return_types.append(ret_type)
        signatures.append((args, return_types))

template: Template = Template(template_path.read_text())

result = template.render(number_of_types=number_of_types, signatures=signatures)

result = (
    "# WARNING: do not modify this code, it is generated by "
    "_expression_select_gen.py.jinja2\n\n" + result
)

result = black.format_str(result, mode=black.Mode())

current_content = destiny_path.read_text()

if current_content != result and os.getenv("CHECK_JINJA"):
    raise RuntimeError(
        "sqldev/sql/expression.py content not update with Jinja2 template"
    )

destiny_path.write_text(result)
