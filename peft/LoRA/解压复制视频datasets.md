# 解压复制音频文件
1. 创建指定目录
   - mkdir -p /home/sigan/datasets/common_voice_27_fr
   - mkdir -p /home/sigan/datasets/common_voice_27_ge
   - mkdir -p /home/sigan/datasets/common_voice_27_nork
2. 进入指定目录
   - cd /home/sigan/datasets/common_voice_27_zh
3. 执行解压命令
   - tar -xzf '/sigan/ai-ml/datasets/common-voice-27/nork/common-voice-scripted-speech-27-0-norweg-8db502ef.tar.gz' --checkpoint=10000