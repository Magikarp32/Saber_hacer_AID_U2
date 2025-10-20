import json
import yaml
import xml.etree.ElementTree as ET
from xml.dom import minidom

def ingresar_datos_docentes():
    """
    Función para ingresar los datos de los docentes
    Retorna una lista de diccionarios con la información
    """
    docentes = []
    
    print("=== SISTEMA DE REGISTRO DE DOCENTES - EDIFICIO 2 ===")
    
    while True:
        print("\n--- Ingresar datos del docente ---")
        
        # Validación del nombre
        while True:
            nombre = input("Nombre del empleado: ").strip()
            if nombre:
                break
            print("Error: El nombre no puede estar vacío")
        
        # Validación de la especialidad
        while True:
            especialidad = input("Especialidad: ").strip()
            if especialidad:
                break
            print("Error: La especialidad no puede estar vacía")
        
        # Validación del número de empleado
        while True:
            try:
                numero_empleado = int(input("Número de empleado: "))
                if numero_empleado > 0:
                    break
                else:
                    print("Error: El número de empleado debe ser positivo")
            except ValueError:
                print("Error: Debe ingresar un número válido")
        
        # Crear diccionario con los datos
        docente = {
            "nombre": nombre,
            "especialidad": especialidad,
            "numero_empleado": numero_empleado
        }
        
        docentes.append(docente)
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea ingresar otro docente? (s/n): ").lower()
        if continuar != 's':
            break
    
    return docentes

def generar_archivo_json(docentes, nombre_archivo="docentes.json"):
    """
    Genera un archivo JSON con los datos de los docentes
    """
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(docentes, archivo, indent=4, ensure_ascii=False)
        print(f"✓ Archivo JSON generado: {nombre_archivo}")
    except Exception as e:
        print(f"✗ Error al generar JSON: {e}")

def generar_archivo_yaml(docentes, nombre_archivo="docentes.yaml"):
    """
    Genera un archivo YAML con los datos de los docentes
    """
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            yaml.dump(docentes, archivo, default_flow_style=False, allow_unicode=True)
        print(f"✓ Archivo YAML generado: {nombre_archivo}")
    except Exception as e:
        print(f"✗ Error al generar YAML: {e}")

def generar_archivo_xml(docentes, nombre_archivo="docentes.xml"):
    """
    Genera un archivo XML con los datos de los docentes
    """
    try:
        # Crear elemento raíz
        root = ET.Element("docentes")
        
        # Agregar cada docente como un elemento
        for docente in docentes:
            docente_elem = ET.SubElement(root, "docente")
            
            ET.SubElement(docente_elem, "nombre").text = docente["nombre"]
            ET.SubElement(docente_elem, "especialidad").text = docente["especialidad"]
            ET.SubElement(docente_elem, "numero_empleado").text = str(docente["numero_empleado"])
        
        # Convertir a string con formato
        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
        
        # Guardar archivo
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(xml_str)
        
        print(f"✓ Archivo XML generado: {nombre_archivo}")
    except Exception as e:
        print(f"✗ Error al generar XML: {e}")

def mostrar_resumen(docentes):
    """
    Muestra un resumen de los datos ingresados
    """
    print("\n" + "="*50)
    print("RESUMEN DE DOCENTES REGISTRADOS")
    print("="*50)
    
    for i, docente in enumerate(docentes, 1):
        print(f"\nDocente {i}:")
        print(f"  Nombre: {docente['nombre']}")
        print(f"  Especialidad: {docente['especialidad']}")
        print(f"  Número de empleado: {docente['numero_empleado']}")

def main():
    """
    Función principal del programa
    """
    print("SISTEMA DE GESTIÓN DE DOCENTES - EDIFICIO 2")
    print("Este programa permitirá registrar docentes y generar archivos en múltiples formatos.\n")
    
    try:
        # Ingresar datos
        docentes = ingresar_datos_docentes()
        
        if not docentes:
            print("No se ingresaron docentes. El programa terminará.")
            return
        
        # Mostrar resumen
        mostrar_resumen(docentes)
        
        # Generar archivos
        print("\n" + "="*50)
        print("GENERANDO ARCHIVOS...")
        print("="*50)
        
        generar_archivo_json(docentes)
        generar_archivo_yaml(docentes)
        generar_archivo_xml(docentes)
        
        print("\n¡Proceso completado exitosamente!")
        print("Se han generado los archivos: docentes.json, docentes.yaml, docentes.xml")
        
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    main()