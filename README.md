# Prueba Técnica - Consultor Analítico (CALA Analytics)

Este repositorio contiene la resolución de la prueba técnica para el rol de Desarrollador Backend / Consultor Analítico.

### BLOQUE 1
## 1. Pasos para ejecutar el proyecto
Para ejecutar la aplicación de Django localmente, sigue estos pasos:

1. **Clonar el repositorio** e ingresar a la carpeta del proyecto.
2. **Crear y activar un entorno virtual**:
   `python -m venv venv`
   `.\venv\Scripts\activate  # Windows`
3. **Instalar Django**: `pip install django`
4. **Ejecutar el servidor**: `python manage.py runserver`
5. **Abrir el navegador en**: `http://127.0.0.1:8000/`

## 2. Decisiones técnicas tomadas
**Arquitectura**: Se utilizó la estructura estándar MVT de Django para separar la lógica de negocio (views) de la presentación (templates).
**Datos Simulados**: Siguiendo los requerimientos, los datos se definieron directamente en el backend (View) como una lista de diccionarios para simular una respuesta de API o base de datos sin necesidad de persistencia.
**Diseño**: Se utilizó CSS embebido en el template para asegurar que la tabla sea legible y profesional sin dependencias externas.

## 3. Principales aprendizajes
- Integración de lógica de backend en Python con estructuras de visualización en HTML.
- Aplicación de funciones analíticas de SQL (como DATE_TRUNC) específicamente para BigQuery.
- Estructuración de un proyecto desde cero priorizando la claridad y las buenas prácticas de documentación.

### BLOQUE 2
## 1. Respuestas - Parte B (Conceptual)
Para consumir datos de BigQuery en Django, el proceso ideal sería:

1. **Conexión**: Usar la librería google-cloud-bigquery con credenciales de Service Account de GCP.
2. **Extracción**: Crear una capa de servicio en Django para ejecutar los queries SQL y transformar los resultados en tipos de datos nativos de Python.
3. **Presentación**: Exponer los datos mediante Django REST Framework para que un frontend moderno los consuma dinámicamente.

### BLOQUE 3
## 1. Respuestas - Bloque 3 (Criterio Profesional)

**1. ¿Cómo abordarías un requerimiento técnicamente incorrecto solicitado por un cliente?**
> "Lo abordaría con transparencia y un enfoque consultivo. Primero, intentaría entender el objetivo final que el cliente busca lograr. Luego, explicaría de forma clara y sin tecnicismos los riesgos o ineficiencias de su propuesta original. Finalmente, presentaría una alternativa viable que cumpla su objetivo de negocio siguiendo las mejores prácticas técnicas, asegurando que el cliente se sienta acompañado y no simplemente rechazado."

**2. ¿Qué harías si debes trabajar con una tecnología que no dominas y el proyecto ya inició?**
> "Implementaría un plan de aprendizaje acelerado: lectura intensiva de documentación, consulta de casos de uso similares y realización de pruebas de concepto rápidas. Sería honesto con mi líder sobre mi curva de aprendizaje para ajustar expectativas de tiempo, mientras busco mentoría con compañeros que dominen la tecnología. Mi prioridad sería entregar funcionalidades estables, aunque inicialmente tome un poco más de tiempo la investigación."

**3. ¿Cómo aseguras calidad técnica cuando trabajas bajo presión de tiempo?**
> "Me enfoco en tres pilares: primero, priorizar el 'core' de la funcionalidad para asegurar que el valor principal se entregue sin errores. Segundo, no negociar las pruebas unitarias básicas para la lógica crítica. Tercero, mantener el código limpio y comentado (siguiendo PEP8), ya que el ahorro de tiempo al escribir código 'sucio' se pierde rápidamente en el mantenimiento y la corrección de errores futuros."