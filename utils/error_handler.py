from .logger import logger

def handle_error(error, context=None):
    if context:
        logger.error(f"An error occurred in {context}: {str(error)}")
    else:
        logger.error(f"An error occurred: {str(error)}")

    # You can add more sophisticated error handling here,
    # such as sending error reports, notifying administrators, etc.