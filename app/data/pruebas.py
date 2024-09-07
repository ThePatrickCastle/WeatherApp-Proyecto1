from input_cleaner import InputCleaner


ciudad = input("Dame una ciudad:")

reader = InputCleaner(ciudad)

print(reader.encontrar_mejor_apareamiento())
