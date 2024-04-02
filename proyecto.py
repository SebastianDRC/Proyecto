import datetime

class tarea:
    def __init__(self, title, descripcion, due_date=None):
        self.title = title
        self.descripcion = descripcion
        self.due_date = due_date
        self.completed = False

    def tarea_completada(self):
        self.completed = True

    def __str__(self):
        status = "Completada" if self.completed else "Pendiente"
        due_date_str = self.due_date.strftime('%Y-%m-%d') if self.due_date else "N/A"
        return f"Título: {self.title}\nDescripción: {self.descripcion}\nEstado: {status}\nFecha de vencimiento: {due_date_str}\n"


class tareaManager:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def tareas_pendientes(self):
        tareas_pendientes = [tarea for tarea in self.tareas if not tarea.completed]
        if tareas_pendientes:
            print("Tareas pendientes:")
            for tarea in tareas_pendientes:
                print(tarea)
        else:
            print("No hay tareas pendientes.")

    def tareas_completadas(self):
        tareas_completadas = [tarea for tarea in self.tareas if tarea.completed]
        if tareas_completadas:
            print("Tareas completadas:")
            for tarea in tareas_completadas:
                print(tarea)
        else:
            print("No hay tareas completadas.")

    def recordatorio_tarea(self):
        today = datetime.date.today()
        for tarea in self.tareas:
            if tarea.due_date and not tarea.completed:
                if (tarea.due_date - today).days <= 1:
                    print(f"¡Recordatorio! La tarea '{tarea.title}' está próxima a su fecha de vencimiento.")


if __name__ == "__main__":
    tarea_manager = tareaManager()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas pendientes")
        print("4. Mostrar tareas completadas")
        print("5. Salir")

        opcion = input("Ingrese su elección: ")

        if opcion == "1":
            title = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            due_date_str = input("Ingrese la fecha de vencimiento (opcional - formato YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
            nueva_tarea = tarea(title, descripcion, due_date)
            tarea_manager.agregar_tarea(nueva_tarea)
            print("Tarea agregada exitosamente.")

        elif opcion == "2":
            tarea_manager.tareas_pendientes()
            tarea_index = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
            if 0 <= tarea_index < len(tarea_manager.tareas):
                tarea_manager.tareas[tarea_index].tarea_completada()
                print("Tarea marcada como completada.")
            else:
                print("Número de tarea no válido.")

        elif opcion == "3":
            tarea_manager.tareas_pendientes()

        elif opcion == "4":
            tarea_manager.tareas_completadas()

        elif opcion == "5":
            break

        tarea_manager.recordatorio_tarea()
