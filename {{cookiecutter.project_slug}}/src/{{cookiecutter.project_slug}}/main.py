def main() -> None:
    """Default main function for utilizing the {{ cookiecutter.project_name }}."""
    from {{cookiecutter.project_slug}}.logger import get_logger
    logger = getLogger(__name__)
    logger.info("Projekt {{ cookiecutter.project_name }} läuft.")


if __name__ == "__main__":
    main()
