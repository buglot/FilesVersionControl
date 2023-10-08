import threading
import dectect
if __name__ == "__main__":
    print("Sever Manger")
    folder_path = "ftp-data"  # ระบุโฟลเดอร์ที่คุณต้องการตรวจสอบ

    # สร้าง Thread สำหรับการตรวจสอบโฟลเดอร์
    monitor_thread = threading.Thread(target=dectect.monitor_folder, args=(folder_path,))
    monitor_thread.start()

    # รอให้ Thread ทำงานอยู่
    monitor_thread.join()