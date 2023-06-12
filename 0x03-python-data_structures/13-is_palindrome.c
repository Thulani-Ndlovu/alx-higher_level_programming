#include "lists.h"

/**
* list_size - returns the size of the list
* @head: pointer to the head of the list
* Return: the size of the list
*/

int list_size(listint_t **head)
{
	listint_t *node = *head;
	int size = 0;

	while (node)
	{
		size++;
		node = node->next;
	}
	return (size);
}

/**
* is_palindrome - checks if a linked list is a palindrome
* @head: head node of the list
* Return: 1 if palindrome, otherwise 0
*/

int is_palindrome(listint_t **head)
{
	listint_t *iter = *head, *comp = *head;
	int _size = list_size(head);
	int list_copy[_size];
	int i = 0, counter = 0, j;

	while (iter)
	{
		list_copy[i] = iter->n;
		i++;
		iter = iter->next;
	}

	for (j = _size - 1; j > -1; j--)
	{
		if (comp->n == list_copy[j])
			counter++;
		else
			break;
		comp = comp->next;
	}
	if (counter == _size)
		return (1);
	return (0);
}
