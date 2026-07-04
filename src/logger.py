"""
Logger configuration module for the Ecommerce Sales Analysis Pipeline.
Sets up logging to both a file and the console.
"""

import logging
import os


class LoggerSetup:
    """Configures and initializes application-wide logging."""

    @staticmethod
    def setup_logger():
        """Initialize root logger with file and console handlers."""

        # This file lives at: Ecommerce_project/src/logger.py
        # One directory up from src/ gives the project root.
        current_file_path = os.path.abspath(__file__)
        root_path = os.path.dirname(os.path.dirname(current_file_path))

        logs_dir = os.path.join(root_path, "logs")
        os.makedirs(logs_dir, exist_ok=True)
        log_file_path = os.path.join(logs_dir, "Ecommerce.log")

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        # Prevent duplicate handlers on re-runs
        if root_logger.hasHandlers():
            root_logger.handlers.clear()

        # File handler
        file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
        file_formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(file_formatter)
        root_logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter("%(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        root_logger.addHandler(console_handler)

        logging.info(f"Logger initialized successfully at: {log_file_path}")
        return root_path