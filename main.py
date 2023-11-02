from src import *
import asyncio


async def main():
    para = Paratranz()
    para.init_dirs()
    await para.download_from_paratranz()

    project = LHSProject()
    project.init_dirs()
    project.process_csv_file_to_paratranz_json()
    project.process_paratranz_json_to_csv_file()


if __name__ == '__main__':
    asyncio.run(main())
