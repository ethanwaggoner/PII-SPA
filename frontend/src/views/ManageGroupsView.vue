<script setup>
import GroupsContainer from "@/components/GroupsContainer.vue";
import NavBarTop from "@/components/NavBarTop.vue";
import NavBarLeft from "@/components/NavBarLeft.vue";

</script>

<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-12 nav-padding">
        <NavBarTop />
      </div>
    </div>
    <div class="row">
      <div class="col-md-2 nav-padding">
        <NavBarLeft />
      </div>
      <div class="col-md-10 nav-padding">
        <GroupsContainer :clients = "[
            {id: 1, status: true, hostname: 'Client 1', ip: '192.168.1.1', piiCount: 3},
            {id: 2, status: true, hostname: 'Client 2', ip: '192.168.1.1', piiCount: 5},
            {id: 3, status: false, hostname: 'Client 3', ip: '192.168.1.1', piiCount: 8},
        ]"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
.nav-padding {
  padding-top: 20px;
}
</style>