// Elaborar un algoritmo con un numero limite n
// Muestre la secuencia de numeros pares
import readline from "node:readline/promises";
import { stdin as input, stdout as output} from "node:process";
const rl = readline.createInterface({input, output});

let n = 1
const limite = await rl.question("INGRESE EL LIMITE: ")
let pares = ""
let impares = ""
// while(n <= limite)
// { 
//    if(n%2==0) pares =  `${pares} ${n},`
//    else impares = `${impares} ${n},`
//    n=n+1;
// }

for(;n<=limite;n=n+1)
{
    if(n%2==0) pares = `${pares} ${n},`
    else impares = `${impares} ${n},`
}
console.log(`Lista pares: ${pares}`)
console.log(`Lista impares: ${impares}`);

rl.close();
