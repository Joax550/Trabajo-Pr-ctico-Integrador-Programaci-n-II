# Food Store - Sistema de Gestión de Pedidos de Comida (Consola)

Aplicación de consola desarrollada en Python para el **Trabajo Práctico Integrador de Programación II (UTN)**. El sistema permite administrar categorías, productos, usuarios y pedidos de un negocio gastronómico aplicando el paradigma de **Programación Orientada a Objetos (POO)**, arquitectura en capas, manejo de excepciones personalizadas y tipado estático (`type hints`).

## 📋 Requisitos Previos e Instalación

* **Lenguaje:** Python **3.12 o superior**.
* **Dependencias:** Módulos de la biblioteca estándar (`abc`, `enum`, `datetime`) y la librería externa **`pwinput`**, utilizada para ocultar la contraseña mediante asteriscos (`*`) durante el inicio de sesión en consola.

Antes de ejecutar el programa por primera vez, instale la dependencia desde la terminal ejecutando:

```bash
pip install pwinput
```

*(Nota: En caso de no tener `pwinput` instalado, el sistema recurrirá automáticamente al módulo nativo `getpass`).*

## 🏗️ Estructura del Proyecto

El código está organizado en tres capas principales con responsabilidades desacopladas (`consola` $\rightarrow$ `servicios` $\rightarrow$ `entidades`):

```text
food_store/
├── entidades/          # Modelo de dominio, herencia (Base), interfaz (Calculable) y validaciones
├── enums/              # Enumerados del sistema (Rol, Estado, FormaPago)
├── excepciones/        # Jerarquía de excepciones personalizadas (FoodStoreError)
├── servicios/          # Lógica de negocio y gestión de colecciones en memoria
├── consola/            # Menús polimórficos por rol y validación de entradas por teclado
├── main.py             # Punto de entrada principal y carga de datos iniciales
└── pruebas.py          # Script de pruebas automatizadas sobre el modelo y los servicios
```

## 💻 Cómo Ejecutar el Proyecto

1. **Abrir una terminal** y ubicarse en la carpeta raíz del proyecto (donde se encuentra `main.py`).
2. **Iniciar el sistema principal** ejecutando:

   ```bash
   python main.py
   ```
   *(En sistemas Linux o macOS puede requerirse el comando `python3 main.py`).*

3. **Ejecutar las pruebas unitarias/funcionales** (opcional, sin menú interactivo):

   ```bash
   python pruebas.py
   ```

## 🔐 Credenciales de Acceso Iniciales

Al iniciar el programa, se precargan en memoria usuarios de prueba junto con categorías y productos de ejemplo:

* **Rol Administrador (Gestión completa - ABM y consultas):**
  * **Mail:** `admin@foodstore.com`
  * **Contraseña:** `admin123`

* **Rol Cliente / Usuario (Solo lectura y seguimiento de pedidos propios):**
  * **Mail:** `juan@foodstore.com`
  * **Contraseña:** `user123`

*(Nota: Al ingresar la contraseña en consola mediante `pwinput`, los caracteres escritos se mostrarán en pantalla enmascarados con asteriscos `*` por seguridad).*

## ⚙️ Características Principales

* **Control de acceso y polimorfismo:** Menús diferenciados (`MenuAdministrador` y `MenuCliente`) instanciados dinámicamente según el rol del usuario autenticado.
* **Persistencia en memoria y baja lógica:** Toda entidad hereda de `Base`, manteniendo trazabilidad temporal y borrado lógico (`eliminado = True`) sin perder integridad referencial en pedidos históricos.
* **Gestión transaccional de pedidos:** Validación preventiva de stock antes de confirmar detalles, cálculo automático de subtotales y totales mediante la interfaz `Calculable`, y restitución de stock ante cancelaciones o bajas.

## 📂 Enlaces de Entrega

* 🎥 **Video Demostración:** https://www.youtube.com/watch?v=olnr6EaHmUE
* 📄 **Informe Técnico (PDF):** [Ver informe del proyecto](./Informe_TPI_Programacion2_FoodStore.pdf)
---
*Desarrollado para la Tecnicatura Universitaria en Programación - UTN.*