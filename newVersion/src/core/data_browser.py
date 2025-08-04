import os

# Devuelve una lista con el nombre de todas las subcarpetas de la sección escogida
def listar_subcarpetas(category_page):
    
    try:
        # Construir la ruta absoluta
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.abspath(os.path.join(base_dir, "..", "..", category_page))
        
        folder = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]
        return folder
    except:
        return []
    