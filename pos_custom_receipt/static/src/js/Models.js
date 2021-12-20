odoo.define('pos_custom_receipt.Models', function (require) {
"use strict";

var models = require('point_of_sale.models');


var _super_order = models.Order.prototype;
models.Order = models.Order.extend({
    export_for_printing: function(){
        var receipt = _super_order.export_for_printing.apply(this,arguments);
        receipt.sequence_number = this.sequence_number;
        var date    = new Date();
        receipt.date.LocaleStringdateStyle = date.toLocaleString('en-US', {day: "2-digit"})+" "+ date.toLocaleString('en-US', { month: "short"})+" "+date.toLocaleString('en-US', { year: "numeric"});
        receipt.date.LocaleStringtimeStyle = date.toLocaleString('en-US', { timeStyle: "short" ,hour12: true });
        return receipt;

    },


});


});

