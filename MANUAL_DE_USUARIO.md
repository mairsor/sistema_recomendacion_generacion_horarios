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
   - 3.4 [Configuración de Perfil](#configuración-de-perfil)

4. [Manual para el Rol: Tutor](#manual-para-el-rol-tutor)
   - 4.1 [Dashboard del Tutor](#dashboard-del-tutor)
   - 4.2 [Gestión de Estudiantes](#gestión-de-estudiantes)
   - 4.3 [Seguimiento Académico](#seguimiento-académico)
   - 4.4 [Reportes y Estadísticas](#reportes-y-estadísticas)

5. [Manual para el Rol: Administrador](#manual-para-el-rol-administrador)
   - 5.1 [Dashboard Administrativo](#dashboard-administrativo)
   - 5.2 [Gestión de Usuarios](#gestión-de-usuarios)
   - 5.3 [Gestión de Cursos](#gestión-de-cursos)
   - 5.4 [Configuración del Sistema](#configuración-del-sistema)
   - 5.5 [Reportes Generales](#reportes-generales)

6. [Preguntas Frecuentes (FAQ)](#preguntas-frecuentes-faq)

7. [Resolución de Problemas Comunes](#resolución-de-problemas-comunes)

8. [Contacto y Soporte](#contacto-y-soporte)

---

<div style="page-break-after: always;"></div>

## INTRODUCCIÓN

### 1.1 Descripción General del Sistema

El **Sistema Inteligente de Recomendación y Predicción de Demanda Académica** es una plataforma web desarrollada para la Universidad Nacional de Ingeniería (UNI) que tiene como propósito principal facilitar y optimizar el proceso de planificación académica de los estudiantes universitarios.

Este sistema integra tecnologías de inteligencia artificial y análisis de datos para ofrecer dos funcionalidades principales:

**1. Recomendación Personalizada de Cursos**

El sistema analiza el historial académico del estudiante, su rendimiento en cursos previos, sus intereses declarados y patrones de éxito de estudiantes similares para sugerir los cursos más adecuados para el siguiente ciclo académico. Esta funcionalidad considera:

- Cursos aprobados y desaprobados
- Promedio ponderado del estudiante
- Prerrequisitos y correquisitos
- Carga académica recomendada según el ciclo
- Dificultad estimada de cada curso
- Compatibilidad con el perfil académico del estudiante

**2. Predicción de Demanda Académica**

El sistema predice la cantidad estimada de estudiantes que se matricularán en cada curso para el próximo ciclo académico. Esta información permite:

- Anticipar cursos con alta demanda (posible saturación)
- Identificar cursos con baja demanda
- Planificar mejor la matrícula
- Tomar decisiones informadas sobre prioridades de matriculación
- Reducir el riesgo de no conseguir vacante en cursos críticos

**Público Objetivo**

El sistema está dirigido a tres tipos de usuarios principales:

- **Estudiantes:** Reciben recomendaciones personalizadas y pueden consultar predicciones de demanda para planificar mejor su matrícula.

- **Tutores Académicos:** Monitorean el progreso de sus tutorados, acceden a recomendaciones generadas por el sistema y brindan orientación académica más efectiva.

- **Administradores:** Gestionan usuarios, cursos, configuraciones del sistema y tienen acceso a reportes y estadísticas generales de la plataforma.

**Beneficios del Sistema**

- Reduce el tiempo de planificación académica
- Aumenta las probabilidades de éxito académico mediante recomendaciones basadas en datos
- Mejora la experiencia de matrícula al anticipar la demanda
- Facilita la toma de decisiones informadas
- Optimiza el uso de recursos académicos
- Promueve trayectorias académicas más exitosas

---

### 1.2 Objetivo del Manual

Este manual tiene como objetivos principales:

**1. Guiar al Usuario en el Uso del Sistema**

Proporcionar instrucciones claras, paso a paso, sobre cómo utilizar cada una de las funcionalidades del sistema según el rol del usuario (Alumno, Tutor o Administrador).

**2. Facilitar la Adopción de la Plataforma**

Ofrecer una referencia rápida y completa que permita a los nuevos usuarios familiarizarse con el sistema de manera autónoma y eficiente.

**3. Explicar las Funcionalidades Principales**

Describir detalladamente qué hace cada módulo del sistema, cómo interpretarlo y cómo aprovecharlo al máximo para la planificación académica.

**4. Resolver Dudas Comunes**

Incluir una sección de preguntas frecuentes y resolución de problemas que anticipe las consultas más habituales de los usuarios.

**5. Servir como Material de Consulta**

Funcionar como un documento de referencia permanente al que los usuarios puedan recurrir cuando necesiten recordar cómo realizar una acción específica.

**Alcance del Manual**

Este manual cubre:

- ✅ Procedimientos de acceso y autenticación
- ✅ Navegación por la interfaz del sistema
- ✅ Uso de todas las funcionalidades disponibles según cada rol
- ✅ Interpretación de resultados y visualizaciones
- ✅ Resolución de problemas comunes
- ✅ Contacto y soporte técnico

Este manual **NO** cubre:

- ❌ Instalación o configuración técnica del sistema (documentación para administradores de sistemas)
- ❌ Programación o modificación del código fuente
- ❌ Mantenimiento de servidores o infraestructura

**Convenciones Utilizadas en este Manual**

A lo largo del documento se utilizan los siguientes elementos para facilitar la comprensión:

> **📌 NOTA:** Información adicional o aclaraciones importantes.

> **⚠️ ADVERTENCIA:** Situaciones que requieren precaución o que pueden causar problemas.

> **💡 CONSEJO:** Recomendaciones y mejores prácticas para optimizar el uso del sistema.

> **[ESPACIO PARA CAPTURA]** Indica dónde se debe insertar una captura de pantalla ilustrativa.

---

### 1.3 Requisitos Previos

Para utilizar correctamente el **Sistema Inteligente de Recomendación y Predicción de Demanda Académica**, es necesario cumplir con los siguientes requisitos:

#### **1.3.1 Navegador Web Recomendado**

El sistema es una aplicación web moderna compatible con los navegadores más actuales. Para una experiencia óptima, se recomienda utilizar:

**Navegadores Recomendados (Versiones Actualizadas):**

- ✅ **Google Chrome** (versión 100 o superior) - *Recomendado*
- ✅ **Mozilla Firefox** (versión 100 o superior)
- ✅ **Microsoft Edge** (versión 100 o superior) - *Basado en Chromium*
- ✅ **Safari** (versión 15 o superior) - *Para usuarios de macOS*

**Navegadores NO Recomendados:**

- ❌ Internet Explorer (cualquier versión - obsoleto y sin soporte)
- ❌ Versiones antiguas de cualquier navegador

> **💡 CONSEJO:** Mantenga su navegador siempre actualizado a la última versión disponible para garantizar la seguridad y el correcto funcionamiento de todas las funcionalidades del sistema.

> **📌 NOTA:** El sistema utiliza tecnologías web modernas (JavaScript ES6+, CSS3, APIs de gráficos) que requieren navegadores actualizados. Si experimenta problemas visuales o funcionales, verifique primero la versión de su navegador.

#### **1.3.2 Conexión a Internet**

El sistema requiere una conexión activa a Internet para funcionar correctamente, ya que se comunica constantemente con servidores remotos para:

- Autenticar usuarios
- Cargar datos académicos actualizados
- Generar recomendaciones en tiempo real
- Obtener predicciones de demanda
- Guardar cambios y preferencias

**Requisitos de Conexión:**

- **Velocidad mínima recomendada:** 2 Mbps (descarga)
- **Velocidad óptima:** 5 Mbps o superior
- **Tipo de conexión:** Banda ancha, Wi-Fi, datos móviles 4G/5G
- **Estabilidad:** Conexión estable sin interrupciones frecuentes

> **⚠️ ADVERTENCIA:** Si la conexión se interrumpe mientras está utilizando el sistema, algunos datos no guardados pueden perderse. Se recomienda trabajar con conexiones estables, especialmente al configurar preferencias o generar reportes.

> **💡 CONSEJO:** Si se encuentra en un lugar con conexión inestable, espere a que el sistema termine de cargar completamente cada sección antes de continuar con otra acción.

#### **1.3.3 Credenciales de Acceso Válidas**

Para ingresar al sistema, es obligatorio contar con credenciales de autenticación válidas proporcionadas por la institución.

**¿Qué necesita para iniciar sesión?**

1. **Código de Usuario**
   - Para estudiantes: Su código de alumno institucional (ejemplo: 20201234A)
   - Para tutores: Su código de docente asignado
   - Para administradores: Su código de usuario administrativo

2. **Contraseña**
   - Contraseña personal asignada durante el registro
   - Debe ser confidencial y no compartirse con terceros

**¿Cómo obtener sus credenciales?**

- **Estudiantes nuevos:** Las credenciales son proporcionadas automáticamente al momento de la matrícula institucional. Recibirá un correo electrónico con instrucciones para activar su cuenta.

- **Tutores:** Las credenciales son asignadas por el área de Recursos Humanos o la Dirección de Escuela al momento de su designación como tutor.

- **Administradores:** Las credenciales son creadas por el administrador principal del sistema según necesidades institucionales.

> **📌 NOTA:** Si es la primera vez que accede al sistema, es posible que se le solicite cambiar su contraseña temporal por una nueva contraseña personal y segura.

> **⚠️ ADVERTENCIA:** Nunca comparta sus credenciales con otras personas. Cada usuario es responsable de las acciones realizadas con su cuenta. Si sospecha que su contraseña ha sido comprometida, cámbiela inmediatamente.

**Requisitos de Seguridad para Contraseñas:**

- Mínimo 8 caracteres
- Al menos una letra mayúscula
- Al menos una letra minúscula
- Al menos un número
- Se recomienda incluir caracteres especiales (@, #, $, etc.)

#### **1.3.4 Resolución de Pantalla Recomendada**

Para una visualización óptima de gráficos, tablas y elementos interactivos:

- **Resolución mínima:** 1280 x 720 píxeles
- **Resolución recomendada:** 1920 x 1080 píxeles o superior
- **Dispositivos compatibles:** Computadoras de escritorio, laptops, tablets (modo horizontal)

> **💡 CONSEJO:** Aunque el sistema es compatible con dispositivos móviles, se recomienda usar una computadora o laptop para acceder a todas las funcionalidades con mayor comodidad, especialmente para visualizar gráficos detallados y reportes extensos.

#### **1.3.5 Permisos del Navegador**

El sistema puede solicitar los siguientes permisos del navegador:

- **Cookies:** Necesarias para mantener la sesión activa
- **Almacenamiento local:** Para guardar preferencias del usuario
- **JavaScript habilitado:** Esencial para el funcionamiento del sistema

> **📌 NOTA:** Asegúrese de que JavaScript esté habilitado en su navegador y que no tenga extensiones o bloqueadores que impidan el correcto funcionamiento de aplicaciones web.

#### **1.3.6 Conocimientos Previos del Usuario**

No se requieren conocimientos técnicos avanzados. Sin embargo, es útil tener:

- ✅ Conocimientos básicos de navegación web
- ✅ Capacidad para leer e interpretar gráficos simples
- ✅ Comprensión de términos académicos básicos (créditos, prerrequisitos, promedio ponderado, etc.)

---

> **📌 IMPORTANTE:** Si no cumple con alguno de estos requisitos o experimenta dificultades técnicas, consulte la sección [Resolución de Problemas Comunes](#resolución-de-problemas-comunes) o contacte al equipo de soporte técnico indicado en la sección [Contacto y Soporte](#contacto-y-soporte).

---

<div style="page-break-after: always;"></div>

