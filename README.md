# Desafio Cotefacil
Prova Técnica de Python - Cotefácil

## Instruções para a executar os desafios

### Desafio 1
- Gerar a imagem Docker;
- Executar o container;

```bash
cd Questao1
docker build -t questao1 .
docker run -e LOGIN=login -e PASSWORD=senha questao1
```
PS: Substituir login e senha pelo que foi disponibilizado na prova.

### Desafio 2
- Gerar a imagem Docker;
- Executar o container;

```bash
cd Questao2
docker build -t questao2 .
docker run -e LOGIN=login -e PASSWORD=senha questao2 [numero_do_pedido]
```
PS: Substituir o "login", a "senha" e o "numero_do_pedido" pelos que foram disponibilizados na prova.

### Desafio 3
- Gerar a imagem Docker;
- Executar o container;

```bash
cd Questao3
docker build -t terceiro-desafio
docker run terceiro-desafio [número_desejado]
```
PS: Substituir o numero_desejado pelo número que você ter o n-ésimo valor correspondente da sequencia de Fibonacci.
