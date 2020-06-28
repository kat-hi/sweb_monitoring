from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers import SchedulerAlreadyRunningError
from flask import Flask, jsonify
from . import monitoring

app = Flask(__name__)

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(monitoring.request_map, 'interval', seconds=5)

@app.route('/')
def hello_world():
    return jsonify({'Json sagt': 'Hallo I bims, der Json'})


@app.route('/start')
def start_monitoring():
    try:
        app.logger.info('Try scheduler start')
        scheduler.start()
    except SchedulerAlreadyRunningError:
        print('scheduler already running error')
        pass
    return jsonify({'Json sagt': 'scheduler started'})


@app.route('/stop')
def stop_monitoring():
    scheduler.shutdown()
    return jsonify({'Json sagt': 'scheduler stopped'})


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)