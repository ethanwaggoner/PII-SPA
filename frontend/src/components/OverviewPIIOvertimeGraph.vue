<script setup>
import { ref, onMounted } from 'vue';
import { Chart, LineController, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js';

// Register the controller, scales, and elements
Chart.register(LineController, CategoryScale, LinearScale, PointElement, LineElement);

const chartType = ref('line');
const chartData = ref({
  labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
  datasets: [
    {
      label: "PII Found",
      data: [12, 19, 10, 17, 6, 3, 7, 8, 9, 10, 11, 12],
      borderColor: "white",
      lineTension: 0,
      pointBackgroundColor: "white",
    },
  ],
});
const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
});

onMounted(() => {
  const chartElement = document.querySelector("canvas");
  const chart = new Chart(chartElement, {
    type: chartType.value,
    data: chartData.value,
    options: chartOptions.value,
  });
});
</script>

<template>
  <div>
    <canvas class="chart-canvas"></canvas>
  </div>
</template>

<style scoped>
.chart-canvas {
  background: linear-gradient(180deg, #10142c, #252c48);
  width: 100%;
  height: 38vh;
  border: 2px solid #5A6D7C; /* Steel gray border */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C, 0 0 8px #5A6D7C, 0 0 12px #5A6D7C;
}
</style>

