<template>
	<div class="h-screen flex flex-col  px-28 justify-center">
	  <Navbar />
	  <div class="flex-1 pt-8">
		<router-view />
	  </div>
	</div>
  </template>
  
  <script setup>
  import Navbar from "./components/Navbar.vue";
  import { useRoute } from "vue-router";
  
  const route = useRoute();
  </script>
  