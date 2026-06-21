from pathlib import Path
import json
import logging
import sys

logger = logging.getLogger(__name__)
def create_json(json_result,output_path):
    output_path = Path(output_path)

    try:

        output_path.parent.mkdir(
        parents=True,
        exist_ok=True
        )
        with output_path.open(
            "w",
            encoding="utf-8")as f:
            json.dump(

                json_result,
                f,
                ensure_ascii=False,
                indent=4
            )
            logger.info("JSON saved as %s",output_path)
            return output_path
    except FileNotFoundError:
        logger.exception("创建JSON文件失败")
        raise
