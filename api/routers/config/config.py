from fastapi import APIRouter
import os
import signal
# import psutil

router = APIRouter(
    prefix="/api/config",
    tags=["config"],
    responses={404: {"description": "Not Found"}}
)


@router.get("/process")
async def get_process():
    # works
    print(os.getenv("UCOLLABORATE"))
    return os.getenv("UCOLLABORATE")


@router.get("/kill")
async def kill_process():
    # works
    port_to_kill = os.getpid()
    os.kill(port_to_kill, 9)
    # for proc in psutil.process_iter():
    #     for conn in proc.connections(kind='tcp'):
    #         if conn.status == psutil.CONN_LISTEN and conn.laddr.port == int(os.getenv("UCOLLABORATE")):
    #             print(conn)
    #             print(proc)
    #             print(proc.pid)

    #             # port_to_kill = proc['pid']
    #             # print(proc['pid'])
    #             port_to_kill = proc.pid

    # print(f" GET PID ? {os.getpid()}")
    # return port_to_kill
