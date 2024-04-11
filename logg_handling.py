import logging
import sys
import ssh_to_dict
import get_message_type
def log(file):
    logger = logging.basicConfig(filename='log.log',encoding='utf-8', level=logging.DEBUG, filemode='w')
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setLevel(logging.INFO)
    handler.setLevel(logging.WARNING)
    handler_error = logging.StreamHandler(stream=sys.stderr)
    handler_error.setLevel(logging.ERROR)
    handler_error.setLevel(logging.CRITICAL)
    # logger.addHandler(handler)
    # logger.addHandler(handler_error)
    logging.getLogger().addHandler(handler)
    with open(file, 'r') as f:
        for f in f:
            dict_of_log = ssh_to_dict.ssh_to_dict(f)
            messege=get_message_type.get_messege_type(dict_of_log)
            if(messege == 'failed_login'):
                logging.warning(messege)
            elif(messege == 'success_login'):
                logging.info(messege)
            elif(messege == 'disconnect'):
                logging.error(messege)
            elif(messege == 'failed password'):
                logging.error(messege)
            elif(messege == 'invalid user'):
                logging.error(messege)
            elif(messege == 'break in attempt'):
                logging.critical(messege)
            logging.debug(sys.getsizeof(f))
    logging.shutdown()
if __name__ == "__main__":
    log(sys.argv[1])