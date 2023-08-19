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
	int len, i, len1, j;
	listint_t *ptr, *temp;

	for (len = 0, temp = *head; temp; len++, temp = temp->next)
		;
	len1 = len;
	for (i = 0, temp = *head; i < len1 / 2; i++, temp = temp->next, len1--)
	{
		for (ptr = *head, j = 0; j < len1 - 1; j++, ptr = ptr->next)
			;
		if (ptr->n != temp->n)
			return (0);
	}
	return (1);
}
