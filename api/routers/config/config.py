from fastapi import APIRouter
import os
# Next 2 import usefuls for more robust solutions to kill a process
# import signal
# import psutil

router = APIRouter(
    prefix="/api/config",
    tags=["config"],
    responses={404: {"description": "Not Found"}}
)


@router.get("/process")
async def get_process():
    print(os.getenv("UCOLLABORATE"))
    return os.getenv("UCOLLABORATE")


@router.get("/kill")
async def kill_process():
    # find the current process (process id) and kills it
    process_to_kill = os.getpid()
    os.kill(process_to_kill, 9)  # 9 == signal to kill
    # More robust way to kill a specific processs
    # for proc in psutil.process_iter():
    #     for conn in proc.connections(kind='tcp'):
    #         if conn.status == psutil.CONN_LISTEN and conn.laddr.port == int(os.getenv("UCOLLABORATE")):
    #             print(proc.pid)

    #             # port_to_kill = proc['pid']
    #             # print(proc['pid'])
    #             port_to_kill = proc.pid

    # return port_to_kill
