from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
ROOT = Path(__file__).parent.parent
RAW_FILES_DIR = ROOT / "StreamingAssets"
DIR_PARATRANZ = ROOT / "paratranz-download"
DIR_TEMP_ROOT = ROOT / "temp"
PRE_PARATRANZ_RESULTS_DIR = ROOT / "pre-paratranz-results"
POST_PARATRANZ_RESULTS_DIR = ROOT / "post-paratranz-results"

PARATRANZ_TOKEN = os.getenv("PARATRANZ_TOKEN") or ""  # 必填，在个人设置里
PARATRANZ_BASE_URL = "https://paratranz.cn/api"
PARATRANZ_HEADERS = {"Authorization": PARATRANZ_TOKEN}
PARATRANZ_PROJECT_ID = 8602  # DOL 项目 ID


__all__ = [
    "ROOT",
    "RAW_FILES_DIR",
    "DIR_PARATRANZ",
    "PRE_PARATRANZ_RESULTS_DIR",
    "POST_PARATRANZ_RESULTS_DIR",
    "DIR_TEMP_ROOT",

    "PARATRANZ_BASE_URL",
    "PARATRANZ_HEADERS",
    "PARATRANZ_PROJECT_ID",
]