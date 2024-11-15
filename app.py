from src.logger import logging  # Import our custom logger

def main():
    try:
        logging.info("Starting the main function")
        
        # Simulate some application steps
        logging.info("Step 1: Initializing application")
        x = 5
        y = 10
        
        logging.info(f"Step 2: Performing calculation with values x={x} and y={y}")
        result = x + y
        
        logging.info(f"Step 3: Calculation complete. Result: {result}")
        
        # Simulate a warning condition
        if result > 10:
            logging.warning(f"Result {result} is greater than threshold (10)")
            
    except Exception as e:
        logging.error("An error occurred in main function", exc_info=True)
        raise e

if __name__ == "__main__":
    logging.info("="*50)  # This will create a line of = for visual separation
    logging.info("Application execution has started")
    logging.info("="*50)
    
    try:
        main()
        logging.info("Application completed successfully")
    except Exception as e:
        logging.error("Application failed", exc_info=True)
    finally:
        logging.info("="*50)
        logging.info("Application execution has ended")
        logging.info("="*50)