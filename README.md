# 📘 Gramáticas y Lenguajes

Este repositorio está diseñado para analizar y visualizar expresiones lógicas utilizando gramáticas. Puedes generar un Árbol de Sintaxis Abstracta (AST) a partir de una expresión lógica y visualizarlo fácilmente. Además, este repositorio está optimizado para ejecutarse en GitHub Codespaces, permitiéndote trabajar en un entorno de desarrollo completamente configurado directamente desde tu navegador.

## 🚀 Funcionalidad

- **📜 Gramáticas**: Define y reconoce expresiones lógicas como `true`, `false`, y combinaciones de estas con operadores lógicos.
- **🌳 Generación de AST**: Utiliza el script `eval.py` para generar un AST de tu expresión lógica y visualizarlo en formato de imagen.

## 🛠 Configuración en GitHub Codespaces

1. **🍴 Fork este repositorio**: Haz clic en el botón "Fork" en la parte superior derecha de esta página.
2. **🌐 Accede a GitHub Codespaces**: Ve a la sección "Codespaces" de tu GitHub.
3. **➕ Crea un nuevo Codespace**: Haz clic en "New Codespace" y selecciona el repositorio que acabas de hacer fork.
4. GitHub automáticamente configurará el entorno basado en el archivo `.devcontainer/devcontainer.json` presente en este repositorio. Esto instalará todas las dependencias necesarias.
5. Una vez que el Codespace esté listo, podrás comenzar a trabajar directamente desde tu navegador.

## 📝 Uso

1. Añade tu expresión lógica en un archivo `.txt`, por ejemplo: `miexpresion.txt`.
2. Ejecuta el script `eval.py` con tu archivo de entrada y un nombre para el archivo de salida:
   ```bash
   python eval.py miexpresion.txt salida.png
Abre salida.png para visualizar el AST de tu expresión.
## 🤝 Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia, no dudes en abrir un issue o enviar un pull request.
