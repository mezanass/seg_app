$("#image-selector").change(function () {
    let reader = new FileReader();
    reader.onload = function () {
        let dataURL = reader.result;
        $("#selected-image").attr("src", dataURL);
        $("#prediction-list").empty();
    }
    let file = $("#image-selector").prop("files")[0];
    reader.readAsDataURL(file);
}); 

let model;
(async function () {
    model = await tf.loadModel("http://localhost:8181/models/weights_sigmoid_mse_loss_js/model.json");
    $(".progress-bar").hide();
})();

$("#predict-button").click(async function(){
	let image = $("#selected-image").get(0);
	let tensor = tf.fromPixels(image)
	    .resizeNearestNeighbor([256, 256])
	    .toFloat()
	    .div(255.0)
	    .expandDims();

	$(".progress-bar").show();
	let predictions = await model.predict(tensor).as3D(256, 256, 3);
	let buffer =predictions.buffer();

	let c = document.getElementById("predicted-mask-");
	let ctx = c.getContext("2d");
	let imgData = ctx.createImageData(256, 256);
	var i, j;
	

	for (j = 0; j <256; j++){
		for (i = 0; i <256; i++) {
			index =(i + j * imgData.width) * 4;
		    imgData.data[index+0] =buffer.get(j, i, 0)*255.0;
		    imgData.data[index+1] =buffer.get(j, i, 1)*255.0;
		    imgData.data[index+2] =buffer.get(j, i, 2)*255.0;
		    imgData.data[index+3] =255;
		}	
	} 

	$(".progress-bar").hide();
	ctx.putImageData(imgData, 0, 0);

	console.log(buffer);
	console.log(imgData.data);
});