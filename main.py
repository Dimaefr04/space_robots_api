from fastapi import FastAPI, HTTPException

app = FastAPI()

robots = [
    {"id": 1, "name": "Кьюриосити", "planet": "Марс", "status": "active"},
    {"id": 2, "name": "Луноход-1", "planet": "Луна", "status": "inactive"},
    {"id": 3, "name": "Персеверанс", "planet": "Марс", "status": "active"}
]

@app.get("/")
def read_root():
    return {"message": "API каталога роботов"}

@app.get("/robots")
def get_robots(status: str = None):
    if status is not None:
        result = []
        for robot in robots:
            if robot["status"] == status:
                result.append(robot)
        return result
    return robots

@app.get("/robots/{robot_id}")
def get_robot(robot_id: int):
    for robot in robots:
        if robot["id"] == robot_id:
            return robot
    raise HTTPException(status_code=404, detail="Робот не найден")