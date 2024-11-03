# Árbol Genealógico Interactivo en Python

Este proyecto es una aplicación en Python para construir y gestionar un árbol genealógico de forma interactiva. La aplicación permite al usuario empezar desde un miembro raíz y añadir familiares de manera progresiva, estableciendo relaciones entre padres, hijos, y hermanos. También permite visualizar gráficamente el árbol genealógico y consultar la relación más cercana entre dos miembros.

## Funcionalidades Principales

1. **Agregar miembro raíz**: Inicia el árbol genealógico con un miembro raíz que será el primer miembro de la familia.
2. **Agregar padres**: Permite asignar un padre o madre a un miembro ya existente en el árbol.
3. **Agregar hijos**: Agrega un hijo a un miembro y establece una conexión de descendencia.
4. **Agregar hermanos**: Agrega un hermano a un miembro existente, asegurándose de que ambos comparten padres.
5. **Buscar relación**: Calcula la relación más cercana entre dos miembros del árbol (hermanos, primos, etc.), basándose en el camino más corto entre ellos en el grafo.
6. **Visualizar árbol**: Muestra una representación gráfica del árbol genealógico utilizando `matplotlib` para visualizar los nodos y las conexiones.

## Requisitos

Para ejecutar este proyecto, necesitas tener Python y las siguientes bibliotecas instaladas:

- `networkx` para la manipulación de grafos.
- `matplotlib` para la visualización gráfica del árbol.

Para instalar las bibliotecas, ejecuta:

```bash
pip install networkx matplotlib
