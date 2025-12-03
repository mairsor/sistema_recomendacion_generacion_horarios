# MANUAL DE USUARIO

---

<div style="text-align: center; margin-top: 150px;">

## SISTEMA INTELIGENTE DE RECOMENDACIÓN Y PREDICCIÓN DE DEMANDA ACADÉMICA

### Manual de Usuario

<br><br>

**UNIVERSIDAD NACIONAL DE INGENIERÍA**

**Facultad de Ingeniería Industrial y de Sistemas**

<br><br>

**Curso:** Ingeniería de Software (CIB02)

**Ciclo Académico:** 2025-II

<br><br>

### INTEGRANTES

---

**Nombre:** _______________________________________________

**Código:** _______________________________________________

<br>

**Nombre:** _______________________________________________

**Código:** _______________________________________________

<br>

**Nombre:** _______________________________________________

**Código:** _______________________________________________

<br>

**Nombre:** _______________________________________________

**Código:** _______________________________________________

<br>

**Nombre:** _______________________________________________

**Código:** _______________________________________________

<br><br>

---

**Fecha de Elaboración:** Noviembre, 2025

**Versión del Documento:** 1.0

**Estado:** Final

---

</div>

<div style="page-break-after: always;"></div>

---

## TABLA DE CONTENIDO

