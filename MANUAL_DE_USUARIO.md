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

## ACCESO AL SISTEMA

### 2.1 Inicio de Sesión

El acceso al sistema se realiza a través de una página de autenticación segura donde deberá ingresar sus credenciales institucionales.

#### **2.1.1 Accediendo a la Página de Inicio de Sesión**

Para acceder al sistema, abra su navegador web e ingrese la URL proporcionada por la institución:

```
https://sistema-horarios.uni.edu.pe
```

> **📌 NOTA:** La URL exacta será proporcionada por su institución. Guárdela en sus marcadores para acceso rápido.

**[ESPACIO PARA CAPTURA: Página de inicio de sesión]**

#### **2.1.2 Campos del Formulario de Inicio de Sesión**

La pantalla de inicio de sesión contiene los siguientes campos:

**1. Código de Usuario**

- **Descripción:** Campo donde debe ingresar su código institucional único.
- **Formato esperado:**
  - Estudiantes: Código de alumno (ejemplo: `20201234A`, `20191567B`)
  - Tutores: Código de docente (ejemplo: `DOC12345`)
  - Administradores: Código administrativo (ejemplo: `ADMIN001`)
- **Características:**
  - No distingue entre mayúsculas y minúsculas
  - No se permiten espacios en blanco
  - Debe ingresarse completo, incluyendo letras finales si las tiene

> **💡 CONSEJO:** Copie y pegue su código de usuario desde un documento seguro si tiene dificultades para recordarlo. Asegúrese de no incluir espacios adicionales al copiar.

**2. Contraseña**

- **Descripción:** Campo donde debe ingresar su contraseña personal.
- **Características:**
  - Los caracteres se muestran ocultos (****) por seguridad
  - Distingue entre mayúsculas y minúsculas
  - Mínimo 8 caracteres
  - No se permiten espacios en blanco

> **⚠️ ADVERTENCIA:** La contraseña es sensible a mayúsculas. Verifique que la tecla Bloq Mayús (Caps Lock) no esté activada si experimenta problemas al iniciar sesión.

**3. Mostrar Contraseña (opcional)**

- Ícono de ojo junto al campo de contraseña
- Permite visualizar temporalmente la contraseña mientras escribe
- Útil para verificar que ha escrito correctamente su contraseña

**4. Recordar Sesión (checkbox opcional)**

- Casilla de verificación "Mantener sesión iniciada"
- Si se marca, el sistema recordará su sesión por 7 días
- Solo active esta opción en dispositivos personales y seguros
- NO active esta opción en computadoras públicas o compartidas

> **⚠️ ADVERTENCIA:** Por seguridad, no active la opción "Recordar sesión" en computadoras de uso público (laboratorios, cabinas de internet, bibliotecas).

**5. Botón "Iniciar Sesión"**

- Haga clic en este botón para enviar sus credenciales
- También puede presionar la tecla `Enter` después de escribir su contraseña
- El sistema validará sus credenciales y le dirigirá al dashboard correspondiente a su rol

**6. Enlace "¿Olvidó su contraseña?"**

- Ubicado debajo del botón de inicio de sesión
- Permite recuperar o restablecer su contraseña
- Requiere su código de usuario y correo electrónico institucional registrado

**[ESPACIO PARA CAPTURA: Formulario de inicio de sesión con campos señalados]**

#### **2.1.3 Proceso de Inicio de Sesión Exitoso**

Cuando ingresa credenciales válidas:

1. El sistema muestra un indicador de carga "Verificando credenciales..."
2. Se validan sus datos contra la base de datos institucional
3. Se determina su rol (Alumno, Tutor o Administrador)
4. Es redirigido automáticamente al dashboard correspondiente
5. Aparece un mensaje de bienvenida con su nombre

**[ESPACIO PARA CAPTURA: Pantalla de carga durante autenticación]**

> **💡 CONSEJO:** Si es su primer acceso al sistema, es posible que se le solicite actualizar su contraseña temporal por una permanente. Siga las instrucciones en pantalla para completar este proceso.

#### **2.1.4 Mensajes de Error Comunes**

El sistema puede mostrar diferentes mensajes de error si hay problemas con el inicio de sesión. A continuación se explican los más comunes:

**Error 1: "Código de usuario o contraseña incorrectos"**

- **Causa:** Las credenciales ingresadas no coinciden con ningún usuario registrado
- **Solución:**
  1. Verifique que su código de usuario esté escrito correctamente
  2. Verifique que no haya espacios antes o después del código
  3. Compruebe que la tecla Bloq Mayús no esté activada
  4. Intente escribir su contraseña nuevamente con cuidado
  5. Si el problema persiste, use la opción "¿Olvidó su contraseña?"

**[ESPACIO PARA CAPTURA: Mensaje de error de credenciales incorrectas]**

**Error 2: "Usuario bloqueado temporalmente"**

- **Causa:** Ha excedido el número máximo de intentos fallidos (generalmente 5 intentos)
- **Duración del bloqueo:** 15-30 minutos
- **Solución:**
  1. Espere el tiempo indicado antes de intentar nuevamente
  2. Si necesita acceso urgente, contacte al soporte técnico
  3. Cuando se desbloquee, use la opción de recuperar contraseña si no la recuerda

**[ESPACIO PARA CAPTURA: Mensaje de cuenta bloqueada]**

**Error 3: "Su cuenta no está activa"**

- **Causa:** Su cuenta existe pero no ha sido activada por un administrador
- **Casos comunes:**
  - Estudiante de nuevo ingreso pendiente de activación
  - Tutor recientemente designado
  - Cuenta desactivada por motivos administrativos
- **Solución:**
  1. Contacte a la oficina administrativa correspondiente
  2. Para estudiantes: Dirección de Escuela o Registro Académico
  3. Para tutores: Recursos Humanos o Dirección de Escuela

**Error 4: "Error de conexión al servidor"**

- **Causa:** Problema de conectividad con el servidor del sistema
- **Solución:**
  1. Verifique su conexión a Internet
  2. Actualice la página (F5 o Ctrl+R)
  3. Intente cerrar y abrir nuevamente el navegador
  4. Si persiste, puede ser un problema temporal del servidor. Intente más tarde
  5. Contacte a soporte técnico si el problema continúa después de 30 minutos

