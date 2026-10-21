import logging
import os
from datetime import datetime

# 1. Her çalıştırmada o anın tarih ve saatiyle benzersiz bir log dosya adı üret (Örn: 10_21_2026_03_45_00.log)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Ana dizinde 'logs' adında bir klasör yolu belirle ve bu dosya adını içine bağla
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# 3. 'logs' klasörü yoksa otomatik olarak oluştur (exist_ok=True varsa hata vermez)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# 4. Tam dosya yolunu belirle
LOG_FILE_PATH = logs_path

# 5. Standart log formatını ayarla
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)