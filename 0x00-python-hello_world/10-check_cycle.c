#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: Is the linked list to check
 *
 * Return: 1 if a loop has a cycle, 0 if it does not
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
