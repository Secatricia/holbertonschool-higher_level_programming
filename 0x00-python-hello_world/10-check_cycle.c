#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check the code
 *
 * Return: Always 0.
 */

int check_cycle(listint_t *list)
{
	int j = 0;
	int adresse_head[40];
	while (list->next != NULL || adresse_head[j] != &list)
	{
		while(adresse_head[j])
		{
			adresse_head[j] = &list;
			*list = *list->next;
			j++;
		}
	}
	if (adresse_head[j] == &list)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}