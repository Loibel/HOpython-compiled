# Compiled languages into Python

En este hands-on vamos a practicar cómo llamar a una librería
nuestra desde python. En la carpeta `src/` tienen dos archivos de C.
Para completar este ejercicio tienen que hacer los siguientes pasos:

1. Compilar ambos archivos como objetos separados
2. Construir una librería dinámica que tenga ambos objetos
3. Escribir un script en python que pruebe **todas** las funciones
de la librería


#1
gcc -c -fPIC add_two.c
gcc -c -fPIC arrays.c

#2
gcc -shared arrays.o add_two.o -o libmymath.so
