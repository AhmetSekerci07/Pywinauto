#before the run need to create memory_usage_log.txt
import psutil
def get_free_ram():
    """Get the amount of free RAM in megabytes."""
    return psutil.virtual_memory().available / (1024 ** 2)

def get_process_memory_usage(process_name):
    """Get the memory usage of a specific process in megabytes."""
    for process in psutil.process_iter(["name", "memory_info"]):
        if process.info["name"] == process_name:
            return process.info["memory_info"].rss / (1024 ** 2)
    return None

process_name = "asekerci.exe"  # Replace with the name of the process you want to monitor
file_path = "memory_usage_log.txt"

memory_usage = get_process_memory_usage(process_name)
free_ram_mb = get_free_ram()

get_free_ram = lambda: psutil.virtual_memory().available / (1024 ** 2)

get_process_memory_usage = lambda process_name: next(
    (
        process.info["memory_info"].rss / (1024 ** 2)
        for process in psutil.process_iter(["name", "memory_info"])
        if process.info["name"] == process_name
    ),
    None,
)


# How I run in main

def get_free_ram():
    """Get the amount of free RAM in megabytes."""
    return psutil.virtual_memory().available / (1024 ** 2)

def get_process_memory_usage(process_name):
    """Get the memory usage of a specific process in megabytes."""
    for process in psutil.process_iter(["name", "memory_info"]):
        if process.info["name"] == process_name:
            return process.info["memory_info"].rss / (1024 ** 2)
    return None

process_name = "Canfield Capture.exe"  # Replace with the name of the process you want to monitor
file_path = "memory_usage_log.txt"

memory_usage = get_process_memory_usage(process_name)
free_ram_mb = get_free_ram()

get_free_ram = lambda: psutil.virtual_memory().available / (1024 ** 2)

get_process_memory_usage = lambda process_name: next(
    (
        process.info["memory_info"].rss / (1024 ** 2)
        for process in psutil.process_iter(["name", "memory_info"])
        if process.info["name"] == process_name
    ),
    None,
)



def test_start():


    free_ram_mb = get_free_ram()
    print(f"Free RAM: {free_ram_mb:.2f} MB")

    memory_usage = get_process_memory_usage(process_name)
    print(f"Memory usage of {process_name}: {memory_usage} MB")