# Gestión de Clientes - Axanet

Aplicación desarrollada para la empresa ficticia **Axanet**, proveedora de servicios de manufactura, con el fin de automatizar la gestión de sus clientes usando Python, GitHub y GitHub Actions.

## Objetivo del Proyecto

Desarrollar una solución en Python capaz de:

- Crear archivos de clientes nuevos.
- Consultar y modificar la información de clientes existentes.
- Eliminar registros si es necesario.
- Asociar cada cliente con su archivo utilizando **tablas hash (diccionarios)**.
- Simular la colaboración entre varios usuarios del equipo.
- Automatizar tareas clave mediante **GitHub Actions**.

---

## Tecnologías Utilizadas

- Python 3
- Git + GitHub
- GitHub Actions
- JSON (para almacenamiento de datos)

---

## Funcionalidades del Programa

El script principal permite:

- Crear un nuevo cliente (genera archivo JSON con sus datos).
- Agregar servicios a un cliente recurrente.
- Consultar los datos de un cliente por nombre.
- Ver la lista de todos los clientes.
- Eliminar registros de clientes existentes.

Los datos se almacenan en la carpeta `clientes/` como archivos `.json`.
