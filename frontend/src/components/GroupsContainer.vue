<script setup>
import { ref, watch } from 'vue';
import GroupClientCard from "@/components/GroupClientCard.vue";

const props = defineProps({
  clients: {
    type: Array,
    required: false
  }
});

let groups = ref([]);
let localClients = ref([...props.clients]);

watch(() => props.clients, (newClients) => {
  localClients.value = [...newClients];
}, { immediate: true });

const dragStart = (event, client) => {
  event.dataTransfer.setData('application/json', JSON.stringify(client));
};

const drop = (event) => {
  const client = JSON.parse(event.dataTransfer.getData('application/json'));
  localClients.value = localClients.value.filter(c => c.id !== client.id);
  groups.value.push(client);
};
</script>



<template>
  <div class="row container-container">
    <div class="col container-with-title">
      <h2>Clients</h2>
      <input class="form-control search-input" type="text" placeholder="Search">
      <div class="client-container">
        <div class="row" v-for="(row, index) in Math.ceil(localClients.length / 3)" :key="index">
          <div class="col-4" v-for="client in localClients.slice(index * 3, (index * 3) + 3)" :key="client.id">
            <GroupClientCard :client="client" draggable="true" v-on:dragstart="dragStart($event, client)"/>
          </div>
        </div>
      </div>
    </div>
    <div class="move-button-container">
      <button class="move-all-button">Move All -></button>
    </div>
    <div class="col container-with-title">
      <h2>Groups</h2>
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle form-control" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
          Select
        </button>
        <ul class="dropdown-menu w-100" aria-labelledby="dropdownMenuButton">
          <li><a class="dropdown-item" href="#">Unassigned</a></li>
          <li><a class="dropdown-item" href="#">Offline</a></li>
          <li><a class="dropdown-item" href="#">Accounting</a></li>
        </ul>
      </div>
      <div class="client-container" v-on:dragover.prevent v-on:drop="drop($event)">
        <div class="row" v-for="(row, index) in Math.ceil(groups.length / 3)" :key="index">
          <div class="col-4" v-for="client in groups.slice(index * 3, (index * 3) + 3)" :key="client.id">
            <GroupClientCard :client="client" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h2 {
  color: white;
  text-align: center;
}

.c  ient-container {
  eight: 66vh;
  width: 100%;
  margin-bottom: 10px;
  padding: 20px;
  border: 2px solid #5A6D7C;
  border-radius: 10px;
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C, 0 0 8px #5A6D7C, 0 0 12px #5A6D7C; /* Steel gray glow */
  background: linear-gradient(180deg, #10142c, #252c48)
}

.container-container {
  padding: 40px;
  gap: 40px;
  display: flex;
  justify-content: space-between;
}

.container-with-title {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.search-input, .dropdown-toggle {
  color: white !important;
  margin-bottom: 10px;
  width: 35vh;
  border: 2px solid #5A6D7C;
  border-radius: 10px;
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C, 0 0 8px #5A6D7C, 0 0 12px #5A6D7C; /* Steel gray glow */
  background: linear-gradient(180deg, #10142c, #252c48)
}

.search-input::placeholder {
  color: white;
  opacity: 0.7;
}

.move-button-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 10vw;
}

.move-all-button {
   background: linear-gradient(180deg, #10142c, #252c48);
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

.move-all-button:hover {
  background-color: rgba(90, 109, 124, 0.1); /* Button hover effect */
  color: #5A6D7C; /* Button text color changes on hover */
  border-color: white;
}
</style>
