from moviepy import VideoFileClip

input_video = "/home/ccg/workspace/LMP-Website/static/lmp_videos/comparsion/stroller/ori-prompt/dmt.mp4"
output_video = input_video

# 读取视频
clip = VideoFileClip(input_video)

# 可在此处处理视频（如裁剪、调整速度、添加文字等）
# processed_clip = clip.subclip(10, 20)  # 截取 10-20 秒
# processed_clip = clip.fx(vfx.resize, width=640)  # 调整宽度

# 保存视频
clip.write_videofile(output_video, codec='libx264', audio_codec='aac')