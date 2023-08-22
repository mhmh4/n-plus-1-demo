const form1 = document.getElementById("form1");
const form2 = document.getElementById("form2");

const loadingIndicator = document.getElementById("loading-indicator");
const results = document.getElementById("results");

form1.addEventListener("submit", async (e) => {
  e.preventDefault();
  results.innerText = "";
  loadingIndicator.innerHTML = "fetching data...";

  const start = Date.now();
  const response = await fetch("http://localhost:5000/get-data");
  const timeTaken = Date.now() - start;
  loadingIndicator.innerHTML = timeTaken + " ms";

  let data = await response.json();
  results.innerText = data;
});

form2.addEventListener("submit", async (e) => {
  e.preventDefault();
  results.innerText = "";
  loadingIndicator.innerHTML = "fetching data...";

  const start = Date.now();
  const response = await fetch("http://localhost:5000/get-data-2");
  const timeTaken = Date.now() - start;
  loadingIndicator.innerHTML = timeTaken + " ms";

  let data = await response.json();
  results.innerText = data;
});
