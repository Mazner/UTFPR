import os
import sys
import subprocess

def execute_tpp_files(directory):
    # Verifica se o diretório existe
    if not os.path.isdir(directory):
        print(f"O diretório {directory} não existe.")
        return

    # Lista todos os arquivos do diretório
    for filename in os.listdir(directory):
        # Verifica se o arquivo tem a extensão .tpp
        if filename.endswith('.tpp'):
            file_path = os.path.join(directory, filename)
            print(f"Executando o arquivo: {file_path}")
            
            # Chama o script Python que processa o arquivo .tpp
            result = subprocess.run(['python', 'tppparser.py', file_path], capture_output=True, text=True)
            
            # Mostra a saída do comando
            if result.returncode == 0:
                print(f"Sucesso na execução de {filename}:\n{result.stdout}")
            else:
                print(f"Erro na execução de {filename}:\n{result.stderr}")

def main():
    # Verifica se o diretório foi passado como parâmetro
    if len(sys.argv) != 2:
        print("Uso: python executa_tpp.py <diretorio>")
        return

    directory = sys.argv[1]
    execute_tpp_files(directory)

if __name__ == "__main__":
    main()
