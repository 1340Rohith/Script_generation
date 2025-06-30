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
function openSettings(){
  const body = document.querySelector('body');
  body.classList.toggle('fade-out');
  setTimeout(() => {
    window.location.href = 'settings.html';
  }, 5000); // Match the duration of the fade-out transition
}
function openHomePage() {
  const body = document.querySelector('body');
  const entry1 = document.querySelector('.entry_1');
  const entry2 = document.querySelector('.entry_2');

  // Start the transition
  body.classList.add('fade-out');
  if (entry1) entry1.classList.add('close');
  if (entry2) entry2.classList.add('close');

  // Wait long enough for all transitions to complete
  setTimeout(() => {
    window.location.href = '/';
  }, 500); // Match the longest transition duration (1s for entry_1/2 + fade-out)
}
