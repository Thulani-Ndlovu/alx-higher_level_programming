#include "lists.h"

/**
* insert_node - insert a number in a sorted list
* @head: address of the linked list
* @number: number being added to the list
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *_n = *head;
	listint_t *tmp = malloc(sizeof(listint_t));

	if (tmp == NULL)
		return (NULL);
	tmp->n = number;

	if (_n == NULL || _n->n >= number)
	{
		tmp->next = _n;
		*head = tmp;
		return (tmp);
	}
	while (_n && _n->next && _n->next->n < number)
	{
		_n = _n->next;
	}
	tmp->next = _n->next;
	_n->next = tmp;
	return (tmp);
}
