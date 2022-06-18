import re

def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)
    if not cpf or len(cpf) != 11:
        return f'Digite 11 digitos do CPF'
    novo_cpf = cpf[:-2]  # elimina os dois ultimos digitos do cpf
    reverso = 10         # contador reverso
    total = 0

    # loop do cpf
    for index in range(19):
        if index > 8:  # primeiro indice vai de 0 a 9,
            index -= 9  # São os 9 primeiros digitos do cpf

        total += int(novo_cpf[index]) * reverso # valor total da multiplicação

        reverso -= 1 #descrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        return 'CPF Válido'

    else:
        return 'CPF Iválido'




