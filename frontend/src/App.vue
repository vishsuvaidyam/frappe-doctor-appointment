<template>
  <div class="inset-0  ">
    <div class="pt-20">
      <Navbar/>
    </div>
    <div class=" h-full bg-[#F8FCFF]">
      <router-view />
      <div class="mx-60">
        <!-- <Footer/> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import Navbar from "./components/Navbar.vue";
// import Footer from "./components/Footer.vue";
import { useRoute } from "vue-router";

const route = useRoute();
</script>
<!-- mx-auto max-w-[1700px] -->