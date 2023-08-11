#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node to the list
 * @head: start of list
 * @number: node to insert
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	listint_t *new_node;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
	}
	new_node->next = ptr->next;
	ptr->next = new_node;

	return (new_node);
}
