#include "lists.h"
/**
 * is_palindrome - function that checks if a single linked list is a palindrome
 * @head: pointer to the single list
 * Return: 1 if not a palindrome, 0 otherwise
**/

int is_palindrome(listint_t **head)
{
	int idx, i, j, a, b;
	listint_t *temp = *head, *ptr_i = *head, *ptr_j = *head;

	if (head == NULL || temp->next == NULL)
	{
		return (1);
	}
	a = temp->n;
	for (idx = 0 ; temp != NULL ; idx++)
	{
		b = temp->n;
		temp = temp->next;
	}
	if (a == b)
	{
		for (i = 0 ; i < (idx + 1) / 2 ; i++)
		{
			ptr_i = ptr_i->next;
			a = ptr_i->n;
			for (j = 0; j < idx - i - 1 ; j++)
			{
				b = ptr_j->n;
				ptr_j = ptr_j->next;
			}
			if (a != b)
			{
				return (0);
			}
			ptr_j = *head;
		}
		return (1);
	}
	return (0);
}
