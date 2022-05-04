#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: First node
 * @number: Number to be inserted
 *
 * Return: The address of the new node, NUll if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new, *tmp2;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	while (tmp && (tmp->n < number))
	{
		tmp2 = tmp;
		tmp2 = tmp->next;
	}
	tmp2->next = new;
	new->next = tmp;
	return (new);
}
