const DS = artifacts.require("./DataStorage.sol");

module.exports = function(deployer) {
  deployer.deploy(DS);
};