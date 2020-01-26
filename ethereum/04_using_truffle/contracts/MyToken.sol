pragma solidity >=0.4.0 <0.6.0;

contract MyToken {
  address public creator;
  uint256 public totalSupply;
  mapping (address => uint256) public balances;

  constructor() public {
    creator = msg.sender;
    totalSupply = 10000;
    balances[creator] = totalSupply;
  }

  function balanceOf(address owner) public view returns(uint256) {
    return balances[owner];
  }

  function sendTokens(address receiver, uint256 amount) public returns(bool) {
    address owner = msg.sender;
    require(amount > 0, "Amount has to be greater than zero");
    require(balances[owner] >= amount, "Owner balance has to be greater than zero");
    balances[owner] -= amount;
    balances[receiver] += amount;
    return true;
  }
}