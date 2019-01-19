<!DOCTYPE html>
<html lang="en">
	<head>
		<!-- CSS file -->
		<link rel="stylesheet" type="text/css" href="style.css">

		<!-- Bootstrap -->
		<meta charset="utf-8">
 	 	<meta name="viewport" content="width=device-width, initial-scale=1">
  		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
 	    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

		<style>
            table {
                border-collapse: collapse;
                border: 2px black solid;
                font: 12px sans-serif;
            }

            td {
                border: 1px black solid;
                padding: 5px;
            }
        </style>

	</head>
	<body>


		<h1>Toyota is Better than Honda</h1>
		<button type="button" onclick="loadDoc()">Refresh Location</button>

		<p>Surrounding Vehicles <span id="demo"></span></p>

		<!-- <script src="https://d3js.org/d3.v5.js"></script> -->
        <script src="https://d3js.org/d3.v5.js"></script>

		<script type="text/javascript"charset="utf-8">
		
			function loadDoc() {
			    var xhttp = new XMLHttpRequest();
			    xhttp.onreadystatechange = function() {
			    	/*	Holds the status of the XMLHttpRequest.
					0: request not initialized 
					1: server connection established
					2: request received 
					3: processing request 
					4: request finished and response is ready
					*/
			    	if (this.readyState == 4) {
			    		if (this.status == 200) {
				    		document.getElementById("demo").innerHTML = this.responseText;
				    	}
				    	else {
				    		alert(this.status + " error");
				    	}
			    	}
			    	// else {
			    		
			    	// 	alert("fail");
			    	// }
			    };
			    xhttp.open("GET", "getuser.php?q=", true);
			    xhttp.send();
			}

			var refreshId = setInterval(function() {
				loadDoc();
		        }, 9000);

			// alert("before d3");
			// d3.text("test.csv", function(data) {
   //              var parsedCSV = d3.csv.parseRows(data);
   //              alert("success");

   //              var container = d3.select("body")
   //                  .append("table")

   //                  .selectAll("tr")
   //                      .data(parsedCSV).enter()
   //                      .append("tr")

   //                  .selectAll("td")
   //                      .data(function(d) { return d; }).enter()
   //                      .append("td")
   //                      .text(function(d) { return d; });
   //          });


			// function refresh() {
			//     // make Ajax call here, inside the callback call:
			//     loadDoc();
			//     //alert("refresh");

			//     setTimeout(refresh, 10);

			    
			//     // ...
			// }

			// // initial call, or just call refresh directly
			//setTimeout(refresh, 10);

		</script>


	</body>

</html>

