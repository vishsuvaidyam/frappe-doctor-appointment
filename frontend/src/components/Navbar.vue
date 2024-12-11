<template>
<nav class="grid grid-cols-3 items-center w-full h-20 px-4 bg-white md:px-8 border-b">
  <!-- Logo Section -->
  <div class="flex items-center">
    <img class="h-10 w-auto" src="../assets/logo-BNCDj_dh.svg" alt="Logo" />
  </div>

  <!-- Links Section -->
  <div class="hidden md:flex justify-center space-x-8 text-sm font-medium">
    <a href="#" class="hover:text-red-600">HOME</a>
    <a href="#" class="hover:text-red-600">ALL DOCTORS</a>
    <a href="#" class="hover:text-red-600">ABOUT</a>
    <a href="#" class="hover:text-red-600">CONTACT</a>
    <a href="#" class="border rounded-3xl py-1 px-4">Admin Panel</a>
  </div>

  <!-- Buttons Section -->
  <div class="flex justify-end items-center space-x-4">
    <button class="hidden px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-3xl md:block">
      Create Account
    </button>
    <!-- Hamburger Menu for Mobile -->
    <div class="relative md:hidden">
      <button @click="toggleMenu" class="focus:outline-none">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
        </svg>
      </button>
      <!-- Dropdown Menu -->
      <div v-if="menuOpen" class="absolute right-0 z-10 mt-2 bg-white border rounded-lg shadow-lg">
        <a href="#" class="block px-4 py-2 text-sm hover:bg-gray-100">HOME</a>
        <a href="#" class="block px-4 py-2 text-sm hover:bg-gray-100">ALL DOCTORS</a>
        <a href="#" class="block px-4 py-2 text-sm hover:bg-gray-100">ABOUT</a>
        <a href="#" class="block px-4 py-2 text-sm hover:bg-gray-100">CONTACT</a>
        <a href="#" class="block px-4 py-2 text-sm hover:bg-gray-100">Admin Panel</a>
      </div>
    </div>
  </div>
</nav>
</template>
 
<script setup>
import { ref } from "vue";

// State to manage dropdown menu visibility
const menuOpen = ref(false);

// Toggle menu visibility
const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
};
</script>