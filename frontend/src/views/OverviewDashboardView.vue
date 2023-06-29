<script setup>
import NavBarTop from "@/components/NavBarTop.vue";
import NavBarLeft from "@/components/NavBarLeft.vue";
import OverviewScansDatatable from "@/components/OverviewScansDatatable.vue";
import OverviewStatusCards from "@/components/OverviewStatusCards.vue";
import OverviewPIIOvertimeGraph from "@/components/OverviewPIIOvertimeGraph.vue";

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
        <div class="row">
          <OverviewScansDatatable />
        </div>
        <div class="row">
          <div class="col-md-2">
            <OverviewStatusCards />
          </div>
          <div class="col-md-10 nav-padding">
            <OverviewPIIOvertimeGraph />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.nav-padding {
  padding-top: 20px;
}
</style>
