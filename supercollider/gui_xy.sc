s.boot

s.doWhenBooted({

	// a sine oscillator node with one parameter
	var x = {|freq=100| Out.ar(0, SinOsc.ar(freq))}.play;

	// create a window with width and position
    var w = Window("Slider", Rect(128, 64, 800, 480));

	// add a slider
	var slider = Slider(w, Rect(400,200,60,200));

	// the callback function on slider move
	slider.action_({x.set(\freq, slider.value * 10000)});

	// "same effect as setting -visible to true"
	w.front;

});

//defer()

Slide