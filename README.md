# Portafolio Grupal - Construcción de Software (Grupo D)

Este repositorio contiene el desarrollo del proyecto grupal para la asignatura **Construcción de Software**, correspondiente al curso de **Ingeniería de Sistemas e Informática**. El objetivo fue construir un portafolio profesional para cada integrante, aplicar pruebas automatizadas y simular un entorno de desarrollo moderno con ORM, TDD y CI/CD.

## 👥 Integrantes del Grupo

- Jonathan Vicente Alvarez Coloma  
- Daniel Alberto Ipince Antunez  
- Richard Ángel Nina Chicaña   
- Washington Olarte Velásquez  
- Carlos Eduardo Varas Pérez  

## 🚀 Descripción del Proyecto

El proyecto consistió en desarrollar un sitio grupal con login y portafolios individuales, aplicando buenas prácticas de ingeniería de software:

- Desarrollo orientado a pruebas (TDD)
- Simulación de base de datos con clases (ORM)
- Validaciones automatizadas (CI/CD)
- Estructura modular con modelos en Python
- Hospedaje mediante GitHub Pages

## 🧪 Pruebas Unitarias

Las pruebas están distribuidas en dos niveles:

### Portafolios individuales (ej. Jonathan Alvarez)

- `test_posts.py` → Validación de proyectos
- `test_users.py` → Validación de emails
- `test_education.py` → Educación formal
- `test_experience.py` → Experiencia laboral
- `test_skills.py` → Habilidades técnicas

### Sitio grupal (login)

- `test_users_login.py` → Validación de usuarios desde archivo JSON

Las pruebas se ejecutan automáticamente mediante GitHub Actions en cada `push` o `pull_request`.

## ⚙️ Simulación ORM

Las entidades (`Post`, `User`, `Education`, `Experience`, `Skill`) fueron modeladas como clases Python con conversión a diccionario mediante `to_dict()`. Esto simula el comportamiento de ORMs como Django o SQLAlchemy.

## 🔒 Login Grupal

El sistema de login lee usuarios desde `users.json` y valida credenciales mediante `users.py`.

```json
[
  {"usuario": "jonathan", "clave": "jon@web.com"},
  {"usuario": "carlos", "clave": "car123"},
  {"usuario": "daniel", "clave": "daniel456"}
]
