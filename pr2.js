const SHA256 = require('crypto-js/sha256')
class Block {
    constructor(index, timestamps, data, previousHash = '') {
        this.index = index;
        this.timestamps = timestamps;
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
        this.nounce = 0;
    }
    calculateHash() {
        return SHA256(this.index + this.previousHash + this.timestamps + JSON.stringify(this.data) + this.nounce).toString();
    }
    mineBlock(difficulty) {
        while (this.hash.substring(0, difficulty) !== Array(difficulty + 1).join("0")) {
            this.nounce++;
            this.hash = this.calculateHash();
        }
        console.log("Block Mined :" + this.hash);
    }
}
class mining {
    constructor() {
        this.chain = [this.createGenesisisBlock()];
        this.difficulty = 4;
    }
    createGenesisisBlock() {
        return new Block(0, "09/09/2022", "Genesis Block", "0");
    }
    getLatestBlock() {
        return this.chain[this.chain.length - 1]
    }
    addBlock(newBlock) {
        newBlock.previousHash = this.getLatestBlock().hash;
        newBlock.mineBlock(this.difficulty);
        this.chain.push(newBlock);
    }
}
let PRCoin = new mining();
console.log("Mining Block 1...");
PRCoin.addBlock(new Block(1, "08/08/2023", { amount: 6 }));
console.log("Mining Block 2...");
PRCoin.addBlock(new Block(2, "09/09/2023", { amount: 10 }));