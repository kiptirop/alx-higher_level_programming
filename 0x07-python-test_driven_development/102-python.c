#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string
 *
 * @p: Pointer to a Python string object
 *
 * Description:
 *   This function prints the length, memory address, and contents of a Python string
 *   object passed as a PyObject pointer.
 *
 * Return: None
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t size;
    wchar_t *str;
    char *type;

    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "TypeError: object is not a Python string\n");
        return;
    }

    size = PyUnicode_GET_LENGTH(p);
    str = PyUnicode_AsWideCharString(p, &size);
    type = (char *)(PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "unicode object");

    printf("'%s' is a %ld character %s object at address %p\n", PyUnicode_AsUTF8(p), size, type, (void *)p);
    printf("  type: %s\n", Py_TYPE(p)->tp_name);
    printf("  object address: %p\n", (void *)p);
    printf("  string length: %ld\n", size);
    printf("  memory address: %p\n", (void *)str);
    printf("  string contents: %ls\n", str);

    PyMem_Free(str);
}
