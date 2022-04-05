var opts = {
    angle: 0, // The span of the gauge arc
    lineWidth: 0.2, // The line thickness
    radiusScale: 0.89, // Relative radius
    pointer: {
      length: 0.54, // // Relative to gauge radius
      strokeWidth: 0.053, // The thickness
      color: '#000000' // Fill color
    },
    limitMax: false,     // If false, max value increases automatically if value > maxValue
    limitMin: false,     // If true, the min value of the gauge will be fixed
    colorStart: '#6FADCF',   // Colors
    colorStop: '#8FC0DA',    // just experiment with them
    strokeColor: '#E0E0E0',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true,     // High resolution support
	staticLabels: {
	  font: "10px sans-serif",  // Specifies font
	  labels: [0,10,20,30,40,50,60,70,80,90,100],  // Print labels at these values
	  color: "#000000",  // Optional: Label text color
	  fractionDigits: 0 , // Optional: Numerical precision. 0=round off.
	},
    staticZones: [
        {strokeStyle: "#0000FF", min: 0, max: 20}, // Red from 100 to 60
        {strokeStyle: "#00FF00", min: 20, max: 40}, // Yellow
        {strokeStyle: "#FFDD00", min: 40, max: 60}, // Green
        {strokeStyle: "#FF6600", min: 60, max: 80}, // Yellow
        {strokeStyle: "#FF0000", min: 80, max: 100}  // Red
     ],
  };
