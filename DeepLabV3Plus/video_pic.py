import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from PIL import Image

 
def Video2Pic():
    videoPath = "video.MP4"  # 读取视频路径
    imgPath = "image_for_seg/"  # 保存图片路径
 
    cap = cv2.VideoCapture(videoPath)
    # fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
    # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
    suc = cap.isOpened()  # 是否成功打开
    frame_count = 0
    while suc:
        frame_count += 1
        suc, frame = cap.read()
        cv2.imwrite(imgPath + str(frame_count).zfill(4)+".png", frame)
        cv2.waitKey(1)
    cap.release()
    print("视频转图片结束！")


def Pic2Video():
    imgPath = "test_results/"  # 读取图片路径
    videoPath = "video_seg.MP4"  # 保存视频路径
 
    images = os.listdir(imgPath)
    images = sorted(images, key= lambda x: int(x[0:4]))
    fps = 30  # 每秒30帧数
 
    # VideoWriter_fourcc为视频编解码器 ('I', '4', '2', '0') —>(.avi) 、('P', 'I', 'M', 'I')—>(.avi)、('X', 'V', 'I', 'D')—>(.avi)、('T', 'H', 'E', 'O')—>.ogv、('F', 'L', 'V', '1')—>.flv、('m', 'p', '4', 'v')—>.mp4
    fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
 
    image = Image.open(imgPath + images[0])
    videoWriter = cv2.VideoWriter(videoPath, fourcc, fps, image.size)
    for im_name in range(len(images)):
        frame = cv2.imread(imgPath + images[im_name])  # 这里的路径只能是英文路径
        # frame = cv2.imdecode(np.fromfile((imgPath + images[im_name]), dtype=np.uint8), 1)  # 此句话的路径可以为中文路径
        videoWriter.write(frame)
    print("图片转视频结束！")
    videoWriter.release()
    cv2.destroyAllWindows()
 
 
if __name__ == '__main__':
    Pic2Video()
    # Video2Pic()
