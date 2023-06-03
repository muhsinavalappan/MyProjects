odoo.define('weather_systray.weather', function(require) {
    "use strict";
    var core = require('web.core');
    var QWeb = core.qweb;
    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');

    var ActionMenu = Widget.extend({
        template: 'weather_systray.myicon',
        events: {
            'click .my_icon': 'onclick_myicon',
        },
        /**
         *defining function
         **/
        onclick_myicon: async function() {
            if ($(".test_div").is(":visible")) {
                $('.test_div').hide();
            } else {
                $('.test_div').show();
                await rpc.query({
                    model: 'ir.config_parameter',
                    method: 'get_param',
                    args: ['OpenWeather.api_key', ],
                }).then(function(result) {
                    var api_key = result;
                    /**
                     *fetching weather data from open weather api
                     **/

                    var url = "https://api.openweathermap.org/data/2.5/weather?q=Calicut&appid=" + api_key
                    console.log(url)
                    fetch(url, {
                            "method": "GET",
                            "headers": {}

                        })
                        .then(response => {
                        console.log(response,'response')
                            return response.json();
                        })
                        /** taking required details from json response **/
                        .then((data) => {
                            console.log(data,'data')
                            var temperature = Math.floor(data.main.temp - 273) + "°C";
                            var main = data.weather[0].main;
                            var summary = data.weather[0].description;
                            var loc = data.name + "," + data.sys.country;
                            var icon = data.weather[0].icon;
                            var iconurl = "http://openweathermap.org/img/wn/" + icon + "@2x.png";
                            var dt = new Date();
                            var date = dt.toLocaleDateString();
                            var datetime = dt.toLocaleString();

                            $("#fa-icon").append(QWeb.render('weather_systray.my_systray_icon', {
                                'temp': temperature,
                                'summary': summary,
                                'loc': loc,
                                'icon': icon,
                                'iconurl': iconurl,
                                'date': date,
                                'datetime': datetime,
                                'main': main,
                            }));
                        })

                })
            }
        }


    });
    SystrayMenu.Items.push(ActionMenu);
    return ActionMenu;
});