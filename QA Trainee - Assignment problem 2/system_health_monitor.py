import psutil
import logging

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Thresholds for alerting
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def check_system_health():
    try:
        # Get CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > CPU_THRESHOLD:
            logging.warning(f'High CPU usage detected: {cpu_usage}%')
            print(f'Warning: CPU usage is at {cpu_usage}%')

        # Get memory usage
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        if memory_usage > MEMORY_THRESHOLD:
            logging.warning(f'High memory usage detected: {memory_usage}%')
            print(f'Warning: Memory usage is at {memory_usage}%')

        # Get disk space usage
        disk_usage = psutil.disk_usage('/')
        if disk_usage.percent > DISK_THRESHOLD:
            logging.warning(f'High disk usage detected: {disk_usage.percent}%')
            print(f'Warning: Disk space usage is at {disk_usage.percent}%')

        # Get running processes
        processes = len(psutil.pids())
        logging.info(f'Number of running processes: {processes}')
        print(f'Number of running processes: {processes}')

    except Exception as e:
        logging.error(f"Error in system health check: {e}")
        print(f"An error occurred: {e}")

check_system_health()
