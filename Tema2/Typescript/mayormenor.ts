import readline from "node:readline/promises";
import { stdin as input, stdout as output} from "node:process";
const rl = readline.createInterface({input, output});

function mayormenor(a: number, b: number, c: number){
if (a > b && a > c) 
    if (b>c) 
        return `Mayor: ${a}  Menor: ${c}` 
    else 
        return `Mayor: ${a}  Menor: ${b}`;
    else if (b > a && b > c) 
        if (a>c) 
            return `Mayor: ${b}  Menor: ${c}` 
        else return `Mayor: ${b}  Menor: ${a}`;
    else if (a > b) 
        return `Mayor: ${c}  Menor: ${b}` 
    else return `Mayor: ${c}  Menor: ${a}`;
}

console.log("**********Mayor Menor**********")
const a = await rl.question("Introduzca el valor de a: ")
const b = await rl.question("Introduzca el valor de b: ")
const c = await rl.question("Introduzca el valor de c: ")

console.log(mayormenor(Number(a), Number(b), Number(c)))

rl.close();