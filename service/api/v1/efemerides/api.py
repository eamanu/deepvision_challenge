import holidays

from datetime import datetime, date
from flask import Blueprint, current_app, make_response
from flask_restful import Resource, reqparse


efemerides_api = Blueprint('api', __name__)


class Efemerides(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('day', help='Fecha format %Y-%m-%d', location='args',
                            type=lambda x: datetime.strptime(x,'%Y-%m-%d'),
                            required=False)

        parser.add_argument('month', help='Fecha mes %Y-%m', location='args',
                            type=lambda x: datetime.strptime(x,'%Y-%m'),
                            required=False)

        args = parser.parse_args()


        if args['day']:
            dia = holidays.AR()[date(args['day'].year, args['day'].month, args['day'].day)]
            k = datetime.strftime(args['day'], '%Y-%m-%d')
            response = make_response({k: dia}, 200)
            response.headers.set('Content-Type', 'application/json')
            return response


        if args['month']:
            efemerides = dict()
            dias = holidays.AR()[
                date(args['month'].year, args['month'].month,1):
                date(args['month'].year, args['month'].month +1, 1)
            ]
            efemerides['Mes'] = args['month'].month
            for d in dias:
                efemerides['Dia: %s' % str(d.day)] = holidays.AR()[d]


            response = make_response(efemerides, 200)
            response.headers.set('Content-Type', 'application/json')
            return response

        return {"INFO": "Sin parametros"}, 200
