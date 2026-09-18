import psutil
import platform
from time import time

class SystemInfoManager:
    def get_system_info(self):
        return {
            "hostname": platform.node(),
            "system_uptime_seconds": int(time() - psutil.boot_time()),
            "cpu_usage_percent": psutil.cpu_percent(interval=None, percpu=False),
            "cpu_frequency": psutil.cpu_freq().current,
            "cpu_core_count": psutil.cpu_count(logical=True),
            "ram_usage_percent": psutil.virtual_memory().percent,
            "disk_usage_percent": psutil.disk_usage('/').percent,
            "temperatures_celsius": psutil.sensors_temperatures()
        }