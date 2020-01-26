import Web3 from 'web3';
import chalk from 'chalk';

// setting the connection string
const rpcURL = "http://127.0.0.1:7545";
const web3 = new Web3(rpcURL);

async function GetDetails(){
  let protocolVersion = await web3.eth.getProtocolVersion();
  let coinbase = await web3.eth.getCoinbase();
  let hashRate = await web3.eth.getHashrate();
  let blockNumber = await web3.eth.getBlockNumber();
  let transactionCount = await web3.eth.getBlockTransactionCount(block)
  let block = await web3.eth.getBlock(blockNumber);


  console.log(chalk.yellow("Protocol Version running on the node : ") + chalk.green(protocolVersion));
  console.log(chalk.yellow("Coinbase address for the node : ") + chalk.green(coinbase));
  console.log(chalk.yellow("Get hashrate for the node : ") + chalk.green(hashRate));
  console.log(chalk.yellow("Get blocknumber for the node : ") + chalk.green(blockNumber));
  console.log(chalk.yellow("Get transaction  for the node : ") + chalk.green(transactionCount));
  console.log(chalk.yellow("Get block for the node : ") + chalk.green(JSON.stringify(block)));
}

// Calling the functions
GetDetails();