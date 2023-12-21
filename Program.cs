using Emgu.CV;
using Emgu.CV.CvEnum;
using System;

class Program
{
    static void Main(string[] args)
    {
        using (VideoCapture capture = new VideoCapture(0)) // 0はデフォルトのカメラを指します
        {
            // 設定が適用されたかを確認
            double width = capture.Get(CapProp.FrameWidth);
            double height = capture.Get(CapProp.FrameHeight);
            double fps = capture.Get(CapProp.Fps);
            Console.WriteLine($"Width: {width}");
            Console.WriteLine($"Height: {height}");
            Console.WriteLine($"FPS: {fps}");

            // 解像度の設定
            capture.Set(CapProp.FrameWidth, 1920); // 幅
            capture.Set(CapProp.FrameHeight, 1080); // 高さ
            capture.Set(CapProp.Fps, 60);
            width = capture.Get(CapProp.FrameWidth);
            height = capture.Get(CapProp.FrameHeight);
            fps = capture.Get(CapProp.Fps);
            Console.WriteLine($"Width: {width}");
            Console.WriteLine($"Height: {height}");
            Console.WriteLine($"FPS: {fps}");
            return;
            // フレームの処理
            using (Mat frame = new Mat())
            {
                while (true)
                {
                    capture.Read(frame); // フレームを取得
                    if (!frame.IsEmpty)
                    {
                        // ここでフレームを表示したり、他の処理を行う
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }
    }
}
