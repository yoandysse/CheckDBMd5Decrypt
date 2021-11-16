import sys
import requests

email = ""
code = ""

def ERROR(message):
    errorCode = {
        "001":"Ha superado las 400 solicitudes autorizadas (contácteme para necesidades superiores).",
        "002":"Hay un error en su par de correo electrónico / código.",
        "003":"Su solicitud contiene más de 400 hashes.",
        "004":"El tipo de hash en la variable $ hash_type no es correcto. Esta variable debe ponerse en minúsculas.",
        "005":"El hash proporcionado no coincide con el tipo de hash proporcionado.",
        "006":"Falta un argumento en su solicitud, o ha escrito incorrectamente uno de ellos.",
        "007":"El código premium proporcionado no corresponde a una cuenta válida o activa.",
        "008":"La variable premium no es correcta, debe ser igual a 1",
        "009":"Tu cuenta premium ha caducado, para seguir usando tu cuenta premium debes tener que volver a comprar tiempo.",
    }
    return errorCode["00"+message[-1]]
    # return message


def md5decrypt(hash, email, code):

    url = "https://md5decrypt.net/en/Api/api.php"
    data = {"hash": hash, "hash_type": "md5", "email": email, "code": code}
    response = requests.get(url, params=data)
    # print(requests.get(url, data=data).request.body) # debug
    if response.status_code == 200:
        if "ERROR" in response.text:
            return ERROR(response.text)
        elif response.text == "":
            return "Hash no encontrada"
        else:
            return "Hash encontrada: {}:{} ".format(hash, response.text)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    if len(sys.argv) == 1:
        hash = input("Introduce el hash: ")
        email = input("Introduce tu email: ")
        code = input("Introduce tu código: ")
        print(md5decrypt(hash, email, code))
    elif len(sys.argv) == 2 and sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("""
        Uso: python main.py [hash] [email] [code]
        Ejemplo: 
            python main.py e10adc3949ba59abbe56e057f20f883e corre@dominio.com 123456
        """)

    # print(len(sys.argv))
    # hash = sys.argv[1]
    # email = sys.argv[2]
    # code = sys.argv[3]
    #
    # print(sys.argv[1], sys.argv[2], sys.argv[3])
    # hash = "835ac0b7b5436c89b9813729148632e7"
    # email = "cuentasdetodo0101@yopmail.com"
    # code = "2df06d48c27f1511"
    # print(md5decrypt(hash, email, code))


