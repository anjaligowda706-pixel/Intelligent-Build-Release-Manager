import csv
from datetime import datetime

def log_build(build_time, prediction):
    status = "STABLE" if prediction == 1 else "UNSTABLE"
    release = "APPROVED" if prediction == 1 else "BLOCKED"

    with open("build_monitor_log.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow([
                "Timestamp",
                "Build_Time",
                "Build_Status",
                "Release_Decision"
            ])

        writer.writerow([
            datetime.now(),
            build_time,
            status,
            release
        ])

    print("build_monitor_log.csv created/updated successfully ✅")
