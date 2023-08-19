#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - check if palindrome exists
 * @head: start of list
 * Return: 1 is palidrome 0 none
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	ptr = *head;

	if (check(*head, ptr))
		return (1);
	else
		return (0);
}
/**
 * check - check for palindrom in list
 * @head: start
 * @temp: pointer
 * Return: 1 if palindrome else 0
 */
listint_t *check(listint_t *head, listint_t *temp)
{
	listint_t *var;

	if (temp == NULL)
		return (head);

	var = check(head, temp->next);
	if (var == NULL)
		return (NULL);
	if (var->n == temp->n && var->next)
		return (var->next);
	else if (var->n == head->n)
		return (var);
	else
		return (NULL);
	return (NULL);
}
