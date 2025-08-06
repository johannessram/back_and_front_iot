# Installation du projet FastAPI

### 1. Créer un environnement virtuel

```bash
python -m venv .venv
````

### 2. Activer l’environnement virtuel

* Sous **Windows** :

```bash
.venv\Scripts\activate
```

* Sous **Linux/macOS** :

```bash
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer le serveur FastAPI

```bash
uvicorn main:app --reload
```

### 5. API access

documentation : `http://localhost:8000/docs`
api get : `http://localhost:8000/get-distance`
api post : `http://localhost:8000/new-distance`
