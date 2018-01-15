var list = document.getElementById("list");
var found = false;

var rawFile = new XMLHttpRequest();
rawFile.open("GET", "https://nichodon.github.io/articles/list.txt", false);
rawFile.onreadystatechange = function () {
	"use strict";

	if (rawFile.readyState === 4) {
		if (rawFile.status === 200 || rawFile.status === 0) {
			var array = rawFile.responseText.split("\n");
			for (var i = 0; i < array.length; i++) {
				found = true;

				var sub = array[i].split(" - ");

				var block = document.createElement("div");
				block.classList.add("block");
				list.appendChild(block);

				var title = document.createElement("h2");
				title.innerHTML = sub[0];
				block.appendChild(title);

				var author = document.createElement("p");
				author.innerHTML = "by <a href=\"https://github.com/" + sub[2] + "\" target=\"_blank\">" + sub[2] + "</a> &ndash; " + sub[1];
				block.appendChild(author);

				var text = document.createElement("p");

				var rf2 = new XMLHttpRequest();
				rf2.open("GET", "https://nichodon.github.io/articles/" + sub[3] + "/article.txt", false);
				rf2.onreadystatechange = function () {
					if (rf2.readyState === 4) {
						if (rf2.status === 200 || rf2.status === 0) {
							text.innerHTML = rf2.responseText.split("\n")[0];
						}
					}
				};
				rf2.send(null);

				block.appendChild(text);

				var more = document.createElement("p");
				more.classList.add("more");
				more.innerHTML = "<a href=\"" + sub[3] + "\">Read More</a>";
				block.appendChild(more);
			}
		}
	}
};
rawFile.send(null);

function update(x) {
	"use strict";
	var children = document.getElementById("list").children;
	for (var i = 0; i < children.length; i++) {
		if (children[i].children[0].innerHTML.toUpperCase().includes(x.toUpperCase())) {
			children[i].style.display = "initial";
		} else {
			children[i].style.display = "none";
		}
	}
}

if (!found) {
	var block = document.createElement("div");
	block.classList.add("block");
	list.appendChild(block);
}

function check() {
	"use strict";
	update(document.getElementById("input").value);
}