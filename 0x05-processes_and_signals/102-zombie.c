#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Keeps running until zombies are dead
 *
 * Return: 0 on success
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	infinite_while();
	return (0);
}