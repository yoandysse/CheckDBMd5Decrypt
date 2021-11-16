# CheckDBMd5Decrypt
Este script permite buscar hashes en la web md5decrypt.net a través de su API.

Si no se introduce ningún parámetro, se pedirá al usuario que introduzca los datos.
        
NOTA: Crea una cuenta en https://md5decrypt.net/ para obtener tu código.


    Uso: python3 CheckDBmd5Decrypt.py  [[hash] | [-f FILE]] [email] [code]
        
        Opciones:
         hash: hash a buscar
         file: archivo con hashes
         email: email de la cuenta premium
         code: código de la cuenta premium
        
        Ejemplo: python3 CheckDBmd5Decrypt.py e10adc3949ba59abbe56e057f20f883e corre@dominio.com 123456