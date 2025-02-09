import logging

class Log_Maker:  # Class name should follow PascalCase convention
    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename=".\\logs\\websitesaspx.log",
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True
        )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

