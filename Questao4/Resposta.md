# Resposta

O problema que acontece é que o programa ficará lento e pode até travar quando for colocado o número 50 na sequência de Fibonacci. Isso ocorre porque o programa começa a calcular a sequência "de trás para frente". Por exemplo, para calcular o número 50, ele precisará calcular os números 49 e 48. No entanto, para calcular o número 49, ele novamente precisará calcular o número 48, e assim por diante.

Como o programa usa a recursão para calcular os números, ele não se lembra dos cálculos que já fez antes, o que o leva a repetir as mesmas contas várias vezes. Isso faz com que o programa fique extremamente lento e, dependendo do tamanho do número, pode até travar o computador.
