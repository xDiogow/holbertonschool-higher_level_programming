#!/usr/bin/python3
"""
This module is used for text indentation
"""

def text_indentation(text):
    """
    Prints each line of text by adding an empty line
    :param text: Text to be indented
    :return: None
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for char in '.?:':
        text = text.replace(char, f'{char}\n')

    lines = []
    for line in text.split('\n'):
        stripped_line = line.strip()
        lines.append(stripped_line)

    print("\n".join(lines), end="")

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")