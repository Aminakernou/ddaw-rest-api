# DDAW REST API

API RESTful pour une plateforme de contenu — gestion des utilisateurs,
articles, catégories et commentaires.

---

## Contexte du projet

Cette application permet à des utilisateurs de publier des articles
classés par catégories et de commenter les publications des autres.

Chaque utilisateur peut :
- Créer un compte avec un profil personnel
- Publier et gérer des articles
- Commenter les articles

---

## Technologies

- **Python 3.11** + **FastAPI**
- **SQLAlchemy** (ORM)
- **PostgreSQL 15** (base de données)
- **Docker** + **Docker Compose**
- **Bcrypt** (sécurisation des mots de passe)

---

## Relations entre les modèles

| Relation | Entre | Type |
|----------|-------|------|
| User → Profile | Un user a un seul profil | One-to-One |
| User → Comments | Un user a plusieurs commentaires | One-to-Many |
| Article ↔ Category | Un article a plusieurs catégories | Many-to-Many |

---

## Structure du projet

```
ddaw-rest-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── user.py
│   │   ├── profile.py
│   │   ├── article.py
│   │   ├── category.py
│   │   └── comment.py
│   └── routes/
│       ├── user_routes.py
│       ├── article_routes.py
│       ├── category_routes.py
│       └── comment_routes.py
├── Dockerfile
├── docker-compose.yml
├── init.sql
└── requirements.txt
```

---

## Lancer le projet

### Prérequis
- Docker Desktop installé et lancé

### Commandes

```bash
git clone https://github.com/Aminakernou/ddaw-rest-api.git
cd ddaw-rest-api
docker-compose up --build
```

L'API est disponible sur : **http://localhost:8000/docs**

---

## Routes de l'API

### Users
| Méthode | Route | Description |
|---------|-------|-------------|
| GET | /users/ | Liste tous les utilisateurs |
| POST | /users/ | Créer un utilisateur |
| GET | /users/{id} | Détail d'un utilisateur |
| PUT | /users/{id} | Modifier un utilisateur |
| DELETE | /users/{id} | Supprimer un utilisateur |
| POST | /users/{id}/profile | Créer le profil |
| GET | /users/{id}/profile | Voir le profil |
| PUT | /users/{id}/profile | Modifier le profil |

### Articles
| Méthode | Route | Description |
|---------|-------|-------------|
| GET | /articles/ | Liste tous les articles |
| POST | /articles/ | Créer un article |
| GET | /articles/{id} | Détail d'un article |
| PUT | /articles/{id} | Modifier un article |
| DELETE | /articles/{id} | Supprimer un article |

### Categories
| Méthode | Route | Description |
|---------|-------|-------------|
| GET | /categories/ | Liste toutes les catégories |
| POST | /categories/ | Créer une catégorie |
| GET | /categories/{id} | Détail d'une catégorie |
| PUT | /categories/{id} | Modifier une catégorie |
| DELETE | /categories/{id} | Supprimer une catégorie |

### Comments
| Méthode | Route | Description |
|---------|-------|-------------|
| GET | /comments/ | Liste tous les commentaires |
| POST | /comments/ | Créer un commentaire |
| GET | /comments/{id} | Détail d'un commentaire |
| DELETE | /comments/{id} | Supprimer un commentaire |
| GET | /comments/article/{id} | Commentaires d'un article |

---

## Exemples de requêtes

### Créer un utilisateur
```
POST /users/
```
```json
{
  "name": "asala",
  "email": "asala@mail.com",
  "password": "monmotdepasse",
  "role": "membre"
}
```

### Créer un article
```
POST /articles/
```
```json
{
  "title": "Introduction à FastAPI",
  "content": "FastAPI est un framework moderne...",
  "date": "2026-04-24",
  "auteur_id": 1
}
```

### Créer un commentaire
```
POST /comments/
```
```json
{
  "body": "Super article !",
  "date": "2026-04-30",
  "article_id": 1,
  "user_id": 2
}
```

---

## Données de test

Un fichier `init.sql` est inclus avec des données de test.
Il s'exécute automatiquement au démarrage de Docker.

Utilisateurs disponibles :
- amina@mail.com — mot de passe : password123
- samy@mail.com — mot de passe : password123
- asala@mail.com — mot de passe : password123

---

## Docker Hub

Image disponible sur Docker Hub :
**https://hub.docker.com/r/aminakernou/ddaw-api**

```bash
docker pull aminakernou/ddaw-api:latest
```

---

## Dépôt GitHub

https://github.com/Aminakernou/ddaw-rest-api

