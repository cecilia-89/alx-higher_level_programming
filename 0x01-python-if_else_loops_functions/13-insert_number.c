#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	if (*head == NULL)
		exit(EXIT_FAILURE);

	temp = *head;

	while (temp != NULL)
	{
		if (number <= temp->n)
		{
			new = malloc(sizeof(listint_t));

			new->next = temp->next;

			temp->next = new;

			break;
		}

		temp = temp->next;
	}

	return (*head);
}
