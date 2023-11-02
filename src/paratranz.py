from zipfile import ZipFile, BadZipfile
import asyncio

import os
import contextlib
import httpx

from .consts import *
from .log import logger


class Paratranz:
    """下载汉化包相关"""
    def __init__(self):
        self._project_id = PARATRANZ_PROJECT_ID

    def init_dirs(self):
        os.makedirs(DIR_TEMP_ROOT, exist_ok=True)
        os.makedirs(DIR_PARATRANZ, exist_ok=True)

    async def download_from_paratranz(self) -> bool:
        """从 paratranz 下载汉化包"""
        os.makedirs(DIR_PARATRANZ, exist_ok=True)
        with contextlib.suppress(httpx.TimeoutException):
            await self.trigger_export()

        async with httpx.AsyncClient() as client:
            flag = False
            for _ in range(3):
                try:
                    await self.download_export(client)
                    await self.unzip_export()
                except (httpx.ConnectError, httpx.TimeoutException, BadZipfile) as e:
                    continue
                else:
                    flag = True
                    break
            if not flag:
                logger.error(f"***** 无法正常下载 Paratranz 汉化包！请检查网络连接情况，以及是否填写了正确的 TOKEN！\n")
                return False
            return True

    async def trigger_export(self):
        """触发导出"""
        logger.info(f"===== 开始导出汉化文件 ...")
        url = f"{PARATRANZ_BASE_URL}/projects/{self._project_id}/artifacts"
        httpx.post(url, headers=PARATRANZ_HEADERS)
        logger.info(f"##### 汉化文件已导出 !\n")

    async def download_export(self, client: httpx.AsyncClient):
        """下载文件"""
        logger.info(f"===== 开始下载汉化文件 ...")
        url = f"{PARATRANZ_BASE_URL}/projects/{self._project_id}/artifacts/download"
        headers = PARATRANZ_HEADERS
        content = (await client.get(url, headers=headers, follow_redirects=True)).content
        with open(DIR_TEMP_ROOT / f"paratranz_export.zip", "wb") as fp:
            fp.write(content)
        logger.info(f"##### 汉化文件已下载 !\n")

    async def unzip_export(self):
        """解压"""
        logger.info(f"===== 开始解压汉化文件 ...")
        with ZipFile(DIR_TEMP_ROOT / f"paratranz_export.zip") as zfp:
            zfp.extractall(DIR_PARATRANZ)
        logger.info(f"##### 汉化文件已解压 !\n")


__all__ = [
    "Paratranz"
]

