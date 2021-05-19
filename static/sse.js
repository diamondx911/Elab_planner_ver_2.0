

var globmsg = null;
var source = new EventSource("/stream/");
source.onmessage = function(event) {
    var msg = JSON.parse(event.data);
    if (!globmsg) {


        $("#airspeed").text("Groundspeed: " + msg.airspeed);
 

    }
}

