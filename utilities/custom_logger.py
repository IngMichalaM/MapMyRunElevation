import logging
import time


def custom_logger(logging_level=logging.DEBUG):
    time_today = time.strftime("%Y_%m_%d")
    newname = 'mapmyrun_logger_' + time_today + '.txt'
    logger = logging.getLogger('mapmyrun_log')  # name of the logger , not the file

    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(filename)-20s:line %(lineno)-4d - %(message)s',
                        level=logging_level,
                        filename=newname,
                        datefmt='%d.%m.%Y %H:%M:%S')
        # format='%(asctime)s %(levelname)-8s [%(filename)-20s:%(lineno)d] %(message)s',
    return logger


if __name__ == '__main__':
    log = custom_logger(logging_level=logging.INFO)
    log.info(f'some log info .')
    print('done')
