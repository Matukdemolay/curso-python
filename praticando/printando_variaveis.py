

inteiro = 10 

decimal = 4.5 

complexo = 5 + 7j

string_simples = 'Opa!!'

string_dupla = "E ae!"

string_tripla = '''Alou
fala comigo rapazeada!'''

falso = False
verdadeiro = True


#O "f" antes das aspas significa que irei imprimir o conteudo das variaveis
""""
print(f'''
      Tipo Integer: {inteiro};  
      Tipo Decimal: {float};
      Tipo Complexo: {complexo};
      String Simples: {string_simples};
      String Dupla: {string_dupla};
      String Tripla: {string_tripla};
      Verdadeiro: {verdadeiro};
      Falso: {falso}''')
      
      """
      
      
# Criando uma lista com cada linha formatada
lines = [
    f'Tipo Integer: {inteiro}',
    f'Tipo Decimal: {decimal}',
    f'Tipo Complexo: {complexo}',
    f'String Simples: {string_simples}',
    f'String Dupla: {string_dupla}',
    f'String Tripla: {string_tripla}',
    f'Verdadeiro: {verdadeiro}',
    f'Falso: {falso}'
]

# Usando join() para concatenar as linhas com quebras de linha
formatted_output = '\n      '.join(lines) 

#Imprimindo o resultado
print(f'''      
      {formatted_output}
''')  