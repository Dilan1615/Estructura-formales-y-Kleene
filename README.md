# Aplicacion de Lenguajes Formales con Flask

## Descripcion

Esta aplicacion web desarrollada con Flask permite trabajar con conceptos basicos de lenguajes formales como generacion de cadenas, operaciones entre lenguajes y evaluacion de la clausura de Kleene.

El sistema esta orientado a fines academicos para comprender mejor la teoria de automatas y lenguajes formales de forma interactiva.

---

## Funcionalidades

### Generacion de cadenas

* Genera cadenas a partir de un alfabeto dado
* Permite definir la longitud de las cadenas

### Operaciones con lenguajes

* Verificar si una cadena pertenece a un lenguaje
* Union de lenguajes
* Concatenacion de lenguajes

### Clausura de Kleene

* Kleene estrella ( *)
* Kleene mas ( + )
* Analisis del crecimiento del lenguaje

---

## Tecnologias usadas

* Python
* Flask
* HTML
* Bootstrap

---

## Instalacion

1. Clonar el repositorio:

```
git clone https://github.com/Dilan1615/Estructura-formales-y-Kleene.git
```

2. Entrar al proyecto:

```
cd Estructura-formales-y-Kleene
```

3. Crear entorno virtual:

```
python3 -m venv venv
source venv/bin/activate
```

4. Instalar dependencias:

```
pip install flask
```

5. Ejecutar la aplicacion:

```
python app.py
```

---

## Uso

* Ingresa un alfabeto o lenguaje
* Selecciona la operacion
* Observa los resultados en la consola integrada

---

## Conceptos aplicados

* Lenguajes formales
* Clausura de Kleene
* Operaciones entre lenguajes
* Generacion de cadenas

---

## Notas

* La generacion de cadenas puede crecer rapidamente si no se limita la longitud
* La clausura de Kleene puede generar conjuntos infinitos, por lo que se trabaja con iteraciones limitadas

---

Proyecto desarrollado con fines educativos
