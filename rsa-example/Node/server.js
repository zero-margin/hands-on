import nodersa from 'node-rsa';
import forge from 'node-forge';
import fs from 'fs';

function encryptAndDecryptStringWithRSA(data){
    const publicKeyPath = './keys/public_key.pem';
    const publicKey = fs.readFileSync(publicKeyPath,'utf-8');

    const key = new nodersa(publicKey);
    const enrcypted = key.encrypt(data, 'base64');
    console.log(enrcypted);

    const privateKeyPath='./keys/private_key.pem'
    const privateKey = fs.readFileSync(privateKeyPath, 'utf-8');

    const pkey=new nodersa(privateKey);
    const decrypted = pkey.decrypt(enrcypted, 'utf-8');
    console.log(decrypted);

}

function encryptAndDecryptForge(data){
    const publicKeyPath = './keys/public_key.pem';
    const publicKey = fs.readFileSync(publicKeyPath,'utf-8');

    const key = forge.pki.publicKeyFromPem(publicKey);
    const encrypted = forge.util.encode64(key.encrypt(data, 'RSA-OAEP', {
        md: forge.md.sha256.create(),
        mgf1: forge.mgf1.create()
    }));
    console.log(encrypted);

    const privateKeyPath = './keys/private_key.pem';
    const privateKey = fs.readFileSync(privateKeyPath,'utf-8');
    const pkey = forge.pki.privateKeyFromPem(privateKey);

    console.log(pkey.decrypt(forge.util.decode64(encrypted), 'RSA-OAEP', {
        md: forge.md.sha256.create(),
        mgf1: forge.mgf1.create()
    }));
}


// encryptAndDecryptStringWithRSA("This is test");
encryptAndDecryptForge("This is second test");