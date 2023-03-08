import os
import fileinput


def create_cert(cert_domain):
    os.mkdir(os.getcwd() + "/" + cert_domain)
    replace_text_file("server.cnf", "<COMMON_NAME>", cert_domain)
    replace_text_file("server.ext", "<COMMON_NAME>", cert_domain)
    generate_server_certs()
    move_generated_files()


def replace_text_file(file, text_to_find, text_to_replace):
    with fileinput.FileInput(file, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_find, text_to_replace), end='')


def generate_server_certs():
    os.system("openssl genrsa -out server.key")
    os.system("openssl req -config server.cnf -new -batch -key server.key -out server.csr")
    os.system(
        "openssl x509 -req -in server.csr  -CA cacert.crt -CAkey ca.key -out server.crt  -CAcreateserial -CAserial serial -days 365 -sha512 -extfile server.ext")


def move_generated_files():
    os.replace("server.crt", os.getcwd() + "/" + cert_domain + "/server.crt")
    os.replace("server.csr", os.getcwd() + "/" + cert_domain + "/server.csr")
    os.replace("server.key", os.getcwd() + "/" + cert_domain + "/server.key")
    os.replace("serial", os.getcwd() + "/" + cert_domain + "/serial")


if __name__ == '__main__':
    cert_domain = input("Enter the Common name for the certificate : ")
    create_cert(cert_domain)
    replace_text_file("server.cnf", cert_domain, "<COMMON_NAME>")
    replace_text_file("server.ext", cert_domain, "<COMMON_NAME>")
