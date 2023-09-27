# Domny: flexible way to write HTML and HTMX in Python

Domny is a Python package that provides a flexible way of creating HTML and HTMX code.
It aims to be the fundamental building block for writing HTMX code in Python, being faster and easier to use than Jinja.

## Installation
To install this module just run the following pip command:
```bash
pip install domny
```

## Examples
With Domny you can create an entier DOM using just it's tags functions.
```py
from domny.html.tags import *

doctype(c=
    html(c=
        head(c=
            meta(src="teste")
        )),
        body(c=
            p(c="Teste")
        )
    )
)
```


## Jinja benchmark comparison

