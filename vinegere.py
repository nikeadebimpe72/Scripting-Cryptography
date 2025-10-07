#!/usr/bin/env python3


def create_vigenere():
    viginere_table = []
    for i in range(26):
        row = [chr((i+j) % 26 + 65) for j in range(26)]
        viginere_table.append(row)

    return viginere_table

def generate_html_table(table):
    html = "<table border = '1'>"
    html += f"<tr><th></th>" + "".join([f"<th>{chr(65+i)}</th>" for i in range(26)]) + "</tr>"
    for i, row in enumerate(table):
        html += f"<tr><th>{chr(65+i)}</th>" + "".join([f"<td>{cell}</td>" for cell in row])
    html += "</tables>"
    return html
