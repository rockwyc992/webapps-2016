'use strict';

class Adapter
{
    constructor() {
        this.server = 'http://seal.tw';
        this.format = '?format=json'
        this.url = this.server + '/api/v1/shortener/' + this.format;
    }

    create(long_url, short_url) {
        var data = new FormData();
        data.append('long_url', long_url);
        if (short_url) {
            data.append('short_url', short_url);
        }
        return this.send('POST', this.url, data);
    }

    send(method, url, data) {
        return new Promise((resolve, reject) => {
            var xhr = new XMLHttpRequest();
            xhr.open(method, url);
            window.xhr = xhr;
            xhr.onload = () => {
                if (xhr.status >= 200 && xhr.status < 300) {
                    resolve(JSON.parse(xhr.response));
                } else {
                    reject({
                        status: xhr.status,
                        statusText: xhr.statusText,
                        response: xhr.response,
                    });
                }
            };
            xhr.onerror = () => {
                reject({
                    status: xhr.status,
                    statusText: xhr.statusText
                });
            };
            xhr.send(data);
        });
    }
}
