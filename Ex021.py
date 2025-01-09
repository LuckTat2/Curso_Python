import random
primeiroAluno = input("Primeiro aluno: ")
segundoAluno = input("Segundo aluno: ")
terceiroAluno = input("Terceiro aluno: ")
quartoAluno = input("Quarto aluno: ")
listaAlunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
random.shuffle(listaAlunos)
print("A ordem de apresentação será: {}".format(listaAlunos))