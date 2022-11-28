import wikipedia as wiki

#paginas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
paginas = ["a", "b", "c"]
cuenta = 0

for pagina in paginas:
    texto = wiki.page(pagina)
    cuenta = cuenta + 1
    if cuenta%2 != 0:
    #if cuenta < 6:
        nombre = "carpetaUno/" + pagina + ".txt"
    else:
        nombre = "carpetaDos/" + pagina + ".txt"
    print(nombre + " - " + str(cuenta))
    f = open(nombre, "w", encoding="utf-8")
    f.write(str(cuenta) + ".txt" + "\n")
    f.write(texto.content)
    f.write("\n")
    f.close()
