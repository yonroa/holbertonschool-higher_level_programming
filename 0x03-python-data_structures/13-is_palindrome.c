#include "lists.h"
#include <stdio.h>

void reverse_listint(listint_t **head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: List to be checked
 * Return: 1 if is palindrome, 0 if is not
 */
int is_palindrome(listint_t **head)
{
    listint_t *tmp = *head;
    listint_t *copy = *head;
    listint_t *copy2 = *head;
    int n_nodes = 0, i = 0;

    if (*head == NULL || (*head)->next == NULL)
        return (1);
    while (copy)
    {
        n_nodes++;
        copy = copy->next;
    }
    while (i != (n_nodes / 2))
    {
        copy2 = copy2->next;
        i++;
    }
    reverse_listint(&copy2);
    while (tmp && copy2)
    {
        if (tmp->n != copy2->n)
            return (0);
        tmp = tmp->next;
        copy2 = copy2->next;
    }
    return (1);
}

/**
 * reverse_listint - Reverse a linked list
 * @head: List to be reversed
 * Return: The list reversed
 */
void reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}