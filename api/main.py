from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.reddit import users, posts
from routers.monsterhunter import weapons, monsters
from routers.projects import projects, a
from routers.config import config
from init_database_monsterhunter import init_database_monster
from init_database_reddit import init_database_reddit
from utils.run_on_port import find_free_port
from utils.config import DATABASE_PATH
from os.path import join
import os
import uvicorn
import logging

port_app = find_free_port()
# f = open(os.path.join(os.getcwd(), ".env"), "w")
# f.write(f"VUE_APP_PORT_API={port_app}")
# # f.write(f"VUE_APP_EXE_PATH={os.a}")
# f.close()
# if not os.path.exists(os.path.join(os.getcwd(), "public")):
#     os.makedirs(os.path.join(os.getcwd(), "public"))

# f = open(os.path.join(os.getcwd(), "configs", "port_config.txt"), "w")
f = open(r"D:/configs/port_config.txt", "w")

f.write(f"{port_app}")
# f.write(f"VUE_APP_EXE_PATH={os.a}")
f.close()

app = FastAPI()

# logging.basicConfig(
#     level=2,
#     format="%(asctime)-15s %(levelname)-8s %(message)s"
# )

origins = [
    "http://localhost:",
    "http://localhost:8080",
    "http://localhost:*",
    "https://localhost:*",
    # "app://.",
    # "app://.*",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(weapons.router)
app.include_router(monsters.router)
app.include_router(projects.router)
app.include_router(a.router)
app.include_router(config.router)

# init_database_reddit(join(DATABASE_PATH, "reddit.db"))
# init_database_monster(join(DATABASE_PATH, "monsterhunter.db"))

# logger = logging.getLogger("My logs")
# logger.setLevel(logging.DEBUG)
# logger.debug("TEST")


@app.get("/")
async def root():
    return {"message": "Hello World"}

print("-------------------PATHS--------------------")
print(os.getcwd())
print(os.path.abspath("./"))
print("--------------------------------------------")

os.environ["UCOLLABORATE"] = f"{port_app}"
print(os.getenv("UCOLLABORATE"))
print("Bruuuuuuuuuuuuh")
uvicorn.run(app, host="127.0.0.1", port=port_app, reload=False)
