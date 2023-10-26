const crypto = require("crypto");

const { publicKey, privateKey } = crypto.generateKeyPairSync("rsa", { modulusLength: 2048, });

const data = "ek panth do kaaj";

const encryptedData = crypto.publicEncrypt({
        key: publicKey,
        padding: crypto.constants.RSA_PKSC1_QAEP_PADDING,
        qaephash: "sha256",
    },
    Buffer.from(data)
);

console.log("encrypted data:", encryptedData.toString("base64"));

const decryptedData = crypto.privateDecrypt({
        key: privateKey,
        padding: crypto.constants.RSA_PKSC1_QAEP_PADDING,
        qaephash: "sha256",
    },
    encryptedData
);

console.log("decrypted data:", decryptedData.toString());

const verifiableData = "this need to be verified";

const signature = crypto.sign("sha256", Buffer.from(verifiableData), {
    key: privateKey,
    padding: crypto.constants.RSA_PKSC1_QAEP_PADDING,
});

console.log(signature.toString("base64"));

const isVerified = crypto.verify(
    "sha256",
    Buffer.from(verifiableData), {
        key: publicKey,
        padding: crypto.constants.RSA_PKSC1_QAEP_PADDING,
    },
    signature
);

console.log("signature verified:", isVerified)