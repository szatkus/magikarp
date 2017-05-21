var imported = document.createElement("script");
imported.src = "/static/js/hash.js";
document.body.appendChild(imported);


function getInputForm(obj){
	
	var fields = obj.fields;
	
	var htmlForm = document.createElement("form");
	{
		htmlForm.setAttribute("action",obj.actionPage);
		htmlForm.setAttribute("method","post");
		htmlForm.id=obj.id;
		htmlForm.setAttribute("onsubmit", "hashPasswords(this);");
		
		/* Tworzę tabele */
		var htmlTable = document.createElement("table");
		
		/* Tworzę wiersze wejściowe */
		for (row in fields) {
			
			var htmlRow = document.createElement("tr");
			{
				var htmlPrompt = document.createElement("td");
				{
					htmlRow.appendChild(htmlPrompt);
					htmlPrompt.innerHTML=fields[row].prompt;
				}
				
				var htmlInputCell = document.createElement("td");
				{
					var htmlInput = document.createElement("input");
					htmlInput.id=row;
					htmlInput.name=row;
					htmlInput.type = fields[row].isPassword ? "password" : "text";
					htmlInputCell.appendChild(htmlInput);
				}
				htmlRow.appendChild(htmlInputCell);
			}
			htmlTable.appendChild(htmlRow)
		} 
		
		/* Tworzę wiersz z przyciskiem send */
		var htmlSendRow = document.createElement("tr");
		{
			var htmlSendCell = document.createElement("td");
			{
				htmlSendCell.setAttribute("colspan","2");
				var htmlSend = document.createElement("button");
				{
					htmlSend.type="send";
					htmlSend.innerHTML = typeof obj.sendText === "undefined" ? "Send" : obj.sendText;
					htmlSendCell.appendChild(htmlSend);
				}
			}
			htmlSendRow.appendChild(htmlSendCell);
		}
		htmlTable.appendChild(htmlSendRow);
	}
	htmlForm.appendChild(htmlTable);
	
	
	return htmlForm;
};

function hashPasswords(form){
	var passInputs = document.querySelectorAll('[type=password]');
	for (var i = 0 ; i<passInputs.length ; i++){
		var input = passInputs[i];
		if (form.contains(input)){
			input.value=md5(input.value);
			console.log(input.value);
		}
	}
};
