#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *tmp = *head;
    listint_t *copy = *head;
    listint_t *copy2 = *head;
    int n_nodes = 0, i = 0;

    if (!head || !*head)
        return (1);
    while (copy)
    {
        n_nodes++;
        copy = copy->next;
    }
    while (i != n_nodes)
    {
        copy2 = copy2->next;
        i++;
    }
    while (tmp && copy2)
    {
        if (tmp->n != copy2->n)
            return (0);
        tmp = tmp->next;
        copy2 = copy2->next;
    }
    return (1);
}