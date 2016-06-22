'use strict';

class Shortener 
{
    constructor() {
        this.api = new Adapter();
        this.button = document.querySelector('button#submit');
        this.long_input = document.querySelector('input#long_url');
        this.short_input = document.querySelector('input#short_url');
        this.link = document.querySelector('a#link');
        this.button.addEventListener('click', this.button_click.bind(this), false);
    }

    get long_url() {
        return this.long_input.value;
    }

    get short_url() {
        return this.short_input.value;
    }

    button_click() {
        this.api.create(this.long_url, this.short_url).then((shortener) => {
            this.link.href = 'http://seal.tw/' + shortener.short_url;
            this.link.text = 'seal.tw/' + shortener.short_url;
        }).catch((error) => {
            console.log(error);
        });
    }
}

const shotener = new Shortener();
