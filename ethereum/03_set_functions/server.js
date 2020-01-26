import Web3 from 'web3';
import fs from 'fs';
import path from 'path';
const EthereumTx = require('ethereumjs-tx').Transaction;

// Step 1: Setting up the connection string
const rpcURL = "http://127.0.0.1:7545";
const web3 = new Web3(rpcURL);
const contract='0x31d064fb1C9B35E3774F99a62bBA56884224fd8D';

//account from Ganache and private key for the account
const account = '0x78E5Ba19670a66882d40b634b21C3D4C1e1D3437';   
//private key
const privateKey = Buffer.from('b475d8d034c5d513f00d3e93b3ca19a127d403a360c31179008d31d3c4a44124', 'hex');


function getContractObject(contractAddress){
    let abiPath = path.join(__dirname + '/contract/bin/DataStorage.abi');
    let abi = fs.readFileSync(abiPath);

    let deployedContract = new web3.eth.Contract(JSON.parse(abi),contractAddress);
    return deployedContract;
}

async function CreateSignedTransaction(account, privateKey, contract ){
    let transactionCount = await web3.eth.getTransactionCount(account);
    console.log(transactionCount);
    const contractInstance = getContractObject(contract);
    const method_data = contractInstance.methods.setData(15).encodeABI();

    console.log(method_data);

    const txData = { 
            nonce: web3.utils.toHex(transactionCount), 
            gasLimit: web3.utils.toHex(800000), // Raise the gas limit to a much higher amount 
            gasPrice: web3.utils.toHex(web3.utils.toWei('30', 'gwei')),
            to: contract, 
            data: method_data } 
    
    const tx = new EthereumTx(txData, { chain: 'ropsten', hardfork: 'petersburg' });
    tx.sign(privateKey);

    const serializeTx = tx.serialize();
    const raw = '0x' + serializeTx.toString('hex');
 
    let txHash = await web3.eth.sendSignedTransaction(raw);
    console.log(txHash.transactionHash) ;
}

CreateSignedTransaction(account, privateKey, contract);




