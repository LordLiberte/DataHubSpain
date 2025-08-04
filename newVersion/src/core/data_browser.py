import os

# Devuelve una lista con el nombre de todas las subcarpetas de la sección escogida
def listar_subcarpetas(category_page):
    
    try:
        folder = [f for f in os.listdir(category_page) if os.path.isdir(os.path.join(category_page, f))]
        return folder
    except:
        return []
    