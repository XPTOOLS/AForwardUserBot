from bot import Bot
from web_server import start_server_in_background
from config import Config
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    # Start the web server in background for Render.com port binding
    logger.info(f"Starting web server on port {Config.PORT}")
    start_server_in_background(Config.PORT)
    
    # Start the Telegram bot
    logger.info("Starting Telegram bot...")
    app = Bot()
    app.run()

if __name__ == "__main__":
    main()
