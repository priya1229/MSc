const SHA256 = require('crypto-js/sha256')
class Block {
    constructor(index, timestamps, data, previousHash = '') {
        this.index = index;
        this.timestamps = timestamps;
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
    }
    calculateHash() {
        return SHA256(this.index + this.previousHash + this.timestamps +
            JSON.stringify(this.data)).toString();
    }
}
class Blockchain {
    constructor() {
        this.chain = [this.createGenesisisBlock()];
    }
    createGenesisisBlock() {
        return new Block(0, "01/01/2017", "Genesis Block", "0");
    }
    getLatestBlock() {
        return this.chain[this.chain.length - 1]
    }
    addBlock(newBlock) {
        newBlock.previousHash = this.getLatestBlock().hash;
        newBlock.hash = newBlock.calculateHash();
        this.chain.push(newBlock);
    }
    ischainValid() {
        for (let i = 1; i < this.chain.length; i++) {
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1];
            if (currentBlock.hash !== currentBlock.calculateHash()) {
                return false;
            }
            if (currentBlock.previousHash !== previousBlock.hash) {
                return false;
            }
        }
        return true;
    }
}
let PRCoin = new Blockchain();
PRCoin.addBlock(new Block(1, "08/08/2023", { amount: 2 }));
PRCoin.addBlock(new Block(2, "09/09/2023", { amount: 8 }));
console.log("Is Block chain Valid ? " + PRCoin.ischainValid());
console.log("Block Chain Created :\n", JSON.stringify(PRCoin, null, 2));
4

//PRCoin.chain[1].data = { amount: 100}; // tampering the data to check block chain Validity
//console.log("is Block chain Valid ? " + PRCoin.ischainValid());