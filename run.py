import logging
import logging.config

from mmgmt_server import app

if __name__ == '__main__':
    logging.config.fileConfig('logger.conf')
    app.run('0.0.0.0', 5000, True)
    
