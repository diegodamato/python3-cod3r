from functools import reduce


def mais_um_meio(delta):
    def calc(nota):
        return nota + delta
    return calc


notas = [6.4, 7.2, 5.8, 8.4]
notas_finais_1 = map(mais_um_meio(1.5), notas)
notas_finais_2 = map(mais_um_meio(1.6), notas)

resultado_final_1 = list(notas_finais_1)
resultado_final_2 = list(notas_finais_2)

print(resultado_final_1)
print(resultado_final_2)


def somar(a, b):
    return a+b

total = reduce(somar, notas, 0)
print(total)


# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5?

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
