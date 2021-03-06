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
    // RSAES-PKCS1-V1_5, RSA-OAEP
    const encrypted = forge.util.encode64(key.encrypt(data, 'RSAES-PKCS1-V1_5', {
        md: forge.md.sha256.create(),
        mgf1: forge.mgf1.create()
    }));
    console.log(encrypted);
    console.log(Buffer.byteLength(encrypted, 'utf-8'));


    const privateKeyPath = './keys/private_key.pem';
    const privateKey = fs.readFileSync(privateKeyPath,'utf-8');
    const pkey = forge.pki.privateKeyFromPem(privateKey);

    const encryptedData ='wZ9Iy3+Z6VawL6rzHN3KaFIHx31ZrINtNB2+uHgtFwnr9sn7deXKfeRRvcmIx2l0WViGkFWsbN7ZChycvYb9U7JzoihhCpqjDfSshq5u374ueE71fOTvIE+OG8zn0VkIgEmsnTol0z/WbdVuSzSWzaq79YE5tNReiOXHD5LXkytRrrIfMxiSv7MoQhRsL2tl5ZzTOyUoaYmEZeDQUrMNACZU5C48oMZEE2dJ+MwzkKG+CEeXHi2JRosygvcrcx8+Sniqs9oaI+cLuoZ6mbszIxzdX751rysbvSJmmtf8yj5OUEvs/pJZsQkmTXLUnzBOSVo1y0VH5/uk9znrvweXJw=='
    // console.log(Buffer.byteLength(encryptedData, 'utf-8'));
    console.log(pkey.decrypt(forge.util.decode64(encryptedData), 'RSAES-PKCS1-V1_5', {
        md: forge.md.sha256.create(),
        mgf1: forge.mgf1.create()
    }));
}


// encryptAndDecryptStringWithRSA("This is test");
encryptAndDecryptForge("ILN | IsPSS | encrypted_id | timestamp | total_amount | currency | country | language | sales_assistant");