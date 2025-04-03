# Solicita a quantidade de alunos
quantidade_alunos = int(input("Digite o número de alunos: "))

# Loop para cada aluno
for i in range(quantidade_alunos):
    print(f"\nAluno {i + 1}")
    nome = input("Nome do aluno: ")
    
    # Coleta das 3 notas
    notas = []
    for j in range(1, 4):
        nota = float(input(f"Digite a nota {j}: "))
        notas.append(nota)
    
    # Cálculo da média
    media = sum(notas) / 3
    
    # Verificação de aprovação
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    
    # Exibição do resultado
    print(f"\nResultado do aluno: {nome}")
    print(f"Notas: {notas[0]:.1f}, {notas[1]:.1f}, {notas[2]:.1f}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")