**[ESPACIO PARA CAPTURA: Mensaje de error de conexión]**

**Error 5: "Sesión expirada"**

- **Causa:** Ha estado inactivo durante mucho tiempo (generalmente 2 horas)
- **Solución:**
  1. Simplemente vuelva a iniciar sesión con sus credenciales
  2. Sus datos guardados se habrán conservado automáticamente

**Error 6: "Navegador no compatible"**

- **Causa:** Está utilizando un navegador antiguo o no compatible
- **Solución:**
  1. Actualice su navegador a la última versión disponible
  2. Use uno de los navegadores recomendados (Chrome, Firefox, Edge, Safari)
  3. Consulte la sección [Requisitos Previos](#requisitos-previos) para más información

> **📌 NOTA:** Si encuentra un mensaje de error no descrito aquí, tome nota del mensaje exacto y contacte al soporte técnico. Esta información ayudará a resolver el problema más rápidamente.

#### **2.1.5 Recuperación de Contraseña**

Si olvidó su contraseña, puede restablecerla siguiendo estos pasos:

**Paso 1:** En la página de inicio de sesión, haga clic en "¿Olvidó su contraseña?"

**Paso 2:** Ingrese su código de usuario en el campo solicitado

**Paso 3:** El sistema le enviará un correo electrónico a su dirección institucional registrada

**Paso 4:** Revise su correo (incluyendo carpeta de spam) y busque el mensaje del sistema

**Paso 5:** Haga clic en el enlace de recuperación dentro del correo (válido por 24 horas)

**Paso 6:** Cree una nueva contraseña que cumpla con los requisitos de seguridad

**Paso 7:** Confirme la nueva contraseña y guárdela en un lugar seguro

**Paso 8:** Inicie sesión con su nueva contraseña

**[ESPACIO PARA CAPTURA: Formulario de recuperación de contraseña]**

> **⚠️ ADVERTENCIA:** El enlace de recuperación expira después de 24 horas. Si no lo utiliza a tiempo, deberá solicitar uno nuevo.

> **💡 CONSEJO:** Si no recibe el correo de recuperación en 5 minutos, verifique su carpeta de spam o correo no deseado. Si aún no lo encuentra, verifique que su correo institucional esté actualizado en el sistema.

---

### 2.2 Roles del Sistema

El sistema cuenta con tres roles principales, cada uno con permisos y funcionalidades específicas según sus responsabilidades institucionales.

#### **2.2.1 Rol: Alumno (Estudiante)**

**Descripción General**

El rol de Alumno está diseñado para estudiantes activos de la universidad. Es el rol con mayor número de usuarios y enfocado principalmente en la planificación académica personal.

**Acceso y Asignación**

- Asignado automáticamente al matricularse en la universidad
- Un estudiante solo puede tener una cuenta activa
- Permanece activo mientras mantenga la condición de estudiante regular

**Funcionalidades Principales**

Los estudiantes con este rol pueden:

✅ **Visualizar Dashboard Personalizado**
   - Ver resumen académico actual (créditos, promedio, ciclo)
   - Consultar alertas y notificaciones importantes
   - Acceder a estadísticas de su progreso académico

✅ **Recibir Recomendaciones de Cursos**
   - Obtener sugerencias personalizadas de cursos para el siguiente ciclo
   - Ver cursos ordenados por prioridad y compatibilidad
   - Consultar justificación de cada recomendación
   - Filtrar recomendaciones según preferencias

✅ **Consultar Predicciones de Demanda**
   - Ver estimación de demanda para cursos de interés
   - Identificar cursos con riesgo de saturación
   - Planificar prioridades de matrícula
   - Comparar demanda histórica vs. predicha

✅ **Gestionar Perfil Personal**
   - Actualizar información de contacto
   - Declarar intereses académicos
   - Configurar preferencias del sistema
   - Cambiar contraseña

✅ **Consultar Historial Académico**
   - Ver cursos aprobados y desaprobados
   - Revisar notas por ciclo
   - Analizar progreso en la malla curricular

**Limitaciones**

Los estudiantes NO pueden:

❌ Modificar datos académicos oficiales (notas, créditos)
❌ Acceder a información de otros estudiantes
❌ Crear o eliminar cursos del sistema
❌ Gestionar usuarios

> **📌 NOTA:** Las recomendaciones y predicciones son orientativas. La decisión final de matrícula es responsabilidad del estudiante, quien debe considerar también otros factores como horarios, docentes y carga académica personal.

**[ESPACIO PARA CAPTURA: Dashboard del rol Alumno]**

---

#### **2.2.2 Rol: Tutor (Docente/Asesor Académico)**

**Descripción General**

El rol de Tutor está diseñado para docentes o asesores académicos que tienen la responsabilidad de orientar y dar seguimiento a un grupo de estudiantes (tutorados).

**Acceso y Asignación**

- Asignado por administradores del sistema
- Requiere nombramiento oficial como tutor académico
- Un tutor puede tener múltiples tutorados asignados
- Puede ser docente activo o personal académico designado

**Funcionalidades Principales**

Los tutores con este rol pueden:

✅ **Visualizar Dashboard de Tutoría**
   - Ver resumen de todos sus tutorados
   - Consultar estadísticas generales del grupo
   - Identificar estudiantes con alertas académicas
   - Acceder a reportes consolidados

✅ **Gestionar Tutorados**
   - Ver lista completa de estudiantes asignados
   - Consultar perfil académico de cada tutorado
   - Revisar historial académico detallado
   - Ver recomendaciones generadas para cada estudiante

✅ **Realizar Seguimiento Académico**
   - Monitorear progreso individual de tutorados
   - Identificar estudiantes en riesgo académico
   - Ver cursos matriculados y planificados
   - Consultar predicciones de demanda para orientar mejor

✅ **Acceder a Reportes**
   - Generar reportes por tutorado
   - Exportar información en PDF o Excel
   - Visualizar tendencias y estadísticas del grupo
   - Comparar desempeño entre ciclos

✅ **Gestionar Perfil de Tutor**
   - Actualizar información de contacto
   - Configurar preferencias de notificaciones
   - Cambiar contraseña

**Limitaciones**

Los tutores NO pueden:

❌ Modificar notas o datos académicos oficiales
❌ Matricular o desmatricular estudiantes
❌ Modificar recomendaciones del sistema (solo consultarlas)
❌ Acceder a información de estudiantes no asignados como tutorados
❌ Crear o eliminar cursos
❌ Gestionar otros usuarios del sistema

> **💡 CONSEJO:** Como tutor, use las recomendaciones del sistema como punto de partida para sus sesiones de asesoría. Complemente la información automatizada con su experiencia y conocimiento del estudiante.

> **📌 NOTA:** La información académica de sus tutorados es confidencial. Úsela exclusivamente para fines de tutoría y orientación académica.

**[ESPACIO PARA CAPTURA: Dashboard del rol Tutor]**

---

#### **2.2.3 Rol: Administrador**

**Descripción General**

El rol de Administrador está diseñado para personal administrativo con responsabilidad sobre la gestión operativa del sistema. Tiene los privilegios más elevados y acceso completo a todas las funcionalidades.

**Acceso y Asignación**

- Asignado únicamente por el administrador principal del sistema
- Requiere autorización institucional de alto nivel
- Limitado a personal de confianza (Dirección de Escuela, TI, Registro Académico)
- Rol con mayor responsabilidad y acceso a datos sensibles

**Funcionalidades Principales**

Los administradores con este rol pueden:

✅ **Visualizar Dashboard Administrativo**
   - Ver estadísticas globales del sistema
   - Consultar métricas de uso y actividad
   - Identificar problemas técnicos o de datos
   - Acceder a reportes institucionales

✅ **Gestionar Usuarios**
   - Crear, editar y eliminar cuentas de usuarios
   - Asignar y cambiar roles (Alumno, Tutor, Administrador)
   - Activar o desactivar cuentas
   - Resetear contraseñas de usuarios
   - Asignar tutores a estudiantes
   - Ver logs de actividad de usuarios

✅ **Gestionar Cursos**
   - Crear nuevos cursos en el sistema
   - Editar información de cursos existentes
   - Configurar prerrequisitos y correquisitos
   - Asignar créditos y dificultad estimada
   - Activar o desactivar cursos
   - Importar/exportar catálogo de cursos

✅ **Configurar Sistema**
   - Ajustar parámetros del algoritmo de recomendación
   - Configurar umbrales de predicción
   - Gestionar períodos académicos (ciclos)
   - Configurar notificaciones automáticas
   - Establecer políticas de seguridad
   - Realizar mantenimiento del sistema

✅ **Acceder a Reportes Globales**
   - Generar reportes institucionales completos
   - Exportar datos masivos para análisis
   - Visualizar tendencias históricas
   - Consultar estadísticas de demanda por facultad/escuela
   - Analizar efectividad de recomendaciones

✅ **Gestión Avanzada**
   - Realizar respaldos (backups) de datos
   - Restaurar información
   - Ver logs del sistema
   - Monitorear rendimiento técnico

**Limitaciones**

Aunque es el rol con más privilegios, los administradores NO pueden:

❌ Modificar el código fuente del sistema (requiere acceso de desarrollador)
❌ Acceder directamente a la base de datos sin registro de auditoría
❌ Delegar permisos de administrador sin autorización superior

> **⚠️ ADVERTENCIA:** El rol de administrador tiene acceso a información sensible de toda la comunidad universitaria. Debe ejercerse con responsabilidad, ética y conforme a las políticas de privacidad institucionales.

> **⚠️ ADVERTENCIA:** Toda acción administrativa queda registrada en logs de auditoría con fecha, hora y usuario responsable.

> **💡 CONSEJO:** Realice respaldos periódicos del sistema, especialmente antes de realizar cambios masivos en la configuración o antes de períodos críticos como matrícula.

**[ESPACIO PARA CAPTURA: Dashboard del rol Administrador]**

---

#### **2.2.4 Tabla Comparativa de Roles**

| Funcionalidad | Alumno | Tutor | Administrador |
|--------------|--------|-------|---------------|
| Ver dashboard personalizado | ✅ | ✅ | ✅ |
| Recibir recomendaciones de cursos | ✅ | ❌ | ❌ |
| Ver predicciones de demanda | ✅ | ✅ | ✅ |
| Ver información de tutorados | ❌ | ✅ | ✅ |
| Gestionar usuarios | ❌ | ❌ | ✅ |
| Gestionar cursos | ❌ | ❌ | ✅ |
| Configurar sistema | ❌ | ❌ | ✅ |
| Exportar reportes | ❌ | ✅ | ✅ |
| Modificar datos académicos | ❌ | ❌ | ✅* |

*Con registro de auditoría

> **📌 NOTA:** Si necesita funcionalidades adicionales que no están disponibles en su rol actual, contacte al administrador del sistema o a la autoridad académica correspondiente.

---

<div style="page-break-after: always;"></div>

## MANUAL PARA EL ROL: ALUMNO

Esta sección está dedicada exclusivamente a los usuarios con rol de **Alumno (Estudiante)**. Aquí encontrará instrucciones detalladas sobre cómo utilizar todas las funcionalidades disponibles para usted.

---

### 3.1 Dashboard del Estudiante

El Dashboard es la pantalla principal que verá inmediatamente después de iniciar sesión. Está diseñado para proporcionarle una visión rápida y completa de su situación académica actual.

**[ESPACIO PARA CAPTURA: Vista completa del Dashboard del estudiante]**

#### **3.1.1 Estructura General del Dashboard**

El Dashboard del estudiante está organizado en varias secciones principales:

**1. Barra de Navegación Superior**

Ubicada en la parte superior de la pantalla, contiene:

- **Logo del Sistema:** En la esquina superior izquierda
- **Menú de Navegación:** Enlaces a las secciones principales
  - Dashboard (inicio)
  - Recomendaciones
  - Predicción de Demanda
  - Mi Perfil
- **Notificaciones:** Ícono de campana con contador de notificaciones pendientes
- **Perfil de Usuario:** Su nombre y foto (si está configurada)
- **Cerrar Sesión:** Botón para salir del sistema de forma segura

**[ESPACIO PARA CAPTURA: Barra de navegación superior con elementos señalados]**

> **💡 CONSEJO:** La barra de navegación permanece visible en todas las pantallas del sistema, permitiéndole moverse fácilmente entre secciones sin perderse.

**2. Panel de Bienvenida**

Muestra un saludo personalizado con su nombre y la fecha actual:

```
¡Bienvenido, [Tu Nombre]!
Miércoles, 27 de Noviembre de 2025
```

**[ESPACIO PARA CAPTURA: Panel de bienvenida personalizado]**

**3. Sección de Resumen Académico**

Esta sección central muestra sus indicadores académicos más importantes en tarjetas informativas:

#### **Tarjeta 1: Créditos Acumulados**

- **Qué muestra:** Total de créditos aprobados hasta el momento
- **Formato:** Número de créditos / Total de créditos de la carrera
- **Ejemplo:** `156 / 200 créditos`
- **Indicador visual:** Barra de progreso que muestra el porcentaje completado
- **Color:** Verde (en buen camino) o amarillo (retraso)

**[ESPACIO PARA CAPTURA: Tarjeta de créditos acumulados]**

> **📌 NOTA:** Los créditos mostrados son únicamente los cursos aprobados. Los cursos desaprobados o en curso no se contabilizan aquí.

#### **Tarjeta 2: Promedio Ponderado**

- **Qué muestra:** Su promedio ponderado acumulado (PPA)
- **Formato:** Número decimal de 0 a 20
- **Ejemplo:** `14.5`
- **Indicador visual:** Medidor circular con código de colores
  - Verde: PPA ≥ 14.0 (excelente)
  - Amarillo: PPA entre 11.0 y 13.9 (regular)
  - Rojo: PPA < 11.0 (en riesgo)

**[ESPACIO PARA CAPTURA: Tarjeta de promedio ponderado]**

> **💡 CONSEJO:** Su promedio ponderado es uno de los factores más importantes que el sistema considera para generar recomendaciones personalizadas.

#### **Tarjeta 3: Ciclo Actual**

- **Qué muestra:** El ciclo académico en el que se encuentra
- **Formato:** Ordinal del ciclo (ejemplo: `8vo ciclo`, `5to ciclo`)
- **Información adicional:** 
  - Fecha de inicio del ciclo
  - Fecha de finalización del ciclo
  - Semanas transcurridas / semanas totales

**[ESPACIO PARA CAPTURA: Tarjeta de ciclo actual]**

#### **Tarjeta 4: Cursos en Progreso**

- **Qué muestra:** Cantidad de cursos en los que está matriculado actualmente
- **Formato:** Número de cursos
- **Ejemplo:** `6 cursos`
- **Información adicional:** Total de créditos de los cursos actuales
- **Enlace:** "Ver detalles" para expandir la lista completa de cursos

**[ESPACIO PARA CAPTURA: Tarjeta de cursos en progreso]**

**4. Sección de Alertas y Notificaciones**

Ubicada en el lado derecho del dashboard, muestra avisos importantes:

#### **Tipos de Alertas**

**🔴 Alertas Críticas (Rojas)**
- Cursos en riesgo de desaprobación
- Créditos insuficientes para graduación
- Matrícula pendiente
- Problemas administrativos urgentes

**🟡 Alertas de Advertencia (Amarillas)**
- Cursos con asistencia baja
- Proximidad de fechas importantes
- Actualizaciones de datos pendientes

**🔵 Alertas Informativas (Azules)**
- Nuevas recomendaciones disponibles
- Actualizaciones del sistema
- Mensajes generales

**[ESPACIO PARA CAPTURA: Panel de alertas con diferentes tipos]**

> **⚠️ ADVERTENCIA:** Preste especial atención a las alertas críticas (rojas). Ignorarlas puede afectar su situación académica.

**5. Sección de Acciones Rápidas**

Botones de acceso directo a las funcionalidades más utilizadas:

- **📊 Ver Recomendaciones:** Acceso directo al módulo de recomendación de cursos
- **📈 Consultar Demanda:** Acceso directo a predicciones de demanda
- **📚 Mi Historial:** Ver todos los cursos cursados
- **⚙️ Configuración:** Ajustar preferencias personales

**[ESPACIO PARA CAPTURA: Sección de acciones rápidas]**

**6. Sección de Progreso Académico (Gráfico)**

Visualización gráfica de su avance en la carrera:

- **Gráfico de barras:** Créditos aprobados por ciclo
- **Línea de tendencia:** Evolución de su promedio ponderado
- **Malla curricular:** Representación visual de cursos aprobados vs. pendientes

**[ESPACIO PARA CAPTURA: Gráficos de progreso académico]**

> **💡 CONSEJO:** Use estos gráficos para identificar patrones. Por ejemplo, si su promedio bajó en ciertos ciclos, piense qué factores influyeron y cómo evitarlos en el futuro.

#### **3.1.2 Interpretando los Indicadores**

**Cómo leer la Barra de Progreso de Créditos:**

- **Verde llena:** Está avanzando según lo esperado o por encima
- **Verde parcial:** Avance normal
- **Amarilla:** Posible retraso en la carrera
- **Números adicionales:** 
  - Porcentaje completado
  - Créditos restantes para graduación
  - Promedio de créditos por ciclo

**Cómo interpretar el Promedio Ponderado:**

- **16.0 - 20.0:** Excelente desempeño académico
- **14.0 - 15.9:** Muy buen desempeño
- **11.0 - 13.9:** Desempeño regular, con espacio para mejorar
- **0.0 - 10.9:** Desempeño bajo, requiere atención urgente

> **📌 NOTA:** El promedio ponderado es calculado automáticamente según la fórmula institucional oficial, considerando las notas y créditos de cada curso.

#### **3.1.3 Acciones Disponibles desde el Dashboard**

Desde el dashboard puede realizar las siguientes acciones:

**1. Actualizar Información**

- Haga clic en el botón de actualizar (ícono de recarga) en la esquina superior derecha
- El sistema sincronizará sus datos académicos más recientes
- Útil si recientemente se publicaron notas o hubo cambios en su matrícula

**2. Ver Detalles Expandidos**

- Cada tarjeta tiene un enlace "Ver más" o "Detalles"
- Al hacer clic, se expande para mostrar información adicional
- Por ejemplo, en "Cursos en Progreso" puede ver la lista completa con notas parciales

**3. Configurar Dashboard**

- Algunos elementos del dashboard son personalizables
- Haga clic en el ícono de engranaje en la esquina superior
- Puede elegir qué secciones mostrar u ocultar según sus preferencias

**4. Exportar Resumen**

- Botón "Exportar" permite descargar su resumen académico
- Formatos disponibles: PDF, Excel
- Útil para presentar en trámites administrativos o tutorías

**[ESPACIO PARA CAPTURA: Opciones de exportación del dashboard]**

#### **3.1.4 Preguntas Frecuentes sobre el Dashboard**

**P: ¿Con qué frecuencia se actualiza la información del dashboard?**

R: Los datos académicos se sincronizan automáticamente cada 24 horas. Sin embargo, puede forzar una actualización manual haciendo clic en el botón de recarga. Las notas se actualizan cuando los docentes las publican oficialmente.

**P: ¿Por qué mi promedio mostrado aquí difiere del oficial?**

R: El sistema calcula el promedio según la información disponible en ese momento. Si hay notas pendientes de registro o correcciones administrativas en proceso, puede haber pequeñas diferencias temporales. Siempre consulte con Registro Académico para confirmación oficial.

**P: ¿Puedo personalizar qué información ver en el dashboard?**

R: Sí, parcialmente. Puede ocultar o mostrar ciertas secciones desde Configuración > Preferencias de Dashboard. Sin embargo, algunos elementos (como créditos y promedio) son obligatorios por políticas institucionales.

**P: ¿Las alertas se envían también por correo?**

R: Sí, las alertas críticas y de advertencia también se envían a su correo institucional. Revise regularmente tanto el dashboard como su correo para no perder información importante.

---

### 3.2 Recomendación de Cursos

El módulo de **Recomendación de Cursos** es una de las funcionalidades principales del sistema. Utiliza inteligencia artificial para analizar su historial académico, rendimiento, intereses y patrones de estudiantes similares, generando sugerencias personalizadas de cursos para su próximo ciclo.

**[ESPACIO PARA CAPTURA: Pantalla principal del módulo de recomendaciones]**

#### **3.2.1 Accediendo al Módulo de Recomendaciones**

Existen tres formas de acceder:

1. **Desde el menú principal:** Clic en "Recomendaciones" en la barra de navegación superior
2. **Desde el dashboard:** Botón "Ver Recomendaciones" en acciones rápidas
3. **Desde notificaciones:** Cuando hay nuevas recomendaciones disponibles

> **📌 NOTA:** Las recomendaciones se generan automáticamente antes de cada período de matrícula. También puede solicitar recomendaciones actualizadas en cualquier momento.

#### **3.2.2 Generando Recomendaciones Personalizadas**

**Paso 1: Configurar Preferencias (Opcional)**

Antes de generar recomendaciones, puede ajustar sus preferencias:

- **Número de cursos deseados:** Indique cuántos cursos planea matricular (rango: 4-8)
- **Carga académica:** Ligera, Moderada o Intensa
- **Áreas de interés:** Marque las áreas académicas de su preferencia
- **Restricciones de horario:** Mañana, tarde, noche o sin preferencia
- **Prioridad:** Nivelar promedio, avanzar rápido, o equilibrado

**[ESPACIO PARA CAPTURA: Formulario de configuración de preferencias]**

> **💡 CONSEJO:** Sea realista con la carga académica. Si trabaja o tiene otras responsabilidades, seleccione "Ligera" o "Moderada". El sistema ajustará las recomendaciones considerando el nivel de dificultad de los cursos.

**Paso 2: Solicitar Recomendaciones**

- Haga clic en el botón **"Generar Recomendaciones"**
- El sistema mostrará un indicador de progreso: "Analizando tu historial académico..."
- El proceso toma entre 5 y 15 segundos
- Una vez completado, aparecerá la lista de cursos recomendados

**[ESPACIO PARA CAPTURA: Indicador de carga durante generación]**

#### **3.2.3 Interpretando las Recomendaciones**

Cada curso recomendado se presenta en una tarjeta con la siguiente información:

**Información Principal del Curso:**

- **Código y Nombre del Curso:** Ejemplo: `CS101 - Algoritmos y Estructuras de Datos`
- **Créditos:** Cantidad de créditos que otorga (ejemplo: 4.0)
- **Nivel de Prioridad:** Indicador visual (Alta, Media, Baja)
- **Porcentaje de Compatibilidad:** Qué tan adecuado es el curso para usted (0-100%)

**[ESPACIO PARA CAPTURA: Tarjeta individual de curso recomendado]**

**Indicadores Visuales:**

- **🟢 Prioridad Alta (Verde):** Curso altamente recomendado para usted
- **🟡 Prioridad Media (Amarillo):** Curso recomendado, pero con consideraciones
- **🔵 Prioridad Baja (Azul):** Curso opcional, puede ser pospuesto

**Justificación de la Recomendación:**

Al hacer clic en "Ver detalles" o en el ícono de información (ℹ️), se despliega una explicación de por qué el sistema recomienda ese curso:

- **Prerrequisitos cumplidos:** ✅ o ❌
- **Relación con cursos aprobados:** Muestra cursos previos relevantes
- **Tasa de éxito predicha:** Porcentaje estimado de que apruebe el curso
- **Dificultad estimada:** Fácil, Moderado, Difícil, Muy Difícil
- **Promedio de otros estudiantes con perfil similar:** Dato estadístico

**Ejemplo de justificación:**

```
Este curso es altamente recomendado porque:
✅ Has cumplido todos los prerrequisitos
✅ Tu rendimiento en cursos relacionados es excelente (promedio: 16.2)
✅ Estudiantes con perfil similar tienen tasa de éxito del 87%
⚠️ Dificultad: Moderada
📊 Compatibilidad con tus intereses declarados: 92%
```

**[ESPACIO PARA CAPTURA: Panel de justificación expandido]**

> **💡 CONSEJO:** Lea siempre la justificación antes de decidir. A veces un curso con "Prioridad Media" puede ser más conveniente para usted que uno de "Prioridad Alta" según circunstancias personales no capturadas por el sistema.

**Información Adicional Disponible:**

- **Horarios disponibles:** Lista de secciones con horarios
- **Docentes:** Profesores asignados (si está disponible)
- **Sillabus:** Enlace al sillabus oficial del curso
- **Comentarios de estudiantes:** Opiniones y consejos de quienes cursaron previamente (opcional)

#### **3.2.4 Filtrando y Ordenando Recomendaciones**

En la parte superior de la lista de recomendaciones encontrará opciones de filtro y ordenamiento:

**Opciones de Filtro:**

- **Por facultad/escuela:** Si aplica
- **Por nivel de dificultad:** Fácil, Moderado, Difícil
- **Por área de conocimiento:** Matemáticas, Programación, Humanidades, etc.
- **Por créditos:** Rango de 2 a 6 créditos
- **Por prioridad:** Alta, Media, Baja
- **Por prerrequisitos:** Solo cursos con todos los prerrequisitos cumplidos

**[ESPACIO PARA CAPTURA: Panel de filtros activo]**

**Opciones de Ordenamiento:**

- **Compatibilidad (recomendado):** Orden por defecto, del más al menos compatible
- **Prioridad:** De alta a baja
- **Dificultad:** De fácil a difícil o viceversa
- **Créditos:** De menor a mayor o viceversa
- **Alfabético:** Por nombre del curso

> **💡 CONSEJO:** Si busca equilibrar su carga académica, ordene por dificultad y seleccione una combinación de cursos fáciles y moderados, evitando matricular solo cursos difíciles en un mismo ciclo.

#### **3.2.5 Acciones con las Recomendaciones**

**1. Marcar Cursos de Interés**

- Haga clic en el ícono de estrella (⭐) o corazón (❤️) en cualquier curso
- Los cursos marcados se guardan en su lista de "Cursos Favoritos"
- Útil para recordar qué cursos planea matricular

**2. Agregar a Lista de Matrícula**

- Botón "Agregar a mi plan" en cada tarjeta
- Los cursos se agregan a un carrito virtual de planificación
- Puede ver el resumen de su plan: total de créditos, carga estimada, horarios sugeridos
- **IMPORTANTE:** Esto NO es matrícula real, solo planificación

**[ESPACIO PARA CAPTURA: Vista del carrito de planificación]**

**3. Comparar Cursos**

- Seleccione hasta 4 cursos marcando sus casillas
- Haga clic en "Comparar seleccionados"
- Aparece una tabla comparativa lado a lado con todas las características

**[ESPACIO PARA CAPTURA: Vista de comparación entre cursos]**

**4. Solicitar Asesoría**

- Botón "Consultar con mi tutor" envía sus recomendaciones a su tutor asignado
- Incluye sus dudas o comentarios específicos
- El tutor recibirá notificación y puede responder directamente en el sistema

**5. Exportar Recomendaciones**

- Botón "Exportar" permite descargar la lista completa
- Formatos: PDF (para imprimir) o Excel (para análisis)
- Incluye todas las justificaciones y detalles
- Útil para discutir con tutor, familia o para archivo personal

#### **3.2.6 Entendiendo las Advertencias**

Algunos cursos pueden mostrar advertencias específicas:

**⚠️ Prerrequisitos no cumplidos**
- El curso requiere haber aprobado otros cursos primero
- Muestra qué prerrequisitos faltan
- **NO puede matricular** este curso hasta cumplir los requisitos

**⚠️ Correquisitos requeridos**
- Debe matricular otro curso simultáneamente
- Muestra qué curso debe acompañar
- Ambos cursos deben estar en su plan de matrícula

**⚠️ Incompatibilidad de horarios**
- El horario de este curso se cruza con otro curso en su plan
- Debe elegir entre uno u otro
- El sistema resalta los horarios en conflicto

**⚠️ Carga académica excesiva**
- Agregar este curso supera la carga recomendada para su perfil
- El sistema advierte pero permite agregarlo (bajo su responsabilidad)
- Considere su capacidad real antes de sobrecargarse

**⚠️ Alta demanda predicha**
- El curso tiene predicción de saturación (ver sección Predicción de Demanda)
- Considere tener alternativas preparadas
- Priorice este curso en su orden de matrícula

**[ESPACIO PARA CAPTURA: Ejemplos de advertencias en tarjetas de cursos]**

> **⚠️ ADVERTENCIA:** Las recomendaciones son sugerencias basadas en análisis de datos, NO son obligatorias ni garantizan aprobación del curso. Usted es responsable de sus decisiones de matrícula.

#### **3.2.7 Actualizando Recomendaciones**

Las recomendaciones pueden actualizarse en las siguientes situaciones:

- **Cambios en su historial académico:** Si se publican notas nuevas
- **Cambios en el catálogo de cursos:** Si se agregan o eliminan cursos
- **Modificación de preferencias:** Si ajusta sus filtros o preferencias
- **Solicitud manual:** Botón "Regenerar recomendaciones"

> **📌 NOTA:** Las recomendaciones se actualizan automáticamente una vez por semana durante el período pre-matrícula. Fuera de ese período, puede solicitarlas manualmente cuando necesite.

#### **3.2.8 Consejos para Aprovechar las Recomendaciones**

**✅ HAGA:**

- Revise las recomendaciones al menos 2 semanas antes de la matrícula
- Lea las justificaciones de cada curso
- Consulte con su tutor académico sobre las recomendaciones
- Prepare un plan principal y 2-3 planes alternativos
- Considere factores personales (trabajo, salud, familia) que el sistema no conoce
- Marque sus cursos favoritos para referencia rápida

**❌ NO HAGA:**

- No confíe ciegamente en las recomendaciones sin análisis personal
- No ignore las advertencias del sistema
- No sobrecargue su matrícula más allá de su capacidad real
- No deje la planificación para el último momento
- No matricule cursos sin verificar prerrequisitos
- No ignore los horarios al planificar (el sistema no siempre puede validar todos los cruces)

> **💡 CONSEJO FINAL:** Use las recomendaciones como punto de partida, no como decisión final. Complemente con su conocimiento personal, objetivos de carrera, situación actual y asesoría de su tutor.

---

### 3.3 Predicción de Demanda

El módulo de **Predicción de Demanda** utiliza algoritmos de machine learning para estimar cuántos estudiantes se matricularán en cada curso durante el próximo ciclo académico. Esta información le ayuda a anticipar cursos saturados y planificar mejor su matrícula.

**[ESPACIO PARA CAPTURA: Pantalla principal del módulo de predicción de demanda]**

#### **3.3.1 Accediendo al Módulo de Predicción**

Puede acceder desde:

1. **Menú principal:** Clic en "Predicción de Demanda" en la barra de navegación
2. **Dashboard:** Botón "Consultar Demanda" en acciones rápidas
3. **Desde recomendaciones:** Enlace directo en cada curso recomendado

#### **3.3.2 Entendiendo las Predicciones**

La predicción de demanda se presenta de varias formas:

**Vista de Lista de Cursos**

Todos los cursos disponibles se muestran con:

- **Código y nombre del curso**
- **Demanda predicha:** Número estimado de alumnos
- **Vacantes disponibles:** Cupos ofrecidos por la universidad
- **Nivel de saturación:** Indicador visual

**Indicadores de Saturación:**

- **🟢 Verde - Disponibilidad alta:** Demanda < 70% de vacantes
  - Ejemplo: 45 alumnos predichos / 80 vacantes
  - Muy baja probabilidad de no conseguir vacante

- **🟡 Amarillo - Disponibilidad media:** Demanda entre 70-95% de vacantes
  - Ejemplo: 68 alumnos predichos / 80 vacantes
  - Probabilidad moderada de saturación, requiere atención

- **🟠 Naranja - Disponibilidad baja:** Demanda entre 95-105% de vacantes
  - Ejemplo: 78 alumnos predichos / 80 vacantes
  - Alta probabilidad de saturación, priorizar en matrícula

- **🔴 Rojo - Saturación esperada:** Demanda > 105% de vacantes
  - Ejemplo: 95 alumnos predichos / 80 vacantes
  - Saturación casi segura, tener plan alternativo obligatorio

**[ESPACIO PARA CAPTURA: Lista de cursos con indicadores de saturación]**

> **⚠️ ADVERTENCIA:** Las predicciones son estimaciones estadísticas basadas en datos históricos y tendencias. NO son garantía absoluta, pero tienen alta precisión (generalmente >85%).

**Vista de Gráfico de Demanda**

Visualización gráfica que muestra:

- **Gráfico de barras:** Demanda predicha vs. vacantes disponibles
- **Línea de tendencia:** Cómo ha variado la demanda en ciclos anteriores
- **Porcentaje de saturación:** Indicador numérico preciso

**[ESPACIO PARA CAPTURA: Gráficos de predicción de demanda]**

#### **3.3.3 Analizando un Curso Específico**

Al hacer clic en cualquier curso, se despliega información detallada:

**Sección 1: Resumen de Predicción**

- **Demanda actual predicha:** 87 estudiantes
- **Vacantes disponibles:** 80 plazas
- **Tasa de saturación:** 109% (Saturación esperada 🔴)
- **Nivel de confianza:** 88% (qué tan precisa es la predicción)

**Sección 2: Historial de Demanda**

Tabla comparativa de ciclos anteriores:

| Ciclo | Demanda Real | Vacantes | Saturación |
|-------|--------------|----------|------------|
| 2025-I | 82 | 80 | 103% 🟠 |
| 2024-II | 79 | 80 | 99% 🟡 |
| 2024-I | 85 | 80 | 106% 🔴 |
| 2023-II | 74 | 75 | 99% 🟡 |

**[ESPACIO PARA CAPTURA: Tabla de historial de demanda]**

> **💡 CONSEJO:** Si un curso ha estado saturado en los últimos 3-4 ciclos consecutivos, es muy probable que vuelva a saturarse. Considere este curso como alta prioridad en su orden de matrícula.

**Sección 3: Factores de Demanda**

Explicación de qué está influyendo en la predicción:

- **Tendencia histórica:** ↗️ Demanda creciente en últimos ciclos
- **Cantidad de alumnos en ciclo previo:** 120 alumnos cursaron el prerrequisito
- **Tasa de aprobación del prerrequisito:** 75% (aprox. 90 alumnos elegibles)
- **Popularidad del curso:** Alto interés según encuestas
- **Factores externos:** Cambios en malla curricular, nuevas especializaciones, etc.

**[ESPACIO PARA CAPTURA: Panel de factores que influyen en la demanda]**

#### **3.3.4 Filtrando Predicciones**

Opciones para filtrar la visualización:

**Por Nivel de Saturación:**
- ☑️ Mostrar solo cursos en riesgo (amarillo, naranja, rojo)
- ☑️ Mostrar solo cursos con disponibilidad (verde)
- ☑️ Mostrar todos

**Por Facultad/Escuela:**
- Filtrar por su escuela o ver cursos de otras facultades (si aplica)

**Por Área de Conocimiento:**
- Matemáticas, Ciencias, Ingeniería, Humanidades, etc.

**Por Créditos:**
- Rango de 2 a 6 créditos

**Por Ciclo Sugerido en Malla:**
- Ver solo cursos de su ciclo actual o específico

**[ESPACIO PARA CAPTURA: Panel de filtros de predicción]**

#### **3.3.5 Comparando Demanda de Múltiples Cursos**

Si está indeciso entre varios cursos, puede compararlos:

**Paso 1:** Seleccione hasta 6 cursos marcando sus casillas

**Paso 2:** Haga clic en "Comparar demanda"

**Paso 3:** Aparece una visualización comparativa:

- Gráfico de barras lado a lado
- Tabla comparativa de métricas clave
- Recomendación de prioridad de matrícula

**Ejemplo de salida:**

```
Orden de prioridad sugerido para matrícula:
1. 🔴 CS201 (Saturación: 112%) - PRIORIDAD MÁXIMA
2. 🟠 MA301 (Saturación: 98%) - PRIORIDAD ALTA
3. 🟡 FI104 (Saturación: 85%) - PRIORIDAD MEDIA
4. 🟢 HU201 (Saturación: 65%) - PRIORIDAD BAJA
```

**[ESPACIO PARA CAPTURA: Vista de comparación de demanda entre múltiples cursos]**

> **💡 CONSEJO:** Use esta comparación para organizar su orden de matrícula. Comience matriculando los cursos con mayor riesgo de saturación.

#### **3.3.6 Configuración de Alertas**

Puede configurar alertas personalizadas para recibir notificaciones:

**Tipos de Alertas Disponibles:**

**1. Alerta de Cambio de Predicción**
- Notifica si la predicción de un curso de su interés cambia significativamente
- Ejemplo: Un curso pasó de 🟡 a 🔴 (aumentó el riesgo)

**2. Alerta de Apertura de Vacantes**
- Notifica si se aumentan las vacantes de un curso
- Útil si un curso estaba saturado y ahora hay más cupos

**3. Alerta de Inicio de Matrícula**
- Recordatorio automático días antes de su turno de matrícula
- Incluye resumen de cursos priorizados

**Cómo configurar alertas:**

**Paso 1:** En cualquier curso, haga clic en el ícono de campana (🔔)

**Paso 2:** Seleccione qué tipo de alerta desea activar

**Paso 3:** Elija el método de notificación:
- ☑️ Notificación en el sistema
- ☑️ Correo electrónico
- ☑️ Ambos

**Paso 4:** Haga clic en "Guardar alerta"

**[ESPACIO PARA CAPTURA: Panel de configuración de alertas]**

> **📌 NOTA:** Puede tener hasta 10 alertas activas simultáneamente. Las alertas se desactivan automáticamente después del período de matrícula.

#### **3.3.7 Interpretando el Nivel de Confianza**

Cada predicción muestra un "nivel de confianza" que indica qué tan precisa es la estimación:

- **90-100%:** Confianza muy alta - Predicción muy confiable
- **80-89%:** Confianza alta - Predicción confiable
- **70-79%:** Confianza media - Predicción aceptable pero con incertidumbre
- **< 70%:** Confianza baja - Predicción menos confiable

**Factores que afectan la confianza:**

- ✅ **Aumentan confianza:** Curso con muchos ciclos de historia, patrones estables, prerrequisitos claros
- ❌ **Disminuyen confianza:** Curso nuevo, cambios recientes en malla curricular, datos históricos limitados

> **📌 NOTA:** Incluso predicciones con confianza del 70% son útiles. Siguen siendo mejor que no tener información, pero considere mayor margen de error.

#### **3.3.8 Exportando Datos de Predicción**

Puede exportar las predicciones para análisis personal o consulta offline:

**Formato PDF:**
- Vista imprimible con gráficos
- Incluye solo cursos de su interés (filtrados)
- Ideal para mostrar a tutor o familia

**Formato Excel/CSV:**
- Datos en tabla para análisis propio
- Incluye todas las métricas y números
- Útil si desea hacer sus propios cálculos o comparaciones

**Cómo exportar:**

**Paso 1:** Configure los filtros según lo que desee exportar

**Paso 2:** Haga clic en "Exportar" en la esquina superior derecha

**Paso 3:** Seleccione formato (PDF o Excel)

**Paso 4:** El archivo se descargará automáticamente

**[ESPACIO PARA CAPTURA: Opciones de exportación de predicciones]**

#### **3.3.9 Estrategias de Matrícula Basadas en Predicciones**

**Estrategia 1: Priorización por Saturación**

Ordene su lista de matrícula de mayor a menor saturación:

1. Cursos 🔴 (saturados) - Matricular primero
2. Cursos 🟠 (alta demanda) - Matricular segundo
3. Cursos 🟡 (demanda media) - Matricular tercero
4. Cursos 🟢 (disponibles) - Matricular al final

**Estrategia 2: Plan A, B y C**

- **Plan A:** Cursos ideales (tu primera opción)
- **Plan B:** Cursos alternativos si Plan A se satura
- **Plan C:** Cursos de respaldo si Plan A y B fallan

Asegúrese de que cada plan tenga suficientes créditos y cumpla requisitos.

**Estrategia 3: Matricular Electivos en Ciclos de Baja Demanda**

Si ve que un electivo tiene alta demanda este ciclo, considere:
- Tomarlo en ciclo posterior cuando la demanda sea menor
- Sustituirlo por otro electivo menos demandado ahora
- Ver el historial para identificar ciclos con menor saturación

> **💡 CONSEJO AVANZADO:** Algunos cursos tienen demanda cíclica (alta en 2025-I, baja en 2025-II). Aproveche estos patrones para optimizar su planificación a largo plazo.

#### **3.3.10 Preguntas Frecuentes sobre Predicciones**

**P: ¿Qué tan precisas son las predicciones?**

R: El sistema tiene una precisión promedio del 85-90% según validaciones con datos reales de ciclos anteriores. La precisión varía según el curso (los cursos obligatorios tienden a tener predicciones más precisas que los electivos).

**P: ¿Las predicciones consideran cambios en la malla curricular?**

R: Sí, el sistema se actualiza cuando hay cambios oficiales en la malla. Sin embargo, cambios muy recientes (menos de un ciclo) pueden no reflejarse completamente en las predicciones.

**P: ¿Por qué algunos cursos no tienen predicción?**

R: Cursos completamente nuevos (sin historial) o cursos con datos insuficientes no muestran predicción. En esos casos, solo se muestra el número de vacantes disponibles.

**P: ¿Puedo confiar en una predicción de "disponibilidad alta" para dejar ese curso al final de mi matrícula?**

R: Generalmente sí, pero siempre hay excepciones. Factores inesperados (como cambios de último momento en oferta de secciones) pueden alterar la demanda. Sea cauteloso y tenga plan B.

**P: ¿Las predicciones se actualizan durante el período de matrícula?**

R: No en tiempo real, pero se recalculan diariamente durante el período pre-matrícula. Una vez iniciada la matrícula, el sistema muestra vacantes reales disponibles en lugar de predicciones.

---

> **💡 CONSEJO FINAL:** Use las predicciones como guía estratégica, no como verdad absoluta. Combine esta información con recomendaciones personalizadas, asesoría de su tutor y su propio criterio para tomar las mejores decisiones de matrícula.

---

<div style="page-break-after: always;"></div>

