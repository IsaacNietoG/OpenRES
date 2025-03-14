# RES: Remote Environment Storage

# Especificación de Requerimientos de Software (SRS)

## 1. Introducción

### 1.1 Propósito

El objetivo principal de este sistema es proporcionar una forma segura y centralizada para almacenar y gestionar variables de entorno en la nube. Permitirá a los desarrolladores acceder a estas variables de manera segura y eficiente mediante una API y una CLI.

### 1.2 Alcance

El sistema permitirá a los usuarios:

- Almacenar variables de entorno de forma cifrada con algoritmos resistentes a ataques de computación cuántica.
- Recuperar variables de entorno de manera segura.
- Modificar y eliminar variables según permisos establecidos.
- Gestionar versiones de las variables.
- Integrarse con aplicaciones a través de un cliente ligero de solo lectura.
- Organizar las variables en distintos proyectos dentro de una instancia de nube, asegurando que cada desarrollador solo tenga acceso a los proyectos asignados.
- Separar los secretos según el entorno (producción, testing, desarrollo, etc.), permitiendo un acceso diferenciado según el contexto de uso.

### 1.3 Definiciones y Acrónimos

- **CLI (Command Line Interface):** Interfaz de línea de comandos para interactuar con el sistema.
- **API (Application Programming Interface):** Interfaz que permite la comunicación con el sistema mediante protocolos estandarizados.
- **Cifrado Post-Cuántico:** Algoritmos de cifrado diseñados para ser seguros ante ataques con computadoras cuánticas.
- **Microcliente:** Componente ligero que permite leer variables de entorno desde el sistema sin acceder a funcionalidades de modificación.
- **Proyecto:** Espacio dentro de la nube donde se almacenan y gestionan variables de entorno específicas de un equipo o aplicación.
- **Entorno:** Clasificación de los secretos según su contexto de uso (producción, testing, desarrollo, etc.).

### 1.4 Referencias

- Documentación de seguridad en almacenamiento de secretos.
- Estándares de cifrado recomendados (AES-256, TLS 1.3, y algoritmos post-cuánticos como Kyber o Dilithium).
- Prácticas recomendadas para la gestión de secretos en entornos de desarrollo.

## 2. Descripción general del sistema

### 2.1 Perspectiva del producto

Este sistema funcionará como un servicio independiente que podrá integrarse con aplicaciones externas mediante su API. Además, contará con una CLI para que los desarrolladores gestionen sus variables de entorno de forma sencilla. Cada empresa podrá desplegar su propia instancia de nube y organizar sus secretos en distintos proyectos y entornos.

### 2.2 Funcionalidades principales

- Autenticación de usuarios.
- Almacenamiento cifrado de variables con soporte post-cuántico.
- Control de acceso basado en permisos.
- Organización de secretos en distintos proyectos dentro de la nube.
- Separación de secretos por entorno (producción, testing, desarrollo, etc.).
- Recuperación de variables de entorno según permisos asignados.
- CLI para gestionar las variables.
- API REST para integración con aplicaciones.
- Microcliente de solo lectura.

### 2.3 Usuarios y público objetivo

- Desarrolladores de software.
- Equipos DevOps.
- Empresas que gestionan entornos de desarrollo y producción.

### 2.4 Restricciones y dependencias

- El servidor deberá ejecutarse en un entorno con soporte para contenedores Docker.
- Requerirá un mecanismo seguro de autenticación (OAuth 2.0, JWT, etc.).
- Deberá implementar cifrado en reposo y en tránsito, incluyendo algoritmos post-cuánticos.
- Cada empresa podrá desplegar su propia instancia de nube para gestionar secretos de múltiples proyectos y entornos.

## 3. Requerimientos específicos

### 3.1 Requerimientos funcionales

1. El sistema debe permitir a los usuarios autenticarse mediante credenciales seguras.
2. El sistema debe permitir almacenar variables de entorno de manera cifrada utilizando algoritmos post-cuánticos.
3. Los usuarios deben poder recuperar variables de entorno según sus permisos.
4. Debe haber soporte para control de versiones de variables.
5. La API REST debe proporcionar endpoints para CRUD de variables.
6. La CLI debe ofrecer comandos para interacción con la API.
7. El microcliente debe poder recuperar variables en un formato ligero y eficiente.
8. Los secretos deben estar organizados en proyectos separados dentro de la nube, asegurando que los accesos sean específicos para cada proyecto.
9. El sistema debe permitir la clasificación y acceso diferenciado a variables según el entorno en el que serán utilizadas.

### 3.2 Requerimientos no funcionales

1. El sistema debe garantizar que todas las comunicaciones estén cifradas (TLS 1.3 o superior, con opciones post-cuánticas cuando estén disponibles).
2. Debe soportar al menos 1000 usuarios simultáneos sin degradación del rendimiento.
3. El tiempo de respuesta de la API no debe exceder los 200ms en condiciones normales de carga.
4. El almacenamiento debe cumplir con los estándares de seguridad para protección de datos sensibles.
5. Cada instancia de nube debe permitir la separación lógica de secretos por proyecto y entorno.
6. La autenticación debe soportar múltiples factores (MFA) para fortalecer la seguridad.
7. Se deben registrar eventos de acceso y modificación de variables para auditoría.

### 3.3 Interfaces

1. **Interfaz de usuario CLI:** Debe ser intuitiva y proporcionar comandos claros para la gestión de variables.
2. **Interfaz API REST:** Debe seguir principios RESTful y utilizar JSON como formato de respuesta.
3. **Microcliente:** Debe permitir la lectura de variables de entorno con un mínimo de dependencias y sobrecarga.

## 4. Seguridad

### 4.1 Autenticación y Control de Acceso

- Implementación de OAuth 2.0 o JWT para la autenticación segura de los usuarios.
- Soporte para autenticación multifactor (MFA) opcional.
- Asignación de roles y permisos para controlar el acceso a variables y proyectos.

### 4.2 Cifrado

- Cifrado en reposo utilizando AES-256.
- Cifrado en tránsito utilizando TLS 1.3 con compatibilidad para algoritmos post-cuánticos.
- Almacenamiento de claves de cifrado en un módulo seguro de hardware (HSM) o equivalente.

### 4.3 Almacenamiento Seguro

- Los secretos deben estar cifrados antes de ser almacenados en la base de datos.
- No se deben almacenar credenciales en texto plano.
- Se debe aplicar rotación de claves de cifrado periódicamente.

### 4.4 Auditoría y Monitoreo

- Registro de eventos de autenticación, acceso y modificaciones a variables.
- Alertas en caso de intentos de acceso no autorizados.
- Soporte para integración con sistemas de monitoreo de seguridad (SIEM).

## 5. Anexos y referencias

[Diagramas C4](https://www.notion.so/Diagramas-C4-1ad093228e1a80d9ac04ceef490ea1eb?pvs=21)

- Documentación de integración con aplicaciones externas.
- Guía de seguridad recomendada para almacenamiento de secretos.