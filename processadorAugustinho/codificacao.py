#processador experimental
registros = []
def mostraMemoria():
  global registros
  print(registros)

def memoria():
  global registros
  for i in range(10):
    registros.append(0)
  return registros

memoria()#constroi a memoria
cmd=''
while(cmd!='HALT'):
  cmd = input('Digite o comando:')
  elementos = cmd.split(' ')
  if len(elementos)==2:
    param=elementos[1].split(',')
    p1=param[0]
    p2=param[1]
    if elementos[0]=='LOAD':
      if p2.startswith('R'):
        print('P2 eh um registro')
        posicaoOrigem = int(p2[1:])
        posicaoDestino = int(p1[1:])
        registros[posicaoDestino]=registros[posicaoOrigem]
        mostraMemoria()
      else:
        posicao = int(p1[1:])
        print(posicao,len(registros))
        registros[posicao]=int(p2)
        mostraMemoria()
