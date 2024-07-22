const input1 = document.getElementById("input1");
const input2 = document.getElementById("input2");
const submitBtn = document.getElementById("submitBtn");
const resultDiv = document.getElementById("result");

function toggleButton() {
  submitBtn.disabled = !(input1.value.trim() && input2.value.trim());
}

async function fetchAccountInfo() {
  const gameName = input1.value.trim();
  const tagLine = input2.value.trim();

  try {
    const response = await fetch(`/api/get-account-info?game_name=${encodeURIComponent(gameName)}&tag_line=${encodeURIComponent(tagLine)}`);
    if (!response.ok) throw new Error('Network response was not ok');
    const data = await response.json();
    resultDiv.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    resultDiv.textContent = `Error: ${error.message}`;
  }
}

submitBtn.addEventListener("click", fetchAccountInfo);

input1.addEventListener("input", toggleButton);
input2.addEventListener("input", toggleButton);
