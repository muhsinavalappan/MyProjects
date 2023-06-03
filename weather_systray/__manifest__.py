{
    'name': 'Weather',
    'version': '16.0.1.0.0',
    'summary': 'Weather Systray Icon',
    'installable': True,
    'depends': ['base', 'sale', 'web'],
    'data': [
        'views/res_config_settings.xml'
    ],
    'assets': {
        'web.assets_backend': {
            'weather_systray/static/src/css/weather.scss',
            'weather_systray/static/src/xml/weather_icon.xml',
            'weather_systray/static/src/xml/weather_template.xml',
            'weather_systray/static/src/js/weather_icon.js',

        },
        'web.assets_qweb': {

        },
    },

}
