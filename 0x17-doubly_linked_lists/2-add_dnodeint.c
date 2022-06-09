#include "lists.h"

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *temp, *new;

	new = malloc(sizeof(dlistint_t));

	if (*head == NULL)
	{
		*head = new;
		new->prev = 0;
	}

	temp = *head;
	temp->n = n;
	new->next = 0;

	while (temp != NULL)
	{
		temp->next = new;
		new-> prev = temp;

		temp = temp->next;
	}

	return (*head);
}

