#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;

	while (temp != NULL)
	{
		if (temp->next == list)
			return (1);

		temp = temp->next;
	}

	return (0);
}
