# Função que imprime elementos string de array
def imprimirElementosDeString(array):
    for elementos in  array:
     print("Lista de elementos de array: %s" %elementos)

# Função de concatenação de duas Strings
def somaDeDuasString(string1,string2):
   strings = {string1, string2}
   validation1 = type(string1)
   validation2 = type(string2)

   if validation1 == str and validation2 == str: 
    stringConcatenada = " ".join(strings)
    return stringConcatenada
   else:
     return "dodos adicionado não é strings"

# soma de numetos de array
def somaDeElementosDeArray(numeros):
  soma = 0
  for numbers in numeros:
    soma += numbers
  
  return soma;

print(somaDeDuasString("Thiago","fonseca"))

numeros = [1,2,3,4,5,6,7,8]

somaDeElementosDeArray(numeros);


#sout
#sysout

# Dados pra programar

# alunos = ["erick", "Thiago", "Luciano"]
# cursos = ["Análise e desenvolviemento de sistemas", "Ciência da computação", "Sistema da informação", "Engenharia de software"]



#nome ="teste"
#nome1 ="teste2"
#nome2 = "teste3"
#print ('fulano %s e %s , %s são legais' %nome)
#print('fulano {2} e {0}, {1} são legais'.format(nome,nome1,nome2))
#print('fulano ' + nome + ' e ' + nome2 +' , ' + nome1 + ' são legais')



#print("nome:  %s" %nome)
