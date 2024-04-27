"""
Ex005: Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.Ex:
    Entrada:
        Nota 1: 4.5
        Nota 2: 8.5
    Saída:
        Primeira nota: 4.5
        Segunda nota: 8.5
        Média: 6.5
"""

primeira_nota = float(input('Informe a primeira nota do aluno: '))
segunda_nota = float(input('Informe a segunda nota do aluno: '))

media = (primeira_nota + segunda_nota) / 2

print(f'Primeira nota:  {primeira_nota}\nSegunda nota: {segunda_nota}\nMédia: {media}')