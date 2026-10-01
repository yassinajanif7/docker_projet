# docker_projet

Petit exemple pour exécuter un script Python avec ses dépendances dans un conteneur Docker.

## Contenu

- `app.py` : utilise NumPy et Matplotlib pour générer une courbe sinus.
- `requirements.txt` : dépendances Python.
- `Dockerfile` : instructions pour construire l'image Docker.
- `.dockerignore` : fichiers exclus du contexte de construction.

## 1. Construire l'image

```bash
docker build -t python-numpy-matplotlib .
```

Docker lit le `Dockerfile`, part de l'image `python:3.12-slim`, puis installe les dépendances de `requirements.txt`.

## 2. Lancer le conteneur

Linux/macOS :

```bash
docker run --rm -v "$(pwd):/output" python-numpy-matplotlib
```

Pour simplement exécuter le script sans récupérer l'image générée :

```bash
docker run --rm python-numpy-matplotlib
```

## Structure

```text
docker_projet/
├── Dockerfile
├── requirements.txt
├── app.py
├── .dockerignore
└── README.md
```

## Principe

```text
Code Python
    |
    v
requirements.txt
    |
    v
docker build
    |
    v
Image Docker
(Python + NumPy + Matplotlib + app.py)
    |
    v
docker run
    |
    v
Conteneur
    |
    v
Exécution de app.py
```
