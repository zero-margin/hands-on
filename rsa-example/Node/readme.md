Step 1: Library to be used for the RSA implementation is "https://www.npmjs.com/package/node-rsa"
Step 2: Install node-rsa "npm -install node-rsa --save-dev
Step 3: Navigate to the Key folder
Step 4: Command to Generate Private Key Using OpenSSL "openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048"
Step 5: Generate Public Key from the Private Key generated step 4 "openssl rsa -pubout -in private_key.pem -out public_key.pem"
Step 6: Enabling NodeJS for ECMA 6
Step 7: Install babel dependencies npm i @babel/cli @babel/node @babel/core @babel/preset-env --save-dev
Step 8: Run the program using "npm run start:server"

Reference:
Babel Setup Reference: https://www.codementor.io/@osazeedoosagie/easy-set-up-babel-7-for-nodejs-rg3zak6pj
