const loadingIndicator = document.getElementById("loading-indicator");
const form = document.getElementById("form1");
const results = document.getElementById("results");
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  loadingIndicator.innerHTML = "fetching data...";

  let start = Date.now();
  let response = await fetch("http://localhost:5000/get-data");
  let timeTaken = Date.now() - start;
  loadingIndicator.innerHTML = timeTaken + " ms";

  let data = await response.json();
  results.innerText = data;
});

const form2 = document.getElementById("form2");
form2.addEventListener("submit", async (e) => {
  e.preventDefault();
  loadingIndicator.innerHTML = "fetching data...";

  let start = Date.now();
  let response = await fetch("http://localhost:5000/get-data-2");
  let timeTaken = Date.now() - start;
  loadingIndicator.innerHTML = timeTaken + " ms";

  let data = await response.json();
  results.innerText = data;
});
