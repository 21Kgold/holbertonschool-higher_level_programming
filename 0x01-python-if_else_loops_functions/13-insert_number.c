#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a node at the begining of a single linked list.
 * @head: pointer to the first node of the linked list
 * @number: int data to include in the inserted node
 * Return: pointer to the inserted node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *temp, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	temp = *head;
	for (; temp->n < number ;)
	{
		current = temp;
		temp = temp->next;
	}
	new->n = number;
	new->next = temp;
	current->next = new;
	return (new);
}
