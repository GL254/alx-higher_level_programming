#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info on Python lists
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *o;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		o = PyList_Getltem(p, i);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
