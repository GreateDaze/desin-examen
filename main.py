from app.controllers.task_controller import TaskController


def main() -> None:
    controller = TaskController()
    controller.run()


if __name__ == "__main__":
    main()
