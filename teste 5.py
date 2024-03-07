def inverter_string(s):
    string_invertida = ''
    for caracter in s:
        string_invertida = caracter + string_invertida
    return string_invertida

# Exemplo de uso:
entrada_usuario = input("Digite uma string para inverter: ")
print("String invertida:", inverter_string(entrada_usuario))
