import os
import time
import logging
from datetime import datetime

from celery import Celery
from celery.exceptions import Ignore

from app.models.domain.text_classifier import predict

celery = Celery(
    __name__,
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379"),
)


@celery.task(name="create_task", bind=True)
def create_celery_task(self, text: str) -> str:
    task_ts = datetime.utcnow().timestamp()
    self.update_state(state="PROGRESS", meta={"result": None, "created_at": task_ts})
    try:
        logging.info(f"Task [{self}] start prediction")
        # TODO: call model & make prediction
        # time.sleep(10)
        prediction = predict(text)
        logging.info(f"Task [{self}] predicted ok -> [{prediction}]")
    except Exception as e:
        logging.error(e)
        self.update_state(
            state="FAILED",
            meta={
                "result": None,
                "created_at": task_ts,
                "error": str(e),
            },
        )
        raise Ignore()

    # time.sleep(10)
    self.update_state(
        state="SUCCESS", meta={"result": prediction, "created_at": task_ts}
    )
    raise Ignore()
    # return f"{text}: Test-Category"
