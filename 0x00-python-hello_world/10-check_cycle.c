#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it does not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);
	fast = list->next->next;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
