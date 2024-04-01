"""
#### Exercício 2 - Identificar se a variante está no gene BRCA1 - Versão 1.

Receba 2 inputs do usuário:
1) O cromossomo de uma variante. Ele virá escrito como texto e da seguinte forma "chr1", "chr2", etc.
2) A posição dessa variante. Será um número inteiro.

Responde:
"Sim" se ela estiver no BRCA1.
"Não" se ela não estiver.

Considere que a variante está no gene BRCA1 se estiver no cromossomo 17 (chr17), e se a posição estiver no intevalo de 41196312 a 41277500.

Obs: Tirei a localização daqui: https://grch37.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012048;r=17:41196312-41277500.


cromossomo = input('Digite o cromossomo: ')
posição = int(input('Digite a posição da variante: '))
if cromossomo == 'chr17' and 41196312 <= posição <= 41277500:
	print ("Sim")
else:
	print ("Não")
