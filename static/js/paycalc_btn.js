var $ = django.jQuery;

$(document).ready(function() {
    var myButton = '<button>Pay</button>';
    $(myButton).insertAfter($('id_order_goods-0-cargo_duties'));
});