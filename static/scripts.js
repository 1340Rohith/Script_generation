function toggleSidebar() {
  const sidebar = document.querySelector('.sidebar-content');
  const container = document.querySelector('.container');
  if(container.classList.contains('active')){
    sidebar.classList.remove('active');
    container.classList.remove('active');
  } else {
    container.classList.toggle('active');
    sidebar.classList.toggle('active');
  }
}
function startApp() {
  const entry1 = document.querySelector('.entry_1');
  const entry2 = document.querySelector('.entry_2');
  entry1.classList.toggle('close');
  entry2.classList.toggle('close');
}

function handleSubmit() {
  const btn = document.getElementById("generateButton");
  document.getElementById("filmTitleLabel").innerHTML = "Enter your Corrections";
  if (btn) btn.style.display = "none";
}

function handleAccept() {
  // Handle the accept button click
  console.log("Accept button clicked");
  // You can add your logic here, like sending a request to the server
}
function handleReject() {
  // Handle the reject button click
  console.log("Reject button clicked");
  // You can add your logic here, like sending a request to the server
}
