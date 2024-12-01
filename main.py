
import argparse
from logger import init_logger


# Parser per argomenti della riga di comando


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Gestione di test a scelta multipla.")

    subparsers = parser.add_subparsers(
        dest="command", help="Comando da eseguire")

    # Sotto-comando per produrre un formato vuoto
    produce_parser = subparsers.add_parser(
        "generate_template", help="Produce un formato vuoto da compilare.")
    produce_parser.add_argument(
        "-q", "--questions", type=int, required=True, help="Numero di domande.")
    produce_parser.add_argument(
        "-c", "--choices", type=int, required=True, help="Numero di scelte per domanda.")

    produce_parser.add_argument(
        "--template_out_path", type=str, help="Percorso salvataggio template.")

    # Sotto-comando per generare il test
    output_parser = subparsers.add_parser(
        "test_generation", help="Genera il test e i relativi file.")
    output_parser.add_argument(
        "-n", "--num_tests", type=int, required=True, help="Numero di test da generare.")
    output_parser.add_argument("-f", "--filled_format_path", type=str,
                               required=True, help="Percorso del formato compilato.")
    output_parser.add_argument("-o", "--output_path", type=str,
                               required=True, help="Percorso di output per il latex.")
    output_parser.add_argument("-a", "--answers_path", type=str,
                               required=True, help="Percorso per salvare le risposte originali.")

    return parser.parse_args()


# Main
if __name__ == "__main__":

    log = init_logger()
    args = parse_arguments()

    if args.command == "generate_template":
        from src.command.Template.generate_template import Template
        log.info("Produzione del formato vuoto iniziata...")
        Format = Template(args.questions, args.choices)
        Format.generate_template()
        log.info(f"Formato vuoto prodotto con {
            args.questions} domande e {args.choices} scelte.")

    # elif args.command == "test_generation":
    #     logger.info("Generazione del test iniziata...")
    #     Test = multiple_choice_test()
    #     working_directory = os.getcwd()

    #     # Risoluzione dei percorsi
    #     Path_filled_format = os.path.abspath(args.filled_format_path)
    #     Output_path = os.path.abspath(args.output_path)
    #     Path_original_answers = os.path.abspath(args.answers_path)

    #     # Creazione delle directory di output, se non esistono
    #     os.makedirs(Output_path, exist_ok=True)
    #     os.makedirs(Path_original_answers, exist_ok=True)

    #     # Esecuzione del comando
    #     Test.output(args.num_tests, Path_filled_format,
    #                 Output_path, Path_original_answers)
    #     logger.info(f"Test generati: {args.num_tests}")
    #     logger.info(f"Percorso formato compilato: {Path_filled_format}")
    #     logger.info(f"Percorso output latex: {Output_path}")
    #     logger.info(f"Percorso risposte: {Path_original_answers}")

    else:
        log.error("Nessun comando valido specificato.")
        raise ValueError("Command not yet implemented")
