Ethereum

Public any one can join it, any one can mine in it
You do not need to have permissions to do anything
No single person managing the whole network
Upgrades are very tedious and time consuming
No plug and play feature 
    (e.g. change the consensus mechanism, it is really hard)
    etherum internally uses a key value database, you cannot change it
    ethreum is not modular to the extend where we can change things easily
Crowdfunction, ICO, vDice, Augur.net (PRediction market on ethereum)
In case of ethereum processor are Pseudo-Anonymous hiding behind an address

Big Enterprises:
Modularity
Governance
Some sort of structure in terms of who can join the network and who can process the transcations.

Will a bank put their infrastructure on etherum or on open blockchain

They are sharing the data across multiple entities
e.g. Single source of truth available to everyone

Linux foundation ---> Project ----> Hyperledger
identity provider MSP --> member ship service provider
modular ---> plug and play (decide the consensus algorithm you want to use, you can decide on the underlying db you want to use)
Permission ---> am i allowed to do a certain transaction or not.
There is not crypto currency for hyperledger
Then who pays for the transctions




There is not such thing as login in ethereum

Have an address 

Private key ---> Public Key ----> Address

Payload of transction

txObject{
    from: address
    to: address of recipent
    gaslimit:
    gasprice:
    payload: transaction data encodeABI
}


if you are doing a transction, you are paying to get that transction done.
locking and unlocking scripts


sign transcation Object ---> Private key
serialize the transaction

you connect to the ethereum n/w and send it

Wallet -->

Hyperledger ---> you have to prove who you are?
Certificate ----> Certificating authority

Business Network

Actors Producer, Distributors, Health Inspectiors, Logistic
Every actor has certain transaction they can do

logic ---> milk stayed within a certain temperature range


Template this out - class out of this  blueprint ---> multiple objects
{
    Asset -- Milk
    Actors  - different roles
    Transctions - what role can do what
    Logic Part -
}

Notarization

Physical Entity to Digital Entity

Ethereum is ledger level consensus
Hyperledger is transaction level consensus


Ethereum --->
Submit a transaction
Node is going validate the transaction
Add the validation transaction to staging area
Send the transaction to the neighbouring node
Transaction becomes part of the block --> transction is commited ot written to the ledger

(Everybody has same copy of ledger)  - ledger level consensus


Hyperledger 
Business N/W

Actor 1 copy of ledger, Actor 2 copy of ledger and Actor 3 copy of ledger
Actor 1 says i am sending actor 2 20 units of something

Proposal (Sending 20 units to actor 2)

1 - 20 units are with a1
2 - 20 units are with a1  (a1 does owns 20 units)  
    ---> acc to my ledger this transaction is ok
    ---> Provide digital signature for Proposal
    ---> Send back the proposal to 1
3 - 20 units are with a1
    --> acc to my ledger this transaction is ok
    ---> Provide digital signature for Proposal
    ---> Send back the proposal to 1

a2 and a3 have signed the proposal so i am good with transaction

a1 --> submit the proposal along with the ds from a2 and a3 for the proposal to transction node.

a1, a2 and a3 to update the records 

a1 - 0 units
a2 - 20 units, 0 units

[Hyperledger Composer](https://composer-playground.mybluemix.net/login)

_What Remix to is to Ethereum, Hyperleger Composer it is to hyperledger._

BNA ---> Business Network

sample.cto --> Model --> Actors, transctions, events, assests

participants are role Logistics, Supplier, Buyer












