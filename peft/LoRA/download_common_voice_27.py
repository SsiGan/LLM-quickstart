from pathlib import Path
import os
import sys

from dotenv import load_dotenv
from datacollective import download_dataset, get_dataset_details


DATASET_ID = "cmu5ktqhe00pgmh07p1xamabd"
DOWNLOAD_ROOT = Path("/sigan/ai-ml/datasets/common-voice-27/german")
ENV_FILE = Path("/home/sigan/work/LLM-quickstart/.env")

DOWNLOAD_ROOT.mkdir(parents=True, exist_ok=True)

load_dotenv(ENV_FILE)

if not os.environ.get("MDC_API_KEY"):
    print(f"错误：没有在 {ENV_FILE} 中找到 MDC_API_KEY")
    print("请在 .env 中设置：MDC_API_KEY=你的新密钥")
    sys.exit(1)

print("=" * 60)
print("Mozilla Common Voice Scripted Speech 27.0")
print("Dataset ID：", DATASET_ID)
print("下载目录：", DOWNLOAD_ROOT)
print("API Key：已配置")
print("=" * 60)

try:
    details = get_dataset_details(DATASET_ID)
    print("数据集访问验证成功")
    print(details)
except Exception as exc:
    print("数据集信息验证失败：")
    print(type(exc).__name__, str(exc))
    sys.exit(1)

print("\n开始下载。网络中断后重新运行本脚本即可续传。\n")

result_path = download_dataset(
    dataset_id=DATASET_ID,
    download_directory=str(DOWNLOAD_ROOT),
    show_progress=True,
    overwrite_existing=False,
    extract=True,
    overwrite_extracted=False,
    enable_logging=True,
    max_download_attempts=10,
)

print("\n" + "=" * 60)
print("下载和解压完成")
print("结果目录：", result_path)
print("=" * 60)
