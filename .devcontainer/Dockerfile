# Usar la imagen universal como base
FROM mcr.microsoft.com/devcontainers/universal:2

# Instalar Graphviz y paquetes Python
RUN apt-get update && apt-get install -y graphviz && \
    pip install plyplus pydot
