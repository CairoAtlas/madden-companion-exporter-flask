import json
import logging.config

import boto3
from flask import Flask, request, make_response

application = Flask(__name__)

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
S3_CLIENT = boto3.client('s3')
S3_BUCKET = 'madden-companion-exporter-flask-test'


@application.route('/madden/export/xbox/<cfm_id>/leagueteams', methods=['POST'])
def export_league_info(cfm_id):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


@application.route('/madden/export/xbox/<cfm_id>/standings', methods=['POST'])
def export_standings(cfm_id):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


@application.route('/madden/export/xbox/<cfm_id>/week/reg/<week>/punting', methods=['POST'])
def export_punting(cfm_id, week):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(f'Madden League Week: {week}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


@application.route('/madden/export/xbox/<cfm_id>/week/reg/<week>/passing', methods=['POST'])
def export_passing(cfm_id, week):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(f'Madden League Week: {week}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


@application.route('/madden/export/xbox/<cfm_id>/week/reg/<week>/rushing', methods=['POST'])
def export_rushing(cfm_id, week):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(f'Madden League Week: {week}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


@application.route('/madden/export/xbox/<cfm_id>/week/reg/<week>/receiving', methods=['POST'])
def export_receiving(cfm_id, week):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(f'Madden League Week: {week}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


@application.route('/madden/export/xbox/<cfm_id>/week/reg/<week>/kicking', methods=['POST'])
def export_kicking(cfm_id, week):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(f'Madden League Week: {week}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


@application.route('/madden/export/xbox/<cfm_id>/week/reg/<week>/defense', methods=['POST'])
def export_defense(cfm_id, week):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(f'Madden League Week: {week}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


@application.route('/madden/export/xbox/<cfm_id>/week/reg/<week>/schedules', methods=['POST'])
def export_schedules(cfm_id, week):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(f'Madden League Week: {week}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


@application.route('/madden/export/xbox/<cfm_id>/week/reg/<week>/teamstats', methods=['POST'])
def export_teamstats(cfm_id, week):
    req_data = request.get_json()
    print(f'Madden League ID: {cfm_id}')
    print(f'Madden League Week: {week}')
    print(req_data)
    # S3_CLIENT.put_object(
    #     Bucket=S3_BUCKET,
    #     Key='Maddendata',
    #     Body=json.dumps(req_data)
    # )
    return make_response(json.dumps({'message': 'complete'}), 200)


if __name__ == '__main__':
    application.run()
