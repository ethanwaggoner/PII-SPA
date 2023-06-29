<script setup>
const props = defineProps({
  client: {
    type: Object,
    required: true
  }
});
</script>

<template>
  <div class="card client-card">
    <div class="card-header">
      {{ client.hostname }}
    </div>
    <div class="card-body">
      <p class="card-text">
        ID: {{ client.id }}<br>
        IP Address: {{ client.ip }}<br>
        PII Count: {{ client.piiCount }}
      </p>
      <button class="btn btn-primary">More Information</button>
    </div>
  </div>
</template>

<style scoped>
.client-card {
  align-items: center;
  color: white;
  width: 10rem;
  font-size: 0.8rem;
  border: 2px solid #5A6D7C;
  border-radius: 10px;
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C, 0 0 8px #5A6D7C, 0 0 12px #5A6D7C; /* Steel gray glow */
  background: linear-gradient(180deg, #10142c, #252c48);
}

.client-card .btn-primary {
  color: white;
  font-size: 0.8rem;
  background-color: #5A6D7C;
  border-color: #5A6D7C;
}

.card-header {
  align-self: start;
}
</style>
