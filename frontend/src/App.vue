<template>
  <div class=" ">
    <div class="pt-20">
      <Navbar/>
    </div>
    <div class="mx-auto max-w-[1700px] h-full ">
      <router-view />
      <!-- <div class="mt-20">
        <Footer/>
      </div> -->
    </div>
  </div>
</template>

<script setup>
import Navbar from "./components/Navbar.vue";
// import Footer from "./components/Footer.vue";
import { useRoute } from "vue-router";

const route = useRoute();
</script>
