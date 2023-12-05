import cv2


def main():
    # テストする解像度
    resolutions = [(160, 120), (320, 240), (640, 480), (800, 600), (1024, 768)]
    # テストするFPSの値
    fps_values = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    # システムに接続されているカメラデバイスを探す
    max_devices = 10
    devices = []
    for i in range(max_devices):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            devices.append(i)
        cap.release()

    # 各デバイスに対してテストを実行
    for device in devices:
        print(f"Testing camera device: {device}")
        cap = cv2.VideoCapture(device)

        # 解像度のテスト
        for width, height in resolutions:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print(
                f"Requested: {width}x{height}, Actual: {actual_width}x{actual_height}")

        # FPSのテスト
        for fps in fps_values:
            cap.set(cv2.CAP_PROP_FPS, fps)
            actual_fps = cap.get(cv2.CAP_PROP_FPS)
            print(f"Requested FPS: {fps}, Actual FPS: {actual_fps}")
        cap.release()

    # もしカメラが見つからない場合
    if not devices:
        print("No camera devices found.")


if __name__ == '__main__':
    main()
