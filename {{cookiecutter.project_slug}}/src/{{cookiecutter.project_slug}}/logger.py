import logging

def get_logger(name: str = None) -> logging.Logger:
    """Creates and confiurates a logger with own default settings."""
    logger = logging.getLogger(name)
    if not logger.hasHandlers():  # Avoids multiple handlers
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)  # Global log level
    return logger