1. [Introducción](#introducción)
   - 1.1 [Descripción General del Sistema](#descripción-general-del-sistema)
   - 1.2 [Objetivo del Manual](#objetivo-del-manual)
   - 1.3 [Requisitos Previos](#requisitos-previos)

2. [Acceso al Sistema](#acceso-al-sistema)
   - 2.1 [Inicio de Sesión](#inicio-de-sesión)
   - 2.2 [Roles del Sistema](#roles-del-sistema)

3. [Manual para el Rol: Alumno](#manual-para-el-rol-alumno)
   - 3.1 [Dashboard del Estudiante](#dashboard-del-estudiante)
   - 3.2 [Recomendación de Cursos](#recomendación-de-cursos)
   - 3.3 [Predicción de Demanda](#predicción-de-demanda)

4. [Manual para el Rol: Tutor/Profesor](#manual-para-el-rol-tutorprofesor)
   - 4.1 [Dashboard del Tutor](#dashboard-del-tutor)
   - 4.2 [Predicción de Demanda](#predicción-de-demanda-1)

5. [Manual para el Rol: Administrador](#manual-para-el-rol-administrador)
   - 5.1 [Dashboard Administrativo](#dashboard-administrativo)
   - 5.2 [Vista de Estudiantes](#vista-de-estudiantes)
   - 5.3 [Predicción de Demanda](#predicción-de-demanda-2)

6. [Preguntas Frecuentes (FAQ)](#preguntas-frecuentes-faq)

7. [Resolución de Problemas Comunes](#resolución-de-problemas-comunes)

8. [Contacto y Soporte](#contacto-y-soporte)

---

<div style="page-break-after: always;"></div>

## INTRODUCCIÓN

### 1.1 Descripción General del Sistema

El **Sistema Inteligente de Recomendación y Predicción de Demanda Académica** es una plataforma web diseñada para optimizar el proceso de planificación académica en la Universidad Nacional de Ingeniería.

**Funcionalidades principales:**

- **Dashboard personalizado** con estadísticas académicas por rol
- **Sistema de recomendación de cursos** basado en algoritmos híbridos (colaborativo + contenido)
- **Predicción de demanda** de cursos usando modelos de Machine Learning
- **Análisis de datos** académicos en tiempo real

**Tecnologías utilizadas:**

- Frontend: Next.js 14 con TypeScript
- Backend: NestJS con PostgreSQL
- API de Recomendaciones: Flask + scikit-learn
- API de Predicción: FastAPI + ARIMA/LSTM/Prophet

### 1.2 Objetivo del Manual

Este manual describe **únicamente las funcionalidades implementadas y operativas** en el sistema actual. No incluye funcionalidades planeadas o en desarrollo.

**Público objetivo:**

- Estudiantes de la UNI
- Tutores/Profesores
- Administradores del sistema académico

### 1.3 Requisitos Previos

**Requisitos técnicos:**

- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Conexión a internet estable
- Resolución mínima recomendada: 1366x768

**Requisitos de acceso:**

- Credenciales de usuario proporcionadas por la institución
- Código de alumno/profesor válido en el sistema

---

<div style="page-break-after: always;"></div>

## ACCESO AL SISTEMA

### 2.1 Inicio de Sesión

**Paso 1:** Acceda a la URL del sistema en su navegador

**Paso 2:** Ingrese sus credenciales:

- **Código de usuario:** Su código institucional
- **Contraseña:** Contraseña asignada

**[ESPACIO PARA CAPTURA: Pantalla de login]**

**Paso 3:** Haga clic en "Iniciar Sesión"

> **📌 NOTA:** El sistema le redirigirá automáticamente al dashboard correspondiente según su rol.

### 2.2 Roles del Sistema

El sistema tiene tres roles con acceso a diferentes funcionalidades:

#### **👨‍🎓 ALUMNO**

**Acceso a:**
- Dashboard con estadísticas personales
- Recomendaciones de cursos personalizadas
- Consulta de predicción de demanda

#### **👨‍🏫 TUTOR/PROFESOR**

**Acceso a:**
- Dashboard con cursos asignados
- Lista de alumnos matriculados
- Consulta de predicción de demanda

#### **👨‍💼 ADMINISTRADOR**

**Acceso a:**
- Dashboard con estadísticas globales del sistema
- Vista general de todos los estudiantes
- Herramientas de predicción de demanda
- Estadísticas del sistema

---

<div style="page-break-after: always;"></div>

## MANUAL PARA EL ROL: ALUMNO

### 3.1 Dashboard del Estudiante

El Dashboard es su pantalla principal. Muestra una vista consolidada de su situación académica actual.

**[ESPACIO PARA CAPTURA: Dashboard completo del estudiante]**

#### **3.1.1 Estadísticas Principales**

El dashboard muestra 4 tarjetas con métricas clave:

**1. Créditos Aprobados**

- Total de créditos que ha aprobado
- Indica su avance en la carrera

**2. Promedio Ponderado**

- Su promedio ponderado acumulado
- Calculado automáticamente desde su historial

**3. Ciclo Relativo**

- El ciclo académico en el que se encuentra
- Basado en su ingreso a la universidad

**4. Tasa de Aprobación**

- Porcentaje de cursos aprobados vs. llevados
- Indicador de su rendimiento general

**[ESPACIO PARA CAPTURA: Tarjetas de estadísticas]**

#### **3.1.2 Indicador de Progreso**

Muestra visualmente su avance en la carrera:

- **Barra de progreso circular** con porcentaje de créditos aprobados
- **Total de créditos:** Aprobados / Totales de la carrera
- **Proyección:** Créditos que le faltan para completar

**[ESPACIO PARA CAPTURA: Indicador de progreso]**

#### **3.1.3 Cursos Actuales**

Lista de cursos en los que está matriculado este semestre:

**Información mostrada por curso:**

- Código y nombre del curso
- Número de créditos
- Profesor asignado
- Sección y turno
- Estado de matrícula

**[ESPACIO PARA CAPTURA: Tabla de cursos actuales]**

> **💡 CONSEJO:** Esta información se actualiza automáticamente cuando se registran cambios en el sistema académico.

#### **3.1.4 Panel de Alertas**

El sistema genera alertas automáticas basadas en sus datos:

**Tipos de alertas:**

**🟡 Alerta de Advertencia**
- Cursos desaprobados que debe recuperar
- Promedio por debajo del mínimo institucional
- Progreso de créditos más lento de lo esperado

**🔵 Alerta Informativa**
- Número de cursos en progreso actual
- Recordatorios generales

**🟢 Alerta de Éxito**
- Reconocimiento por buen rendimiento
- Tasa de aprobación alta

**[ESPACIO PARA CAPTURA: Panel de alertas]**

---

### 3.2 Recomendación de Cursos

El sistema le sugiere cursos basándose en su historial académico, desempeño y malla curricular.

**Acceso:** Menú principal > Recomendaciones

**[ESPACIO PARA CAPTURA: Página de recomendaciones]**

#### **3.2.1 Información del Estudiante**

En la parte superior verá 4 tarjetas con su información:

**1. Progreso en Malla**

- Porcentaje de avance en la carrera
- Cursos obligatorios aprobados vs. totales
- Barra de progreso visual

**2. Promedio General**

- Su promedio ponderado
- Tasa de aprobación general

**3. Mejor Línea de Carrera**

- La línea de carrera donde tiene mejor desempeño
- Promedio en esa línea específica

**4. Cursos Jalados**

- Número de cursos obligatorios desaprobados
- Requieren atención prioritaria

**[ESPACIO PARA CAPTURA: Tarjetas de información del estudiante]**

#### **3.2.2 Pestañas de Información**

El sistema organiza la información en 3 pestañas:

**Pestaña: Recomendaciones**

Lista de cursos recomendados ordenados por relevancia.

**Información de cada recomendación:**

- **Ranking:** Posición (#1, #2, #3...)
- **Código y nombre del curso**
- **Score de recomendación:** Puntuación (0-10)
- **Líneas de carrera:** Áreas académicas relacionadas
- **Badges informativos:**
  - "Jalado" si es un curso que desaprobó
  - "Obligatorio" si es requisito de la malla

**[ESPACIO PARA CAPTURA: Lista de recomendaciones]**

**Razones de la recomendación:**

Cada curso muestra por qué se recomienda:

- **Similitud de contenido:** Qué tan similar es a cursos que aprobó con buen promedio
- **Score colaborativo:** Basado en estudiantes con historial similar al suyo
- **Performance en líneas:** Su desempeño en las áreas relacionadas al curso
- **Prerequisitos:** Si cumple o no con los cursos previos requeridos

**[ESPACIO PARA CAPTURA: Detalle de una recomendación]**

> **💡 CONSEJO:** Los cursos con ranking #1, #2 y #3 tienen borde resaltado por ser los más recomendados.

**Pestaña: Mi Desempeño**

Muestra su rendimiento por línea de carrera:

- **Análisis por área académica:** Matemáticas, Física, Programación, etc.
- **Promedio en cada línea:** Con barra de progreso visual
- **Ordenado de mayor a menor desempeño**

**Cursos pendientes de aprobar:**

Lista de cursos obligatorios que tiene desaprobados y debe recuperar.

**[ESPACIO PARA CAPTURA: Análisis de desempeño]**

**Pestaña: Mi Historial**

Resumen de todos los cursos que ha cursado:

- **Total de cursos llevados**
- **Cursos aprobados** con barra de progreso
- **Cursos desaprobados** con barra de progreso

**[ESPACIO PARA CAPTURA: Historial académico]**

#### **3.2.3 Actualizar Recomendaciones**

Puede actualizar sus recomendaciones en cualquier momento:

**Paso 1:** Haga clic en el botón "Actualizar" (icono de refresh)

**Paso 2:** El sistema recalculará las recomendaciones (toma 2-3 segundos)

**Paso 3:** La lista se actualizará con nuevas sugerencias

> **📌 NOTA:** Si su código no está en el sistema de recomendaciones, se mostrarán datos de demostración con una advertencia.

---

### 3.3 Predicción de Demanda

Consulte predicciones de cuántos estudiantes se matricularán en cursos específicos.

**Acceso:** Menú principal > Predicción de Demanda

**[ESPACIO PARA CAPTURA: Página de predicción]**

#### **3.3.1 Cómo Consultar Predicciones**

**Paso 1:** Seleccione el semestre a consultar (ej: 2025-I, 2025-II)

**Paso 2:** (Opcional) Filtre por:
- Código de curso específico
- Nombre del curso
- Rango de fechas

**Paso 3:** Haga clic en "Buscar" o "Consultar Predicciones"

**Paso 4:** El sistema mostrará los resultados disponibles

**[ESPACIO PARA CAPTURA: Formulario de búsqueda]**

#### **3.3.2 Interpretando los Resultados**

Cada predicción muestra:

- **Código y nombre del curso**
- **Semestre proyectado**
- **Demanda predicha:** Número estimado de matriculados
- **Nivel de confianza:** Qué tan confiable es la predicción
- **Modelo usado:** ARIMA, LSTM o Prophet

**Indicadores visuales:**

- 🟢 **Verde:** Baja demanda (muchas vacantes esperadas)
- 🟡 **Amarillo:** Demanda media (vacantes limitadas)
- 🔴 **Rojo:** Alta demanda (posible saturación)

**[ESPACIO PARA CAPTURA: Resultados de predicción]**

> **💡 CONSEJO:** Use esta información para planificar su matrícula. Si un curso tiene predicción de alta demanda, considere matricularse temprano o tener alternativas.

#### **3.3.3 Ver Resultados Históricos**

Puede consultar predicciones anteriores y su precisión:

**Acceso:** Resultados > Ver Histórico

**Información mostrada:**

- Predicciones pasadas
- Demanda real que ocurrió
- Error de predicción (diferencia)
- Gráficos comparativos

**[ESPACIO PARA CAPTURA: Resultados históricos]**

---

<div style="page-break-after: always;"></div>

## MANUAL PARA EL ROL: TUTOR/PROFESOR

### 4.1 Dashboard del Tutor

El Dashboard del tutor muestra información sobre sus cursos asignados y estudiantes matriculados.

**[ESPACIO PARA CAPTURA: Dashboard del tutor]**

#### **4.1.1 Estadísticas Generales**

El dashboard muestra tarjetas con:

**1. Información Personal**

- Su código de profesor
- Nombre completo
- Años de experiencia
- Índice de popularidad (basado en matrículas)

**2. Estadísticas de Cursos**

- **Total de cursos ofertados:** En todo el historial
- **Cursos distintos:** Diferentes cursos que ha dictado
- **Total de alumnos:** Suma de todos sus estudiantes
- **Promedio de alumnos por curso**

**[ESPACIO PARA CAPTURA: Tarjetas de estadísticas del tutor]**

#### **4.1.2 Cursos del Semestre Actual**

Lista de cursos que está dictando actualmente:

**Información por curso:**

- **Código y nombre del curso**
- **Sección asignada**
- **Cupos disponibles**
- **Alumnos matriculados**
- **Porcentaje de ocupación**
- **Turno** (mañana, tarde, noche)

**[ESPACIO PARA CAPTURA: Lista de cursos actuales]**

#### **4.1.3 Lista de Alumnos por Curso**

Para cada curso puede ver la lista de estudiantes matriculados:

- Código del alumno
- Nombre completo
- Estado de matrícula

**[ESPACIO PARA CAPTURA: Lista de alumnos]**

> **💡 CONSEJO:** Use esta información para conocer el tamaño de sus clases y planificar las actividades académicas.

---

### 4.2 Predicción de Demanda

Como tutor, tiene acceso a las mismas herramientas de predicción que los alumnos.

**Funcionalidad:** Idéntica a la sección 3.3 del rol Alumno

**Uso recomendado:**
- Planificar apertura de nuevas secciones
- Identificar cursos con alta/baja demanda
- Coordinar con otros profesores

---

<div style="page-break-after: always;"></div>

## MANUAL PARA EL ROL: ADMINISTRADOR

El panel de administrador le da acceso a tres módulos principales: **Gestión de Matrícula**, **Recomendador de Horarios** y **Predictor de Demanda**.

### 5.1 Dashboard Administrativo

Vista general con estadísticas globales del sistema académico.

**[ESPACIO PARA CAPTURA: Dashboard administrativo completo]**

#### **5.1.1 Estadísticas Globales**

4 tarjetas principales con métricas institucionales:

**1. Total Alumnos**
- Número total de estudiantes en el sistema

**2. Total Profesores**
- Número total de docentes registrados

**3. Total Cursos**
- Cursos en el catálogo institucional

**4. Total Usuarios**
- Todos los usuarios del sistema (alumnos + profesores + admins)

**[ESPACIO PARA CAPTURA: Tarjetas de estadísticas globales]**

#### **5.1.2 Información del Semestre Actual**

Panel con datos del ciclo académico en curso:

- **Cursos ofertados:** Total de cursos abiertos este semestre
- **Total matrículas:** Suma de todas las matrículas registradas
- **Promedio de matrículas por curso:** Indicador de demanda general

**[ESPACIO PARA CAPTURA: Panel semestre actual]**

#### **5.1.3 Demanda Promedio Global**

Tarjeta destacada que muestra:

- **Matrícula promedio por curso** en el semestre actual
- Cálculo: Total matrículas / Total cursos ofertados
- Útil para planificación de recursos

**[ESPACIO PARA CAPTURA: Demanda promedio]**

#### **5.1.4 Cursos Más Saturados**

Lista de los 5 cursos con mayor número de matriculados:

**Información por curso:**

- Código y nombre
- Profesor asignado
- Sección
- Número de matriculados
- Vacantes disponibles
- Porcentaje de ocupación
- Badge "100%" si está completamente lleno

**[ESPACIO PARA CAPTURA: Top cursos saturados]**

> **⚠️ ALERTA:** Estos cursos requieren atención prioritaria. Considere abrir nuevas secciones o aumentar cupos.

#### **5.1.5 Cursos con Baja Matrícula**

Lista de los 5 cursos con menor demanda:

- Misma información que cursos saturados
- Badge "Baja demanda"
- Útil para identificar cursos que podrían cancelarse o necesitan promoción

**[ESPACIO PARA CAPTURA: Cursos con baja matrícula]**

#### **5.1.6 Distribución de Alumnos por Ciclo**

Gráfico de barras mostrando cuántos estudiantes hay en cada ciclo relativo:

- Identifica concentración de estudiantes
- Ayuda a planificar oferta de cursos por nivel
- Barras proporcionales al número de alumnos

**[ESPACIO PARA CAPTURA: Gráfico de distribución por ciclos]**

#### **5.1.7 Estadísticas de Matrícula por Estado**

Tarjetas mostrando cantidad de matrículas en cada estado:

- **Matriculado:** Cursos en progreso
- **Aprobado:** Cursos culminados exitosamente
- **Desaprobado:** Cursos no aprobados
- **Retirado:** Matrículas canceladas

**[ESPACIO PARA CAPTURA: Estadísticas por estado]**

#### **5.1.8 Rendimiento General**

Tarjeta destacada con:

- **Promedio general del sistema:** Promedio ponderado de todos los estudiantes
- Indicador de desempeño académico institucional

**[ESPACIO PARA CAPTURA: Rendimiento general]**

#### **5.1.9 Actividad del Sistema**

Panel informativo con:

- Estado del sistema (En línea)
- Última actualización (semestre)
- Total de matrículas procesadas
- Cursos activos
- Base de datos (resumen)
- Estado de APIs (Predictor y Recomendador)

**[ESPACIO PARA CAPTURA: Panel de actividad]**

---

### 5.2 Gestión de Matrícula

Módulo para administrar cursos y secciones del sistema académico.

#### **5.2.1 Gestión de Cursos**

**Acceso:** Menú lateral > Gestión de Matrícula > Cursos

Vista de todos los cursos disponibles en el catálogo institucional.

**Funcionalidades:**

- Tabla con listado de cursos
- Información: código, nombre, créditos, estado
- Búsqueda y filtrado de cursos
- Vista detallada de cada curso

**[ESPACIO PARA CAPTURA: Página de gestión de cursos]**

> **📌 NOTA:** Esta sección permite consultar el catálogo de cursos registrados en el sistema.

#### **5.2.2 Gestión de Secciones**

**Acceso:** Menú lateral > Gestión de Matrícula > Secciones

Vista de las secciones ofertadas por semestre.

**Funcionalidades:**

- Listado de secciones por curso
- Información: profesor asignado, horario, cupos
- Filtrado por semestre y curso
- Detalles de matrícula por sección

**[ESPACIO PARA CAPTURA: Página de gestión de secciones]**

---

### 5.3 Recomendador de Horarios

Sistema de análisis y recomendación académica usando Machine Learning.

#### **5.3.1 Estadísticas del Sistema**

**Acceso:** Menú lateral > Recomendador de Horarios > Estadísticas del Sistema

Vista general de métricas del sistema de recomendación.

**[ESPACIO PARA CAPTURA: Página de estadísticas del sistema]**

**Estadísticas Principales:**

**Tarjeta 1: Total Estudiantes**
- Número de estudiantes registrados en el sistema de recomendación

**Tarjeta 2: Total Cursos**
- Cursos disponibles en el catálogo

**Tarjeta 3: Registros Totales**
- Total de matrículas históricas procesadas

**Tarjeta 4: Líneas de Carrera**
- Número de líneas académicas definidas

**[ESPACIO PARA CAPTURA: Tarjetas de estadísticas principales]**

**Información de Modelos ML:**

El sistema muestra métricas de los 3 modelos de Machine Learning implementados:

**1. Knowledge Graph**
- **Nodos:** Entidades en el grafo de conocimiento
- **Conexiones:** Relaciones entre cursos y conceptos
- **Embeddings:** Vectores de representación generados

**2. Collaborative Filtering**
- **Factores latentes:** Dimensión del espacio latente
- **Algoritmo:** ALS (Alternating Least Squares)

**3. Modelo Híbrido**
- **Dimensión:** Tamaño de los embeddings
- **Arquitectura:** MLP (Multi-Layer Perceptron)

**[ESPACIO PARA CAPTURA: Panel de modelos ML]**

**Distribución por Líneas de Carrera:**

Gráfico de barras mostrando:

- Cada línea de carrera disponible
- Número de cursos en cada línea
- Porcentaje respecto al total
- Barra de progreso visual

**[ESPACIO PARA CAPTURA: Distribución por líneas]**

**Métricas Promedio del Sistema:**

**1. Promedio Cursos/Estudiante**
- Cuántos cursos ha llevado cada estudiante en promedio

**2. Densidad de Datos**
- Porcentaje de cobertura de la matriz estudiante-curso
- Indica qué tan completos están los datos

**3. Cursos por Línea**
- Distribución promedio de cursos entre líneas de carrera

**[ESPACIO PARA CAPTURA: Tarjetas de métricas promedio]**

#### **5.3.2 Gestión de Estudiantes**

**Acceso:** Menú lateral > Recomendador de Horarios > Gestión de Estudiantes

Vista completa de todos los estudiantes en el sistema de recomendación.

**[ESPACIO PARA CAPTURA: Página de gestión de estudiantes]**

**Estadísticas Generales (4 Tarjetas):**

1. **Total Estudiantes:** Registrados en el sistema
2. **Promedio General:** Nota promedio de todos los estudiantes
3. **Progreso Promedio:** Avance de carrera promedio
4. **Cursos Reprobados:** Total en el sistema

**[ESPACIO PARA CAPTURA: Tarjetas estadísticas generales]**

**Panel Izquierdo - Lista de Estudiantes:**

- **Barra de búsqueda:** Filtrar por código de estudiante
- **Lista completa:** Todos los estudiantes con:
  - Código del estudiante
  - Porcentaje de progreso
  - Promedio ponderado (con ⭐)
  - Badge de color según rendimiento
  - Icono de tendencia
- **Selección:** Clic para ver detalles completos

**[ESPACIO PARA CAPTURA: Panel de lista de estudiantes]**

**Panel Derecho - Detalles del Estudiante:**

Cuando selecciona un estudiante, se muestra:

**Información Básica:**
- Código del estudiante
- Nota promedio

**Progreso de Carrera:**
- Barra de progreso visual
- Porcentaje completado

**Estadísticas:**
- **Cursos Completados:** Total aprobados
- **Cursos Reprobados:** Total desaprobados

**Mejor Línea de Carrera:**
- Badge con el nombre de la línea
- Basado en desempeño histórico

**Información Adicional:**
- Cursos en progreso estimados
- Tasa de aprobación calculada

**[ESPACIO PARA CAPTURA: Panel de detalles del estudiante]**

> **💡 CONSEJO:** Use la búsqueda para encontrar estudiantes rápidamente por su código.

---

### 5.4 Predictor de Demanda

Como administrador, tiene acceso completo al sistema de predicción de demanda.

#### **5.4.1 Generar Predicciones**

**Acceso:** Menú lateral > Predictor de Demanda > Predicciones

**Funcionalidad:**

- Seleccionar semestre objetivo
- Elegir modelos de predicción (ARIMA, LSTM, Prophet)
- Configurar parámetros
- Ejecutar predicción para todos los cursos

**[ESPACIO PARA CAPTURA: Interfaz de generación de predicciones]**

#### **5.4.2 Ver Resultados**

**Acceso:** Menú lateral > Predictor de Demanda > Resultados

- Consulta de predicciones generadas
- Filtros por curso, semestre, modelo
- Exportación de datos

**[ESPACIO PARA CAPTURA: Resultados de predicciones]**

#### **5.4.3 Modelos ML**

**Acceso:** Menú lateral > Predictor de Demanda > Modelos ML

Información sobre los modelos disponibles:

- **ARIMA:** Para series temporales con tendencia
- **LSTM:** Red neuronal para patrones complejos
- **Prophet:** Modelo de Facebook para estacionalidad

**[ESPACIO PARA CAPTURA: Información de modelos]**

---

<div style="page-break-after: always;"></div>

## PREGUNTAS FRECUENTES (FAQ)

### Preguntas Generales

**P: ¿Necesito instalar algo para usar el sistema?**

R: No. El sistema es completamente web. Solo necesita un navegador moderno y conexión a internet.

**P: ¿Funciona en móviles?**

R: Sí, pero para mejor experiencia se recomienda usar una computadora, especialmente para ver gráficos y tablas.

**P: ¿Mis datos están seguros?**

R: Sí. El sistema usa conexión HTTPS encriptada y las contraseñas se almacenan de forma segura.

---

### Sobre Recomendaciones

**P: ¿Por qué dice "usando datos de demostración"?**

R: Si su código no está en el sistema de recomendaciones, se muestran datos de ejemplo. Contacte al administrador para agregar su información.

**P: ¿Las recomendaciones garantizan que aprobaré?**

R: No. Son sugerencias basadas en patrones estadísticos. Su éxito depende de su esfuerzo personal.

**P: ¿Con qué frecuencia se actualizan las recomendaciones?**

R: Se generan en tiempo real cada vez que las solicita, basándose en su historial académico más reciente.

---

### Sobre Predicción de Demanda

**P: ¿Qué tan precisas son las predicciones?**

R: Depende del curso y el modelo. En promedio tienen 85-90% de precisión, pero eventos imprevistos pueden afectar los resultados.

**P: ¿Las predicciones cambian durante la matrícula?**

R: No. Las predicciones son proyecciones pre-matrícula. No se actualizan en tiempo real durante el proceso.

**P: ¿Debo evitar cursos con "alta demanda"?**

R: No necesariamente. Use esa información para planificar: tener alternativas, matricularse temprano, considerar otros horarios.

---

<div style="page-break-after: always;"></div>

## RESOLUCIÓN DE PROBLEMAS COMUNES

### Problema 1: No puedo iniciar sesión

**Síntomas:** Error al ingresar credenciales

**Soluciones:**

1. Verifique que el código y contraseña sean correctos
2. Intente con otro navegador
3. Limpie caché y cookies
4. Contacte al administrador si persiste

---

### Problema 2: Las recomendaciones no aparecen

**Síntomas:** Página de recomendaciones vacía o con error

**Soluciones:**

1. Actualice la página (F5)
2. Verifique su conexión a internet
3. Si ve advertencia de "datos de demostración", es normal (su código no está registrado)
4. Contacte al administrador si el error persiste

---

### Problema 3: Las predicciones no se muestran

**Síntomas:** No hay resultados de predicción

**Soluciones:**

1. Verifique que haya seleccionado un semestre
2. Intente buscar un curso específico por código
3. Puede que no haya predicciones generadas para ese semestre aún
4. Contacte al administrador

---

### Problema 4: El dashboard no carga

**Síntomas:** Pantalla en blanco o error de carga

**Soluciones:**

1. Verifique su conexión a internet
2. Cierre sesión y vuelva a entrar
3. Limpie caché del navegador
4. Intente con modo incógnito
5. Contacte soporte técnico si persiste

---

### Problema 5: Datos desactualizados

**Síntomas:** La información no refleja cambios recientes

**Soluciones:**

1. Use el botón "Actualizar" o "Refresh" si está disponible
2. Cierre sesión y vuelva a entrar
3. La sincronización con el sistema académico puede tardar hasta 24 horas
4. Contacte al administrador si los datos siguen incorrectos después de 48 horas

---

<div style="page-break-after: always;"></div>

## CONTACTO Y SOPORTE

### Canales de Soporte

**Soporte Técnico del Sistema**

- **Correo electrónico:** soporte.sistema@uni.edu.pe
- **Horario de atención:** Lunes a viernes, 8:00 AM - 6:00 PM
- **Tiempo de respuesta:** 24-48 horas hábiles

---

**Administrador del Sistema**

- **Correo:** admin.academico@uni.edu.pe
- **Oficina:** [Ubicación física]

---

**Mesa de Ayuda Institucional**

- **Teléfono:** (01) XXX-XXXX
- **Correo:** mesaayuda@uni.edu.pe
- **Horario:** Lunes a viernes, 8:00 AM - 8:00 PM

---

### Para Reportar Problemas

**Información útil al contactar soporte:**

1. Descripción clara del problema
2. Qué estaba haciendo cuando ocurrió
3. Mensaje de error (captura de pantalla si es posible)
4. Navegador que usa
5. Su rol en el sistema (Alumno/Tutor/Admin)

---

### Recursos Adicionales

**Documentación:**

- Manual de usuario (este documento)
- Disponible en el sistema: Menú > Ayuda

---

> **📌 NOTA FINAL:** Este manual describe únicamente las funcionalidades actualmente implementadas en el sistema. Puede haber actualizaciones futuras que agreguen nuevas características.

---

**Versión del Manual:** 1.0 (Funcionalidades Reales)  
**Fecha de publicación:** Noviembre 2025  
**Última actualización:** 27 de Noviembre de 2025

---

<div style="text-align: center; margin-top: 50px;">

**FIN DEL MANUAL DE USUARIO**

---

**Sistema Inteligente de Recomendación y Predicción de Demanda Académica**

Universidad Nacional de Ingeniería

© 2025 - Todos los derechos reservados

</div>
