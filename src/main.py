import os
import sys
from services.dataInsights import show_median_comparator, show_kurtosis_and_skewness, df_describe_and_info
from services.processData import process_csv_path
from services.showBox import show_box
from services.showCorrelation import show_correlation, show_correlation_between_files
from services.showHistogram import show_histogram

def clear_screen():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_user():
    """Pausa a execução até que o usuário pressione Enter."""
    input("\nPressione Enter para continuar...")

def display_menu(options, title):
    """Exibe um menu de opções, limpando a tela antes de exibir."""
    clear_screen()
    print(f"=== {title} ===")
    for key, value in options.items():
        print(f"{key} - {value}")
    print("0 - Voltar")

def main_menu(csv1_final, csv2_final):
    """Menu principal."""
    while True:
        options = {
            "1": "Comparadores",
            "2": "Visualizadores",
            "3": "Descrevedores"
        }
        display_menu(options, "Menu Principal")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            comparadores_menu(csv1_final, csv2_final)
        elif choice == "2":
            visualizadores_menu(csv1_final, csv2_final)
        elif choice == "3":
            descrevedores_menu(csv1_final, csv2_final)
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            wait_for_user()

def comparadores_menu(csv1_final, csv2_final):
    """Menu de comparadores."""
    while True:
        options = {
            "1": "Mediana",
            "2": "Curtose - Assimetria"
        }
        display_menu(options, "Comparadores")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            clear_screen()
            show_median_comparator(csv1_final, csv2_final)
            wait_for_user()
        elif choice == "2":
            clear_screen()
            show_kurtosis_and_skewness(csv1_final, csv2_final)
            wait_for_user()
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            wait_for_user()

def visualizadores_menu(csv1_final, csv2_final):
    """Menu de visualizadores."""
    while True:
        options = {
            "1": "Box Plot",
            "2": "Histograma",
            "3": "Correlação",
            "4": "Correlação entre arquivos"
        }
        display_menu(options, "Visualizadores")
        choice = input("Escolha uma opção: ").strip()

        if choice in {"1", "2", "3"}:  
            df_choice = input("Deseja analisar o DF1 ou DF2? (1/2): ").strip()
            
            if df_choice == "1":
                csv_selected = csv1_final
            elif df_choice == "2":
                csv_selected = csv2_final
            else:
                print("Opção inválida. Retornando ao menu.")
                continue  

        if choice == "1":
            clear_screen()
            show_box(csv_selected)
        elif choice == "2":
            clear_screen()
            show_histogram(csv_selected)
        elif choice == "3":
            clear_screen()
            show_correlation(csv_selected)
            wait_for_user()
        elif choice == "4":
            clear_screen()
            show_correlation_between_files(csv1_final, csv2_final)
            wait_for_user()
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def descrevedores_menu(csv1_final, csv2_final):
    """Menu de descrevedores."""
    while True:
        options = {
            "1": "Descrever e Informações"
        }
        display_menu(options, "Descrevedores")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            while True:
                df_choice = input("Deseja analisar o DF1 ou DF2? (1/2): ").strip()
                if df_choice == "1":
                    clear_screen()
                    df_describe_and_info(csv1_final)
                    break
                elif df_choice == "2":
                    clear_screen()
                    df_describe_and_info(csv2_final)
                    break
                else:
                    print("Opção inválida. Escolha 1 para DF1 ou 2 para DF2.")
                    wait_for_user()

            wait_for_user()
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            wait_for_user()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py <caminho_csv1> <caminho_csv2>")
        sys.exit(1)

    csv1 = sys.argv[1]
    csv2 = sys.argv[2]

    print(f'Comparando {csv1} e {csv2}')

    csv1_final = process_csv_path(csv1)
    csv2_final = process_csv_path(csv2)

    main_menu(csv1_final, csv2_final)
