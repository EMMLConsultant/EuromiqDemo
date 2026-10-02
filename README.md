# EUROMIQ · Demo pública de solo lectura

Versión demostrativa creada a partir de la interfaz y estructura de la aplicación EUROMIQ.

## Qué incluye
- Portada pública de acceso a la demo.
- Panel de inicio.
- Flujo de nueva revisión en cuatro pasos.
- Expedientes ficticios.
- Centro documental ficticio.
- Informes y métricas de muestra.
- Base normativa ilustrativa.
- Configuración de demo.

## Seguridad
Esta demo no utiliza Neon, `DATABASE_URL`, usuarios reales, expedientes reales ni secretos de producción. No permite subir documentos ni guardar cambios de forma persistente.

## Despliegue en Streamlit Community Cloud
- Repository: el repositorio GitHub de la demo.
- Branch: `main`
- Main file path: `streamlit_app.py`
- No configurar Secrets.

## Estructura esperada del repositorio
```
streamlit_app.py
requirements.txt
README.md
.gitignore
.streamlit/config.toml
brand/euromiq_logo_white.png
brand/euromiq_logo_blue.png
```
