import random
from busca_ordenacao import busca_sequencial, busca_binaria
 
random.seed(42)  # sorteio fixo: quem rodar de novo obtém os mesmos números
 
print("Registros | Sequencial | Binária")
for n in [100, 1000, 10000]:
    # n registros com códigos de 1 a n, já em ordem
    ordenados = []
    for codigo in range(1, n + 1):
        ordenados.append({"codigo": codigo})
    # uma cópia embaralhada, para a busca sequencial
    embaralhados = ordenados[:]
    random.shuffle(embaralhados)
 
    total_seq = 0
    total_bin = 0
    for i in range(100):  # 100 buscas por códigos sorteados
        codigo = random.randint(1, n)
        _, comp = busca_sequencial(embaralhados, codigo)
        total_seq += comp
        _, comp = busca_binaria(ordenados, codigo)
        total_bin += comp
 
    print(f"{n} | {total_seq / 100:.1f} | {total_bin / 100:.1f}")
 