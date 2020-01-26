import Web3 from 'web3';
import fs from 'fs';
import chalk from 'chalk';
import path from 'path';

// Step 1: Setting up the connection string
const rpcURL = "http://127.0.0.1:7545";
const web3 = new Web3(rpcURL);
const contract='0x31d064fb1C9B35E3774F99a62bBA56884224fd8D';

// Step 2: Load the contract ABI (Application Binary Interface)
// In order to read the contract from the file install file system package

/**
 * Creating a utility function to get the contract object.
 */
function getContractObject(contractAddress){
    let abiPath = path.join(__dirname + '/contract/bin/DataStorage.abi');
    let abi = fs.readFileSync(abiPath);

    let deployedContract = new web3.eth.Contract(JSON.parse(abi),contractAddress);
    return deployedContract;
}

async function readMethodOfContract(value){

    console.log(chalk.green('==> Demonstrating the get method invocation of smart contract'));
    let deployedContract = getContractObject(value);
  
    console.log(chalk.bgWhite(chalk.black('######## Details of Deployed Contract ###########')));
    console.log(chalk.green('Contract Address : ' + deployedContract.options.address));
  
    console.log(chalk.white("######  Method Invocation ########"));
    console.log(chalk.yellow('Invoking function getData() on contract : ' + deployedContract.methods.getData()));
    console.log(chalk.green('====== This is just spitting out the code that should be invoked. ======'));
  
    let output = await deployedContract.methods.getData().call();
    console.log(chalk.yellow('Invoking function getData() on contract : ' + output));
}

// main body 
readMethodOfContract(contract);