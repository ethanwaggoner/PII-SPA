<script setup>

</script>

<template>
  <div class="container">
    <div class="row">
        <div class="card card-fixed-width">
          <div class="card-body">
            <h5 class="card-title">Total PII Count</h5>
            <p class="card-text">500</p>
          </div>
        </div>
        <div class="card card-fixed-width">
          <div class="card-body">
            <h5 class="card-title">Total Scans</h5>
            <p class="card-text">500</p>
          </div>
        </div>
        <div class="card card-fixed-width">
          <div class="card-body">
            <h5 class="card-title">Total PII Removed</h5>
            <p class="card-text">500</p>
          </div>
        </div>
      </div>
  </div>
</template>

<style scoped>
.container {
  margin-top: 20px;
  display: flex;
  justify-content: start;

}

.card-fixed-width {
  width: 100%; /* Adjust the width as needed */
  margin-bottom: 20px;
  border: 2px solid #5A6D7C; /* Steel gray border */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C, 0 0 8px #5A6D7C, 0 0 12px #5A6D7C; /* Steel gray glow */
}

.card-body {
  color: white;
  padding: 24px;
  text-align: center;
  background: linear-gradient(180deg, #10142c, #252c48);
}

.card-title {
  font-size: 18px;
  text-align: center;
}
</style>
