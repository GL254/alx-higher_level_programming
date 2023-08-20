#include "lists.h"
/**
 * check_cycle - Checks if a cycle exist in the linked list
 * @list: Is the pointer to the linked list
 *
 * Return: 1 if a cycle exists or 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p = list;
	listint_t *fast_p = list;

	if (list == NULL)
		return (0);

	fast_p = fast_p->next;

	while (slow_p != NULL && fast_p != NULL && fast_p->next != NULL)
	{
		if (fast_p == slow_p)
			return (1);
		fast_p = fast_p->next->next;
		slow_p = slow_p->next;
	}
	return (0);
}
