# 🧮 Python GUI Calculator (Dark Mode & History)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-00BCD4.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Una calculadora de escritorio **moderna, limpia y minimalista** desarrollada en **Python** y **Tkinter**. Presenta un diseño clásico de sobremesa con chasis oscuro, botones texturizados de alta visibilidad y funciones avanzadas de memoria.

---

## 📸 Vista Previa & Diseño

* **Diseño Flat / Moderno:** Botones cuadrados con alto contraste entre números (azul oscuro) y operadores principales (azul cian/turquesa).
* **Modo Oscuro 🌙:** Selector superior para alternar o indicar el estado del tema visual.
* **Historial Integrado:** Registro en tiempo real de todos los cálculos realizados durante la sesión.
 <img src="Calculadora Python/calculadora actual.jpg" width="200">
---

## ✨ Características Principales

- 🌙 **Modo Oscuro / Tema Moderno:** Interfaz estilizada tipo flat con contraste optimizado para reducir la fatiga visual.
- 📜 **Historial de Operaciones:** Almacena y muestra cada cálculo completado (`ej. 8 * 9 = 72`) para consultar resultados anteriores. **Agregado 30/07/26**.
- ⌫ **Control de Corrección:**
  - **`C`**: Limpia la pantalla por completo.
  - **`<`**: Borra el último carácter introducido.
- 🧮 **Operaciones Esenciales:** Suma (`+`), Resta (`-`), Multiplicación (`*`), División (`/`) y Porcentaje (`%`).
- 📐 **Distribución Adaptable:** Cuadrícula proporcional que mantiene los botones centrados y bien alineados.


---

## 📁 Estructura del Proyecto

```text
calculadora-dark/
│
├── main.py                 # Punto de entrada de la aplicación
├── form_calculadora.py     # Clase principal FormularioCalculadora (Interfaz y Lógica)
├── config/
│   └── constantes.py       # Definición de colores y constantes visuales
└── util/
    └── util_ventana.py     # Funciones auxiliares (ej. centrado de ventana)

```


## 📸 Vista Final & Diseño

* **Diseño Estilo Escritorio SIGMA.** 
* **Panel Superior:** Indicador de estado de sonido encendido (*ON*) y celda solar decorativa integrada en la carcasa.
 <img src="Calculadora Python/calculadora final.jpg" width="200">

 ## ✨ Características Agregadas
- 🔢 **Teclado Extendido:** Soporte para dígitos estándar, doble cero (`00`) y punto decimal.
- 💾 **Funciones de Memoria:** Incorpora botones clásicos de gestión de memoria (`MRC`, `M-`, `M+`) para operaciones financieras o acumulativas.
- 🔄 **Control de Signo y Corrección:**
  - **`C·CE`**: Limpieza total o borrado de entrada actual (destacado en color rojo).
  - **`+/-`**: Alterna el signo positivo/negativo del número actual.
  - **`➪`**: Borra el último dígito introducido.
- 🧮 **Operaciones Esenciales:** Añadidos Porcentaje (`%`) y operaciones con paréntesis `()`.
- 📐 **Estructura Robusta:** Cuadrícula proporcional simulando el relieve físico de una calculadora de oficina.
