<template>
  <nav
    class="grid-cols-3 w-full fixed top-0 bg-white z-20 px-4 md:px-8 lg:px-20 h-20 flex justify-between items-center shadow-md ">
    <!-- Logo Section -->
    <div class="flex items-center">
      <router-link to="/" class="text-2xl font-bold">
        <img class="w-32 md:w-40 h-12 md:h-[52px]" src="../assets/logo-BNCDj_dh.svg" alt="Logo" />
      </router-link>
    </div>
    <!-- Links Section -->
    <div class="hidden md:flex justify-center space-x-8 text-sm font-medium">
      <router-link to="/" class="text-sm font-medium">
        HOME
      </router-link>
      <router-link to="/doctors">
        ALL DOCTORS
      </router-link>
      <router-link to="/about">
        ABOUT
      </router-link>
      <router-link to="/contact">
        CONTACT
      </router-link>
      <a href="#" class="border rounded-3xl py-1 px-4">Admin Panel</a>
    </div>

    <!-- Buttons Section -->
    <div class="flex justify-end items-center space-x-4">
      <button class="hidden px-6 py-3 text-sm font-normal text-white bg-blue-600 rounded-3xl md:block">
        Create account
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
          <router-link to="/" class="text-sm font-medium">
            HOME
          </router-link>
          <router-link to="/doctors">
            ALL DOCTORS
          </router-link>
          <router-link to="/about">
            ABOUT
          </router-link>
          <router-link to="/contact">
            CONTACT
          </router-link>
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