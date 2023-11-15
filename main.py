correo = "foo@foo.com"
nombre = "foozy"
correos = ["bar@bar.com","baz@baz.com","qux@qux.com"]


for valor in (correos):
    print(valor)


print(correo)
print(nombre)
print(correos)


entrada = "bronce"

if entrada == "oro" or entrada == "plata":
    print("puedes entrar")
else:
    print("no puedes entrar")


limite = len(correos)
print(limite)

edad= 30
entrada = "oro"

def verificar_persona(edad, entrada):
    if edad >=30 and entrada == "oro":
        print("puedes entrar")

    else:
        print("no puedes entrar")

verificar_persona(edad, entrada)
    
perfil_usuario = {"correo":"foo@foo.com","nombre":"foo","planeta":"tierra"}

copia = perfil_usuario.copy()

del copia["correo"]
copia["nombre"] = "bar-copia"

print(perfil_usuario)

print(copia)


lista_a = ["a","b","c"]
lista_b = [*lista_a,"d","e"]

print(lista_b)


perfil_a = {"nombre":"foo","correo":"foo@foo.com"}

perfil_b = {**perfil_a}

print(perfil_b)


tupla_a = ("foo","baz","qux")
tupla_b = ("bax",*tupla_a)
print(tupla_b)


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

edad = 25

if edad > 21:
    print("true")

else:
    print("false")

mensaje = "hola desde python"

def mensaje():
    print("hola desde python")

mensaje()

edad = 18

if edad > 25 or edad == 18:
    print("true")

else:
    print("false")    


lista = ["foo","bar","baz","qux"]

print(lista[2])

nombre = "foo"
edad = 25

if nombre == "bar" and edad >=21:
    print("true")

else:
    print("false")    



nombre = "foo"

if nombre != "foo":
    print("true")

else:
    print("false")    