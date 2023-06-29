<script setup>

</script>

<template>
  <div>
    <nav class="nav-bar">
      <div class="nav-left">
        <table class="table table-inline">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Group Name</th>
              <th scope="col">Scheduled Run time</th>
              <th scope="col">Status</th>
            </tr>
          </thead>
          <tbody>
            <!-- Table rows will go here -->
          </tbody>
        </table>
      </div>
    </nav>
  </div>
</template>

<style scoped>
.nav-bar {
  height: 40vh;
  display: flex;
  flex-direction: column;
  padding: 20px;
  background: linear-gradient(180deg, #10142c, #252c48);
  color: white;
  font-family: 'Roboto', sans-serif;
  border: 3px solid #5A6D7C; /* Steel gray border */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C, 0 0 8px #5A6D7C, 0 0 12px #5A6D7C; /* Steel gray glow */
}

.table {
  color: white;
}

.table thead th {
  background: linear-gradient(180deg, #10142c, #252c48);
  border: 3px solid #5A6D7C; /* Steel gray border */
  border-radius: 5px; /* Rounded corners for the header cells */
  color: white;
  font-size: 18px;
  text-align: center;
  transition: background-color 0.3s ease, color 0.3s ease, border 0.3s ease; /* Transition for color and border */
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C, 0 0 8px #5A6D7C, 0 0 12px #5A6D7C; /* Steel gray glow */
}

</style>

