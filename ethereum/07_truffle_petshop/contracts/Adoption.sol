pragma solidity >=0.4.0 <0.6.0;

contract Adoption {
    address[16] public adopters;

function adopt(uint petId) public returns (uint) {
  require(petId >= 0 && petId <= 15, "Only 16 Pets available");
  adopters[petId] = msg.sender;
  return petId;
  }

function getAdopters() public view returns (address[16] memory) {
  return adopters;
  }
}