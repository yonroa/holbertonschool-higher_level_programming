#include "lists.h"
/**
 * check_cycle - Check if the list has a cycle
 * @list: list to be checked
 * Return: 1 if has a cycle, 0 if has not
 */
int check_cycle(listint_t *list)
{
	int tmp = list->n;
	list = list->next;

	while (list->next != NULL)
	{
		if (list->n == tmp)
			return (1);
		list = list->next;
	}
	return (0);
}
