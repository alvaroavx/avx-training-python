# ==============================
# Gestor de Lista de Tareas
# ==============================
# Objetivo: aplicar estructuras de control
# (if / while / for / break / try-except)
# usando una lista simple para almacenar tareas.

# Lista vacía al inicio
tareas = []

print("=== GESTOR DE TAREAS ===")

while True:
    print("\nOpciones:")
    print("1) Agregar tarea")
    print("2) Ver tareas")
    print("3) Marcar tarea como completada")
    print("4) Eliminar tarea")
    print("5) Salir")

    opcion = input("Elige una opción: ").strip()

    # ==============================
    # Opción 1: agregar tarea
    # ==============================
    if opcion == "1":
        tarea = input("Escribe la nueva tarea: ").strip()
        if tarea != "":
            tareas.append(tarea)
            print("Tarea agregada.")
        else:
            print("No se agregó nada (tarea vacía).")

    # ==============================
    # Opción 2: listar tareas
    # ==============================
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas aún.")
        else:
            print("\nLista de tareas:")
            for i in range(len(tareas)):
                print(f"{i + 1}. {tareas[i]}")

    # ==============================
    # Opción 3: marcar completada
    # ==============================
    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para marcar.")
        else:
            print("\nTareas actuales:")
            for i in range(len(tareas)):
                print(f"{i + 1}. {tareas[i]}")
            try:
                pos = int(input("Número de tarea completada: ")) - 1
                if 0 <= pos < len(tareas):
                    print(f"Tarea completada: {tareas[pos]}")
                    tareas[pos] = f"[Hecha] {tareas[pos]}"
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Debes ingresar un número válido.")

    # ==============================
    # Opción 4: eliminar tarea
    # ==============================
    elif opcion == "4":
        if len(tareas) == 0:
            print("No hay tareas para eliminar.")
        else:
            print("\nTareas actuales:")
            for i in range(len(tareas)):
                print(f"{i + 1}. {tareas[i]}")
            try:
                pos = int(input("Número de tarea a eliminar: ")) - 1
                if 0 <= pos < len(tareas):
                    eliminada = tareas.pop(pos)
                    print(f"Se eliminó: {eliminada}")
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Debes ingresar un número válido.")

    # ==============================
    # Opción 5: salir
    # ==============================
    elif opcion == "5":
        confirmar = input("¿Seguro que quieres salir? (s/n): ").lower()
        if confirmar == "s":
            print("¡Hasta luego!")
            break
        else:
            print("Volviendo al menú...")

    # ==============================
    # Opción inválida
    # ==============================
    else:
        print("Opción no válida. Intenta de nuevo.")
