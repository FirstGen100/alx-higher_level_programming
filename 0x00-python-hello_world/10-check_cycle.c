#include "lists.h"
/**
 * check_cycle - check if there is a cycle in the list
 * @head: start if list
 * Return: 1(cycle present)
 */
int check_cycle(struct listint_s *head)
{
	struct listint_s *slow = head;
	struct listint_s *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
