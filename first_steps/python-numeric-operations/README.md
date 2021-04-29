# Módulo - Executar operações matemáticas em valores numéricos no Python 

## Aprendizados

- Usar os métodos 'type()', 'isinstance()' e 'isnumeric()' para inspecionar o tipo de dados de um valor e a adequação para uso ou a conversão em um tipo de dados numérico.
- Usar operadores matemáticos para fazer operações matemáticas básicas em dados numéricos.
- Usar o tipo de dados 'float' para representar valores que incluem valores fracionários, que são representados por números após o ponto decimal.

## Desafio 1 

#### Convertendo Fahrenheit em Celsius

A fórmula matemática para converter uma temperatura medida em Fahrenheit em uma temperatura medida em Celsius é mostrada no seguinte código:
```
celsius = (fahrenheit - 32) * 5/9
```
Use esta fórmula para criar um programa que solicita aos usuários uma temperatura em Fahrenheit, faz a conversão dela em Celsius e, em seguida, exibe a temperatura em Celsius.

Se os usuários inserirem o valor 55 no aviso, o programa deverá produzir a seguinte saída:
```
What is the temperature in fahrenheit?  55
Temperature in celsius is 12
```
No entanto, se os usuários inserirem um valor inválido, o programa deverá informá-los de que há um problema e, em seguida, ele será encerrado. Para esse cenário, se os usuários inserirem o valor mateus no aviso, o programa deverá produzir a seguinte saída:
```
What is the temperature in fahrenheit?  bob
Input is not a number.
```

## Desafio 2 

#### Calculadora Simples

Crie uma calculadora simples que aceita um primeiro número, uma operação e um segundo número.

Esta é uma saída de exemplo, em que um usuário inseriu 4 , * e 5 nos avisos:
```
Simple calculator!
First number? 4
Operation? *
Second number? 5
product of 4 * 5 equals 20
```
O programa deverá aceitar um símbolo, como o símbolo de asterisco ( * ), para fazer uma multiplicação e gerar um produto. Implemente a lógica para os seguintes resultados:

- Soma
- Diferença
- Produto
- Quociente
- Expoente
- Módulo

Se os usuários não conseguirem inserir um valor numérico, exiba a seguinte mensagem:
```
Please input a number.
```

Se os usuários inserirem uma operação não reconhecida, exiba a seguinte mensagem:
```
Operation not recognized.
```


