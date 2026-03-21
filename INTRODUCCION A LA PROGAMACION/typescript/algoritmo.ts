import readline from "node:readline/promises";
import { stdin as input, stdout as output} from "node:process";
const rl = readline.createInterface({input, output});

const x = await rl.question("INTRODUCE EL VALOR DE x: ")

const z= (15+(2*x/3))/(x*x+2)
console.log(`EL VALOR DE z ES: ${z}`)

rl.close()