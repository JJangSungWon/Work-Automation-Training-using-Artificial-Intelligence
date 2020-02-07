import os, shutil, glob

# os
print(os.environ)

#shutil - 파일 복사 모듈
shutil.copy("인공지능캠프.txt", "인공지능 캠프2기.txt")

#glob - 디렉토리 내 파일을 읽어 리스트로 리턴
print(glob.glob("디렉토리 경로"))