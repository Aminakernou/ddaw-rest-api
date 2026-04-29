# Module Commentaires

## Description
Gestion des commentaires liés aux articles et utilisateurs.

## Modèle Comment

```json
{
  "id": 1,
  "body": "Très bon article",
  "date": "2026-04-29",
  "article_id": 1,
  "user_id": 1
}
```

## Relations

- Many-to-One avec Article
- Many-to-One avec User

## Routes API

GET /comments  
GET /comments/{id}  
POST /comments  
DELETE /comments/{id}  
GET /comments/article/{id}

## Docker

Lancer :

```bash
docker-compose up --build
```