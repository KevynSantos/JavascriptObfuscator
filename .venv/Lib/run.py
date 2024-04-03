import os
from jsmin import jsmin
from jproperties import Properties

configs = Properties()

with (open('Obfuscator.properties', 'rb') as config_file):
    configs.load(config_file)
    # Diretório onde estão os arquivos .js
    directory = configs.get("path").data

    # Listar todos os arquivos .js no diretório
    js_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".js")]

    try:
        # Para cada arquivo .js, minificar e sobrescrever o arquivo
        for js_file in js_files:
            with open(js_file, "r", encoding="utf-8") as file:
                original_code = file.read()

            # Minificar o código JavaScript
            minified_code = jsmin(original_code)

            # Sobrescrever o arquivo com o código minificado
            with open(js_file, "w", encoding="utf-8") as file:
                file.write(minified_code)

        print("Sucesso")
    except Exception as e:
        print(f"Falha ao minificar os arquivos JavaScript: {e}")