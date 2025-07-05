from logging import getLogger


def main() -> None:
    """Default main function for utilizing the {{ cookiecutter.project_name }}."""
    logger = getLogger(__name__)
    logger.info("Projekt {{ cookiecutter.project_name }} läuft.")


if __name__ == "__main__":
    main()
