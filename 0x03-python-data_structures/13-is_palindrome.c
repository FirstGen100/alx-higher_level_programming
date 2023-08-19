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
	listint_t *h_ptr = *head, *t_ptr = *head;
	listint_t *temp = t_ptr;
	listint_t *prev = NULL;

	if (head == NULL || *head == NULL)
		return (1);
	while (h_ptr != NULL && h_ptr->next != NULL)
	{
		h_ptr = h_ptr->next;
		t_ptr = t_ptr->next;
		temp->next = prev;
		prev = temp;
	}
	if (h_ptr != NULL)
		t_ptr = t_ptr->next;
	while (t_ptr != NULL)
	{
		if (t_ptr->n != prev->n)
		{
			return (0);
		}
		t_ptr = t_ptr->next;
		prev = prev->next;
	}
	return (1);
}

