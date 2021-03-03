# proto_fastapi

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

1. py -3.7 -m venv venv
2. venv\Scripts\activate
   venv\Scripts\activate
   pyinstaller -y --clean --additional-hooks-dir hooks api/main.py --distpath api_compiled

npm run custom:serve

### Fixes

- ExecFile for the main.exe
- OS ENV not working => writing and reading in a file-
- process.env.UCOLLABORATE
- Make axios calls to fetch stuff

# PORT

- Ouvrir et ecrire dans le fichier .env lors du lancement de l'api
- npm i dotenv ou pas ???
  https://cli.vuejs.org/guide/mode-and-env.html#environment-variables ! si vuecli > 3

# Exec main

# Axios

- https://fastapi.tiangolo.com/tutorial/cors/ to prevent cors cross origin errors

# Read the env before exec file

# Fix 2

- Write into txt file (py) and read port in background (ready)
- Config axios and all methods in api.js

# Build ?

- Localhost:8080 not running on build ?
- icpMain && renderer \_\_dirname error

# Read file not in sync

- Corriger await partout
- Mettre port_config.txt dans un fichier autre que la ou est le build => Nope

- IpcMain to renderer (background callback)
- Mounted => while (port) => works
