MATERIAIS = ["papel", "plástico", "vidro", "metal"]
coletas = [{"codigo": 1, "data": "05/10/2026", "material": "papel", "peso": 8.5},
           {"codigo": 2, "data": "12/10/2026", "material": "vidro", "peso": 12.0},
           {"codigo": 3, "data": "03/11/2026", "material": "papel", "peso": 4.0}]
 
# Opção A: relatório por categoria (laço dentro de laço + acumulador)
def relatorio_por_material():
    for material in MATERIAIS:
        total = 0
        quantidade = 0
        for c in coletas:
            if c["material"] == material:
                total += c["peso"]
                quantidade += 1
        print(f"{material:<9} | {quantidade} coletas | {total:.1f} kg")
 
# Opção B: desfazer o último cadastro (uma lista usada como pilha)
historico = []
 
def registrar(c):
    coletas.append(c)
    historico.append(c)        # guarda o último no fim da lista
 
def desfazer():
    if len(historico) == 0:
        print("Nada para desfazer.")
        return
    ultima = historico.pop()   # tira o último que entrou
    coletas.remove(ultima)
    print(f"Cadastro {ultima['codigo']} desfeito.")
 
relatorio_por_material()
registrar({"codigo": 4, "data": "10/11/2026", "material": "metal", "peso": 2.5})
desfazer()
desfazer()
print(len(coletas))
 