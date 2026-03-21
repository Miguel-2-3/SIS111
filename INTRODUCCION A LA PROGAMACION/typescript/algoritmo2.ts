const limite = 1000;
let numero = 2;
let suma = 0;

while (numero <= limite)
{
    suma = suma + numero;
    numero = numero + 2;  
}
console.log(`La suma es: ${suma}`);