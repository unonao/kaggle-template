import datetime
import time
from datetime import timezone

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

COMPETITION = "child-mind-institute-detect-sleep-states"
result_ = api.competition_submissions(COMPETITION)[0]
latest_ref = str(result_)  # 最新のサブミット番号
print(result_.url)
submit_time = result_.date

status = ""

while status != "complete":
    list_of_submission = api.competition_submissions(COMPETITION)
    for result in list_of_submission:
        if str(result.ref) == latest_ref:
            break
    status = result.status

    now = datetime.datetime.now(timezone.utc).replace(tzinfo=None)
    elapsed_time = int((now - submit_time).seconds / 60) + 1
    if status == "complete":
        print("\r", f"run-time: {elapsed_time} min, LB: {result.publicScore}")
    else:
        print("\r", f"elapsed time: {elapsed_time} min", end="")
        time.sleep(60)
