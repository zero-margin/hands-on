using System;
using System.Text;
using System.IO;
using System.Text.Encodings;
using Org.BouncyCastle.Crypto;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.OpenSsl;
using Org.BouncyCastle.Security;
using System.Security.Cryptography;


namespace DotNetCore
{
    class Program
    {
        static void Main(string[] args)
        {
            string data = RunEncryption("This is test data", false);
            Console.WriteLine(data);
            RunDecryption(data, false);
        }
        
        public static RSACryptoServiceProvider PrivateKeyFromPemFile (String filePath){ 
            using (TextReader privateKeyTextReader = new StringReader(File.ReadAllText(filePath, Encoding.UTF8)))  
            {  
                // AsymmetricCipherKeyPair readKeyPair = (AsymmetricCipherKeyPair)new PemReader(privateKeyTextReader).ReadObject();  
                // RsaPrivateCrtKeyParameters privateKeyParams = ((RsaPrivateCrtKeyParameters)readKeyPair.Private);  
                RsaPrivateCrtKeyParameters privateKeyParams = (RsaPrivateCrtKeyParameters)new PemReader(privateKeyTextReader).ReadObject();
                RSACryptoServiceProvider cryptoServiceProvider = new RSACryptoServiceProvider();  
                RSAParameters parms = new RSAParameters();  
        
                parms.Modulus = privateKeyParams.Modulus.ToByteArrayUnsigned();  
                parms.P = privateKeyParams.P.ToByteArrayUnsigned();  
                parms.Q = privateKeyParams.Q.ToByteArrayUnsigned();  
                parms.DP = privateKeyParams.DP.ToByteArrayUnsigned();  
                parms.DQ = privateKeyParams.DQ.ToByteArrayUnsigned();  
                parms.InverseQ = privateKeyParams.QInv.ToByteArrayUnsigned();  
                parms.D = privateKeyParams.Exponent.ToByteArrayUnsigned();  
                parms.Exponent = privateKeyParams.PublicExponent.ToByteArrayUnsigned();  
        
                cryptoServiceProvider.ImportParameters(parms);  
                return cryptoServiceProvider;  
            }  
        }

         public static RSACryptoServiceProvider PublicKeyFromPemFile(String filePath){  
            using (TextReader publicKeyTextReader = new StringReader(File.ReadAllText(filePath,Encoding.UTF8)))  
            {  
                RsaKeyParameters publicKeyParam = (RsaKeyParameters)new PemReader(publicKeyTextReader).ReadObject();  
                RSACryptoServiceProvider cryptoServiceProvider = new RSACryptoServiceProvider();  
                RSAParameters parms = new RSAParameters();  
                parms.Modulus = publicKeyParam.Modulus.ToByteArrayUnsigned();  
                parms.Exponent = publicKeyParam.Exponent.ToByteArrayUnsigned();  
                cryptoServiceProvider.ImportParameters(parms);  
                return cryptoServiceProvider;  
            }  
        }

        static public string RunEncryption(String input, bool DoOAEPPadding){  
        String response="";
        try  
            {
                
                // UnicodeEncoding ByteConverter = new UnicodeEncoding();
                byte[] data = Encoding.UTF8.GetBytes(input);;
                byte[] encryptedData;  
                using (RSACryptoServiceProvider RSA = PublicKeyFromPemFile(@"./keys/public_key.pem"))  
                {  
                     // RSA.ImportParameters(RSAKey);  
                    encryptedData = RSA.Encrypt(data, DoOAEPPadding);
                    response = Convert.ToBase64String(encryptedData);
                } 
                }  
                catch (CryptographicException e)  
                {  
                    response = e.Message;
                }  
                return response;
        } 
        
        static public void RunDecryption(String input, bool DoOAEPPadding) {
            byte[] data = Convert.FromBase64String(input);
            byte[] decryptedData ;
            using (RSACryptoServiceProvider RSA = PrivateKeyFromPemFile(@"./keys/private_key.pem"))  
                {
                    decryptedData = RSA.Decrypt(data,DoOAEPPadding ) ;
                    Console.WriteLine(System.Text.Encoding.UTF8.GetString(decryptedData));
                } 
        } 
    }
}