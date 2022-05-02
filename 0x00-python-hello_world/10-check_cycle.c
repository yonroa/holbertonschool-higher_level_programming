#include "lists.h"
/**
 * check_cycle - Check if the list has a cycle
 * @list: list to be checked
 * Return: 1 if has a cycle, 0 if has not
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	if (!list)
		return (0);
	while (tmp->next != NULL)
	{
		tmp = tmp->next;
		if (list == tmp)
			return (1);
	}
	return (0);
}
