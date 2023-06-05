#include "lists.h"

/**
* check_cycle - checks if a linked list has a cycle
* @list: Linked list
* Return: 1 if the linked list has a cycle, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *slow_node = list;
	listint_t *fast_node = list;

	if (!list)
		return (0);

	while (slow_node && fast_node && fast_node->next)
	{
		slow_node = slow_node->next;
		fast_node = fast_node->next->next;

		if (slow_node == fast_node)
			return (1);
	}
	return (0);
}
