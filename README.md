# Documentación del INVENTARIO

Este proyecto consiste en un script de Python diseñado para la captura y validación de datos de inventario. El objetivo principal es garantizar que la información ingresada por el usuario sea coherente y esté libre de errores tipográficos comunes antes de procesar cálculos financieros.

---
## ¿Cómo ejecutar el código?

Primero debes tener PYTHON y GIT en tu computador, ya que clonarás el repositorio en tu local y lo ejecutarás

1. En el repositorio esta un recuadro que dice | <> code ▼ | en verde, copias la URL para mas tarde.

2. Ve a tu explorador de archivos, ahí eligiras donde clonar el repositorio para guardarlo en tu local.

3. Una vez en elegido el lugar crea una carpeta, entra a ella, da click derecho (aunque aún no haya contenido) y das click donde dice "abrir con la terminal".

4. Ya ejecutada la terminal escribiras "git init" (sin comillas, obviamente) luego escribiras "git clone <url>, pegarás la url del repositorio que copiaste, usando click derecho y pegar, esto se verá así como ejemplo: git clone https://github.com/Luyss264/inventario.git y darás ENTER (Esto solo funcionará si previamente ya tenias git instalado).

5. Ya el repositorio esta copiado, entraras a la carpeta que se agregó y repetiras el paso de dar click derecho y abrir con la terminal.

6. Ahora escribirás "python3 inventario.py" sin comillas, esto deberá abrirte el programa y ya podrás utilizarlo.

---
## Descripción del Funcionamiento

El programa solicita tres datos fundamentales: el nombre del producto, su precio unitario y la cantidad disponible. A diferencia de un script lineal simple, este código implementa ciclos de repetición para asegurar que el programa no se detenga si el usuario comete un error.

### 1. Validación de Identidad (Nombre)
Para el nombre del producto, el sistema verifica que la entrada no consista únicamente en dígitos numéricos. Esto evita errores donde se confunde el nombre con el código o el precio. Si el usuario ingresa un número, el programa lanza un error y solicita el dato nuevamente.

### 2. Gestión de Errores en Datos Numéricos (Precio y Cantidad)
Para los valores de precio y cantidad, se utilizan estructuras de control avanzadas:
* **Manejo de Excepciones (try-except):** Si el usuario ingresa letras en campos que requieren números, el programa captura el error en lugar de colapsar.
* **Restricciones Lógicas:** Se verifica que los valores no sean negativos, ya que en un contexto de inventario, un precio o una existencia menor a cero no tiene sentido lógico.

---

## Flujo de Trabajo Técnico

El flujo de ejecución sigue una estructura de tres bloques independientes de validación:



1.  **Entrada de Nombre:** Se utiliza `isdigit()` para descartar entradas puramente numéricas.
2.  **Entrada de Precio:** Se convierte la entrada a tipo `float` (punto flotante) para permitir decimales.
3.  **Entrada de Cantidad:** Se convierte la entrada a tipo `int` (entero), ya que las unidades suelen ser indivisibles.
4.  **Cálculo de Salida:** Se aplica la fórmula matemática:
    $$CostoTotal = Precio \times Cantidad$$
5.  **Visualización:** Se presenta un resumen formateado con el resultado de la operación.

---

## Requisitos de Ejecución

Para ejecutar este programa, es necesario contar con un entorno de Python 3.x instalado. No se requieren librerías externas adicionales.

### Instrucciones:
1. Clonar o descargar el archivo `.py`.
2. Abrir una terminal o consola de comandos.
3. Ejecutar el comando:
   `python nombre_del_archivo.py`

---

