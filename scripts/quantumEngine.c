#include <stdio.h>
#include <stdlib.h>

int main(int ac, char** av) {
	if (ac < 2) return (printf("No circuit number was provided.\n"));
	int cNumber = atoi(av[1]);
	if (cNumber < 0) return (printf("Please provide a positive number you quantum toot.\n"));
	if (cNumber > 20000) return (printf("\n"));
}
