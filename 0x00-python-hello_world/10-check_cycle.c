#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Check if a linked list contains a cycle
 * @list: pointer to the first element of a linked list
 * Return: 1 if a cycle is found, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *next_i = NULL, *next_j = NULL;

	next_i = list;
	next_j = list;
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	next_j = next_i->next;
	for ( ; next_j != NULL ;)
	{
		for ( ; next_j != NULL ; )
		{
			if (next_i == next_j)
			{
				return (1);
			}
			next_j = next_j->next;
		}
		next_i = next_i->next;
		next_j = next_i->next;
	}
	return (0);
}
