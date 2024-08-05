
while True:
    
    print("Oprima 2 para dirigirse al ejercicio 2")
    print("Oprima 3 para dirigirse al ejercicio 3")
    print("Oprima 4 para dirigirse al ejercicio 4")
    print("Oprima 5 para dirigirse al ejercicio 5")
    print("Oprima 6 para dirigirse al ejercicio 6")
    print("Oprima 7 para dirigirse al ejercicio 7")
    print("Oprima 8 para dirigirse al ejercicio 8")
    print("Oprima 9 para dirigirse al ejercicio 9")
    print("Oprima 10 para dirigirse al ejercicio 10")
    
    opcion = int(input())
    
    if (opcion == 2):
      print("""Para la realizacion de este ejercicio para mostar los numeros primos en el rango de 1 y un numero dado por el usuario, se realizaron los siguientes pasos:

1) Se crea la variable num en la cual se le va a pedir al usuario que ingrese un numero.

2) Debemos anadir dos variables e igualarlas a 0, esta son cont y suma.

3) Establecemos el ciclo for i in range (1, num + 1). Luego debemos volver a igualar cont a 0.

4) Creamos otro ciclo for j in range (1, i +1). Aqui establecemos una condición en la cual si el residuo de j dividido i es igual a 0, cont va a aumentar de uno en uno. 

5) Fuera del ciclo anadimos otro condicional en el cual si cont es igual a 2, a la variable suma aumenta en i. 

6) Por ultimo mediante el siguiente print mostrams el resultado: print(f"Los numero primos son: {i}"). Aqui apareceran todos los numeros que son primos indicados en cierto rango.
""")
    
    elif (opcion == 3):
      print("""Para la realizacion de este ejercicio para saber a que equivale cada uno los numeros en el rango (1, 10) en nuemros romanos se realizaron los siguientes pasos:

1) Se crea la variable num la cual mediante un input nos va pedir escribir un numero del 1 al 10.

2) Establecemos el condicional if enla cual igualamos el num a 1, si esta condicion es verdadera se ejecutara un printa el cual menciona que el numero expresado en romanos es y aqui aprecera su equivalencia. 

3) Dado el caso de no cumplirse  debemos tener establecidos 9 elif cada uno con su condicion igualandola a un numero difente siguiendo la secuencia de los numeros del 1 al 10 y en caso al print cambiaria el valor en cuant a los numeros romanos

4) Llegado el caso que nuguno de estos concionales se cumpliera anadimos un else el cual va indicar mendintae un print que el numero ingresado es invalido.
""")

    elif (opcion == 4):
      print("""Para la realizacion de este ejercicio para sumar pares e impares se realizaron los siguientes pasos: 

1) Debemos igualar las variables suma_pares y suma_impares a 0.

2) Mediante un for establecemos lo siguiente: for i in range(1,101 + 1); despues con el uso de condicionales estblecemos si i%2 == 0 y de ser correcto : suma_pares += i, para luego mediante un print mostrar la suma de los numeros pares. 

3) Seguidamente implementamos otro for estableciendo lo mismo que en el anterior for solo que en la condicional cambia puesto que ahora vamos a sumar los numeros pares, entonces: if i%2 != 0 y de ser correcto: suma_impares += i. finalmente establecemos un print para mostrar la suma de los numeros impares. 
""")

    elif (opcion == 5):
      print("""Para la realizacion de este ejercicio para calcular el valor total del alquiler de un auto con el impuesto del IVA. Se realizaron los siguientes pasos:

1) Creamos una variable la cual vamos a llamar kilometros y mediante esta establecemos un input pidiendo ingresar los kilometros recorridos por el auto. 

2) Mediante un condicional establecemos lo siguiente : if kilometros < 300; aqui vamos a igualar al variable valor a 300000. 

3) Implementamos dos condicionales mas, el primero: elif kilometros >=300 and kilometros < 1000, estableciendo la variavble valor de la siguiente manera: valor = 300000 + 15000 * (kilometros -300). Posterior a ello mediante la suguiente condición: elif kilometros > 1000 , la variable valor tomaria esto: valor = 300000 + 15000 * (kilometros - 300) + 10000 * * (kilometros - 1000). 

4) Igualamos la variable valor_sin_impuesto a valor, luego calculamos el iva: IVA = valor_sin_impuesto * 0.20 y finalmente caculamos el total a pagar: total_a_pagar = valor_sin_impuesto + IVA. 

5) Mediante un print mostramos el total a pagar por el cliente al alquilar el auto. 
""")

    elif (opcion == 6):
      print("""Para la realizacion de este ejercicio para saber cual el ahorro total al cabo de un anio teniendo en cuenta que cada mes ahorra cantidades variables de dinero. Se realizaron los siguientes pasos:

1) Igualamos la variable ahorro_total a 0.

2) Implementamos el bucle for: for mes in range(1,13). Denrtro de este creamos una variable la cual vamos a llamar deposito mediante la cual vamos a pedir al  usuario ingresar la cantidad de dinero depositada cada mes. 

3) Ala variable que igualamos a 0 vamos a sumarle lo que el usuario vaya ingresando en el deposito: ahorro_total += Deposito. Luego mediante un print el cual va mostran el ahorro total de cada mes a medida de que se va incrementando en el transcurso de los 12 meses del anio.

4) Se cierra el bucle y fuera de este establecemos otro print el cual nos va a mostrar cual es el arro total luego de trancurrir un anio. 
""")

    elif (opcion == 7):
      print("""Para la realizacion de este ejercicio la cual consiste en realizar un cronometro se realizaron los siguientes pasos: 

1) Debemos importar time y importar os, time es para que nos muetre en tiempo real y os es para limpiar pantalla, es decir que cuando ejecutemos en consola solo aparecera el cronometro. 

2) Establecemos tres for: for hora in range(24), dentro de este: for minuto in range(60) y detro de este : for segundo in range(60). Ahora dentro de esta for anadimos lo siguiente: os.system('cls'), el cual nos permitira limpiar pantalla, luego mediante un print vamos a mostrar el cronometro: print(f"{hora}:{minuto}:{segundo}"). y ya para finalizar el bucle establecemos time.sleep(1) para que luego de un segundo se ejcute el cronometro. 
""")

    elif (opcion == 8):
      print("""Para la realizacion de este ejercicio para saber cuantos multiplos de 3 hay en un rango de (1 ,n) se realizaron los siguientes pasos:

1) Creamos una variable a la cual llamamos n y vamos a pedir que el usuario ingrese un numero mediante un input.

2) andimos la variable cont y la igualamos a 0. 

3) Mediante un ciclo establecemos lo siguiente: for i in range(1,n + 1). Despues utilizando un condicional vamos a verificar si el residuo de un numero dividio¿do entre 3 es igual a 0, de ser asi cont += 1, es decir, contador aumenta en uno cada vez que el residuo  de la división sea 0. Mediante un print imprimimos los multiplos de 3. 

4) Fuera del ciclo establecemos un print: print(f"Entre 1 y {n} hay {cont} multiplos de 3.")
""")

    elif (opcion == 9):
      print("""Para realizar este ejercicio se realizaron los siguientes pasos: 

1) Se nombra una variable la cual pide ingresar el numero para calcular la tabla de multiplicar. 

2) Mediante el ciclo for establecemos un item, en este caso la llamamos i en un rango de (1,11).

3) Se nombra la variable resultado para calcular la operacion en dicho rango.

4) Imprimimos  la tabla de multiplicar estableciendo lo siguiente en el print({num} * {i} = {resultado}).
""")

    elif (opcion == 10):
      print("""Para la realizacion de este ejercicio se realizaron los siguientes pasos:

FUNCIONALIDAD 1 : REGISTRAR USUARIO

1) Establecemos una lista vacia la cual vamos a llamar datos.

2) Luego establecemos un print mediante el cual vamos a mostarr el mensaje de resgitro de usuario. luego mediante otro print vamos a pedir ingresar el nombre completo y creamos la variable nombre para poder digitar lo que se pide, seguimos estableciendo el siguiente print en cual pedimos ingresar el numero de identificacion y creamos la variable ID implememtando que solo pueda ingresar numero enteros con el caracter int. continuamos pidiendo informacion, pedimos que ingrese su correo electronico  y creamos la variable correo_electronico, ahora le pedimos al usuario que nos defina que tipo de usuario es y creamos la variable tipo_de_usuario para digitarlo. asi mismo vamos pedir ingresar una contrasena ademas debemos crearla variable contrasena para escribirlo y finalmete debemos pedir que ingrese su numero de telefono y creamos la variable telefono utilazndo int para que solo nos permita ingresar valores numericos.

3) Mediante datos.append() vamos poder agregar toda la informacion pedida al usuario en la lista creada inicialmente, debemos añdir 6 datos.append() en total.

4) Utilando un print, mostramos la lista datos y mediante otro mostramos el mensaje de registro exitoso.


FUNCIONALIDAD 2 : AUTENTICACIÓN O INICIO DE SESIÓN

1) Añadimos una lista que llamamos datos escribiendo manualmente los datos pedidos en la funcionalidad anterior: datos = ['Luis Miguel Giron Orozco', 1081729282, 'gironorozcoluisniguel3@gmail.com', 'Aprendiz', 'Luismi321', 3132642980]. 

2) Establecemos dos print : print("Inicio de sesión o autenticación") y print("Ingrese su identificación:") y debajo del est segundo creamos la variable ID estableciendo el int el cual permite ingresar valores que solo sean de tipo numerico. continumos implementando otro print el cual pedirá digitar la contrasena  y luego creamos la variable contrasena para poder digitarla. 

3) Añadimos una condición (if contrasena == datos[4] and ID == datos[1]:), si esta se cumple motrara dos print:print(datos[0], "sus datos son correctos") y print("Iniciando sesión..."). En caso contrario mostrar otros print completamente distintos: print("Lo siento, los datos son incorrectos") y print("Cargando pagina nuevamente...")


FUNCIONALIDAD 3 : RECUPERAR CONTRASENA

1) Establecemos dos print en la cual aparecera recuperar contrasena y en el otro le pedira ingresar el correo electronico. Luego creamos la variable correo para que el usuario lo digite. despes mediante otro print pedira ingresar la nueva contrasena y creamos la variable nueva_contrasena para que la digite y finalmente se le pide que confirme la contrasena y añadimos la variable confirmar para que vuelva a escribir la contrasena.  

2) Implementamos un condicional: if (nueva_contrasena == confirmar), si esto se cumple mostrara un mensaje a través de un print en cual dira que la contrasena ha sido cambiada correctamente. En caso contrario se establece un else el cual mediante un print dira que no hay coincidencia entre las contrasenas.


FUNCIONALIDAD 4 : AJUSTES APRENDIZ

1) Primero que todo se estableciron 4 print : print("Ajustes"), print("¿A donde desea dirigirse?") print("Opcion 1 para configurar la cuenta"), print("Opcion 2 para  las notificaciones de la cuenta") y  print("Opcion 3 para cerrar sesion"), posterir a ello se creo la variable op para seleccionar una de las opciones mencionadas en los print, se establecio int para que solo se puedan digitar valores numericos enteros.

2) Se establece una condicion if(op == 1) para acceder a la configuracion de la cuenta, en la cual si se cumple se imprimiran los siguientes print: print("Cofiguarcion de la cuenta"), print("¿Que desea hacer?"), print("Opcion 1 para configurar login"), print("Opcion 2 para ingresar a las opciones del sistema") y print("Opcion 3 para regresar a ajustes"). Luego creamos la variable selecccion para poder digitar alguna de las opciones mencionadas anteriormente, establecimos inta para que solo ingresara valores numericos enteros.
Seguidamete establecimos un condicional if y dos elif: if(seleccion == 1), elif(seleccion == 2) y elif(seleccion == 3). Aqui si se cumple la primera condición se mostraun mensaje mediante un print el cual dira "configurar el login", por consiguiente si no se cumple esta se evaluara el condicional elif y en caso de ser afirmativa se ejcutara y mostrar mediante un print el mensaje de "opciones de sistema", en caso negativo se evaluara el otro condicional elif y si se cumple se ejcutar el print mostrando un mensaje: "Regesando a ajustes...". En caso de que no se cumpa ninguna condición mediante un else y utilizando un print vamos a mostrar el siguiente mensaje:"Debe ingresar una opción válida".

3) En caso de no cumplirse la codicion (if(op == 1)), debemos tener en cunta que establecimos dos condicionales elif : elif (op == 2) y elif (op == 3). Aqui evaluara el primer elif, si se cumple mostrar dos print en la cual se establece las notificaciones de la cuenta: print("Notificaciones de la cuenta") y print("No hay notificaciones"). Si esta condidcion no se cumple se evaluara el siguiente elif en la cual llegando a cumplirse mostrar dos print en al cua se establce el cerrado de sesion: print("Cerrar sesión") y print("¿Seguro que deseas cerrar sesión?"), luego creamos la variable cerrar_sesion para responder "si" o "no". Despues establecemo una concdición: if (cerrar_sesion.lower() == "si"), utilizamos el .lower() para que cuando se ingrese en mayuscula la respuesta automaticamente cambie a minuscula para evaluarla en la condición. Al cumplirse esta condición se mostrará un print con el mensaje "cerrando sesión..." pero si la respuesta no coincide, mediante un else y luego utilizando un print damos el mensaje "Regresando a ajustes..."  

4) si no se cumple ninguna de las condiciones evaluadas: if (op == 1), elif (op == 2) y elif (op == 3), debemos implementar un else y utilizando un print mostramos un mensaje que diga que la opcion seleccionada es incorrecta.
""")

    else:
      print("Seleccione una opción válida.")