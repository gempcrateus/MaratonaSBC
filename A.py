#recebe os dois primeiros parametros e os guarda
entrada1 = input()
N, H = (int(number) for number in entrada1.split(' '))
        
#verifica os mesmos
if not 1<=N<=6:
    exit()
if not 90<=H<=200:
    exit()

#recebe as alturas dos brinquedos e cria um vetor de strings
B = input().split(' ') 

#verifica se foram listadas todas as alturas
if not len(B)==N:
    exit()

#Visualiza em quais brinquedos Joaozinho pode andar
R = 0
for valor in B:
    if(H>=int(valor)):
        R+=1
print(R)
exit()