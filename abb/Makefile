compile:

	clear
	gcc -g -std=c99 -Wall -Wconversion -Wno-sign-conversion -Werror -c pila.c -o pila.o
	gcc -g -std=c99 -Wall -Wconversion -Wno-sign-conversion -Werror -c pila.o abb.c -o abb.o
	gcc -g -std=c99 -Wall -Wconversion -Wno-sign-conversion -Werror -c testing.c -o testing.o
	gcc -g -std=c99 -Wall -Wconversion -Wno-sign-conversion -Werror -c pruebas_alumno.c -o pruebas_alumno.o

run:
	gcc -g -std=c99 -Wall -Wconversion -Wno-sign-conversion -Werror  main.c pila.o abb.o testing.o pruebas_alumno.o -o pruebas
	valgrind --leak-check=full --track-origins=yes --show-reachable=yes ./pruebas
