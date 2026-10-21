import sys

def error_message_detail(error, error_detail: sys):
    # Hatanın traceback nesnesini alıyoruz
    _, _, exc_tb = error_detail.exc_info()
    
    # Hatanın meydana geldiği dosya adını çekiyoruz
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Hatanın meydana geldiği satır numarasını çekiyoruz
    line_number = exc_tb.tb_lineno
    
    # Detaylı hata mesajını formatlıyoruz
    error_message = f"Hata: [{file_name}] dosyasında, [{line_number}]. satırda oluştu. Mesaj: [{str(error)}]"
    
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
