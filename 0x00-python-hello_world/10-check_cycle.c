#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Check if a linked list contains a cycle
 * @list: pointer to the first element of a linked list
 * Return: 1 if a cycle is found, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	int i, j;
	listint_t *next_i, *next_j;

	next_i = list->next;
	next_j = list->next;
	for (i = 0 ; next_i != NULL ; i++)
	{
		for (j = 0 ; next_j != NULL ; j++)
		{
			if (next_i == next_j)
			{
				if (i == j)
				{
					next_j = list->next;
					continue;
				}
				else
				{
					return(1);
				}
			}
			next_j = list->next;
		}
		next_i = list->next;
	}
	return(0);
}
