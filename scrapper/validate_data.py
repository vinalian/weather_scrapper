from serializers.database_filters import WeatherToAdd


class Data:
    @staticmethod
    async def validate(full_data: dict):
        hourly_data = full_data.get('hourly')
        if not hourly_data:
            raise ValueError('Invalid full data!')

        _time = hourly_data.get('time')
        _temperature = hourly_data.get('temperature_2m')
        _pressure = hourly_data.get('pressure_msl')
        _wind_speed = hourly_data.get('wind_speed_10m')
        _wind_direction = hourly_data.get('wind_direction_10m')

        _rain = hourly_data.get('rain')
        _snow = hourly_data.get('snowfall')

        if not all((_time, _temperature, _pressure, _wind_speed, _wind_direction, _rain, _snow)):
            raise ValueError('Invalid hourly data!')

        weather_obj_list = []

        for time, temperature, pressure, wind_speed, wind_direction, rain, snow in zip(
                _time, _temperature, _pressure, _wind_speed, _wind_direction, _rain, _snow
        ):
            if rain:
                precipitation_type = 'rain'
                precipitation_count = rain
            elif snow:
                precipitation_type = 'snow'
                precipitation_count = snow
            else:
                precipitation_type = 'clear'
                precipitation_count = 0.0

            weather_obj_list.append(WeatherToAdd(
                temperature=temperature,
                wind_speed=wind_speed,
                wind_direction=wind_direction,
                air_pressure=pressure,
                datetime=time,
                precipitation_type=precipitation_type,
                precipitation_count=precipitation_count
            ))

        return weather_obj_list


data_ = {'latitude': 55.6875, 'longitude': 37.375, 'generationtime_ms': 0.07605552673339844,
         'utc_offset_seconds': 10800, 'timezone': 'Europe/Moscow', 'timezone_abbreviation': 'MSK', 'elevation': 183.0,
         'hourly_units': {'time': 'iso8601', 'temperature_2m': '°C', 'precipitation': 'mm', 'rain': 'mm',
                          'showers': 'mm', 'snowfall': 'cm', 'snow_depth': 'm', 'pressure_msl': 'hPa',
                          'wind_speed_10m': 'km/h', 'wind_direction_10m': '°'}, 'hourly': {
        'time': ['2024-05-06T00:00', '2024-05-06T01:00', '2024-05-06T02:00', '2024-05-06T03:00', '2024-05-06T04:00',
                 '2024-05-06T05:00', '2024-05-06T06:00', '2024-05-06T07:00', '2024-05-06T08:00', '2024-05-06T09:00',
                 '2024-05-06T10:00', '2024-05-06T11:00', '2024-05-06T12:00', '2024-05-06T13:00', '2024-05-06T14:00',
                 '2024-05-06T15:00', '2024-05-06T16:00', '2024-05-06T17:00', '2024-05-06T18:00', '2024-05-06T19:00',
                 '2024-05-06T20:00', '2024-05-06T21:00', '2024-05-06T22:00', '2024-05-06T23:00'],
        'temperature_2m': [4.6, 4.0, 3.4, 2.9, 2.8, 2.8, 3.5, 4.8, 6.2, 6.8, 7.7, 8.3, 8.7, 8.9, 9.3, 9.7, 9.4, 9.5,
                           8.9, 8.3, 7.4, 6.6, 6.3, 6.1],
        'precipitation': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 0.0, 0.0, 0.0, 0.0],

        'rain': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0, 0.0, 0.0, 0.0],

        'snowfall': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                     0.0, 0.0, 0.0, 0.0],

        'pressure_msl': [1009.6, 1009.3, 1009.8, 1010.3, 1010.4, 1010.8, 1010.6, 1010.6, 1010.7, 1010.7, 1010.7, 1010.3,
                         1009.9, 1009.8, 1009.3, 1009.3, 1008.8, 1008.7, 1008.2, 1008.4, 1008.7, 1008.8, 1008.3,
                         1007.9],
        'wind_speed_10m': [2.8, 2.6, 2.6, 2.6, 2.1, 2.4, 2.3, 0.5, 1.5, 2.9, 3.3, 0.4, 1.5, 1.8, 0.5, 1.8, 4.1, 5.9,
                           10.0, 10.1, 9.6, 9.1, 8.8, 9.6],
        'wind_direction_10m': [320, 304, 286, 286, 301, 297, 288, 225, 14, 30, 77, 360, 284, 349, 225, 53, 75, 43, 52,
                               73, 77, 72, 71, 70]}}
if __name__ == '__main__':
    import asyncio

    asyncio.run(Data.validate(full_data=data_))
