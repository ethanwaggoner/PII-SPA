<script setup>

</script>

<template>
  <nav class="nav-bar">
    <div class="nav-left">
      <router-link to="/overview">
        <button class="nav-button">Overview</button>
      </router-link>
      <button class="nav-button">View Data</button>
      <router-link to="/groups">
        <button class="nav-button">Manage Groups</button>
      </router-link>
      <button class="nav-button">Manage Scans</button>
      <button class="nav-button">Permissions</button>
    </div>
  </nav>
</template>

<style scoped>
.nav-bar {
  height: 80vh;
  display: flex;
  flex-direction: column;
  padding: 20px;
  background: linear-gradient(180deg, #10142c, #252c48);
  color: white;
  font-family: 'Roboto', sans-serif;
  border: 3px solid #5A6D7C; /* Metallic border */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C, 0 0 8px #5A6D7C, 0 0 12px #5A6D7C; /* Metallic glow */
}

.nav-left {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.nav-button {
  background: none;
  border: 2px solid #5A6D7C; /* Metallic border for the button */
  border-radius: 5px; /* Rounded corners for the button */
  color: white;
  cursor: pointer;
  font-size: 24px;
  padding: 10px 20px;
  transition: background-color 0.3s ease, color 0.3s ease, border 0.3s ease; /* Transition for color and border */
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C; /* New: Box-shadow for the button */
  width: 100%; /* New: Make the button fill its container */
}

.nav-button:hover {
  background-color: rgba(90, 109, 124, 0.1); /* Button hover effect */
  color: #5A6D7C; /* Button text color changes on hover */
  border-color: white; /* Button border color changes on hover */
  box-shadow: 0 0 5px #5A6D7C, 0 0 15px #5A6D7C, 0 0 25px #5A6D7C, 0 0 35px #5A6D7C; /* New: Increase box-shadow on hover */
}
</style>


