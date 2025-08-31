#!/bin/bash
# Script para construir y ejecutar el backend con Docker


SCRIPT_DIR="$(dirname "$0")"
PROJECT_ROOT="$SCRIPT_DIR/../../.."

# Detectar si estamos en la raíz o en edustream
if [ -d "$PROJECT_ROOT/edustream/SRC/backend" ]; then
    cd "$PROJECT_ROOT"
    CONTEXT="edustream"
    DOCKERFILE="edustream/SRC/backend/dockerfile.back"
else
    CONTEXT="."
    DOCKERFILE="SRC/backend/dockerfile.back"
fi

echo "Construyendo imagen Docker..."
docker build -t edustream-backend -f "$DOCKERFILE" "$CONTEXT"
if [ $? -eq 0 ]; then
    echo -e "\n✅ Imagen Docker construida correctamente."
    echo "Ejecutando contenedor Docker en puerto 8000..."
    echo "Accede a la API en: http://localhost:8000/docs"
    if command -v xdg-open &> /dev/null; then
        xdg-open http://localhost:8000/docs
    elif command -v open &> /dev/null; then
        open http://localhost:8000/docs
    fi
    docker run -p 8000:8000 edustream-backend
    if [ $? -eq 0 ]; then
        echo -e "\n✅ Contenedor ejecutado correctamente."
    else
        echo -e "\n❌ Error al ejecutar el contenedor Docker."
    fi
else
    echo -e "\n❌ Error al construir la imagen Docker. Revisa los logs."
fi