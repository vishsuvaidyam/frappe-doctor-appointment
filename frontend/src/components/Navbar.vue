<template>
  <nav
    class="grid-cols-3 w-full fixed top-0 bg-white z-20 px-4 md:px-8 lg:px-20 h-20 flex justify-between items-center shadow-md">
    <!-- Logo Section -->
    <div class="flex items-center">
      <router-link to="/" class="text-2xl font-bold">
        <img class="w-32 md:w-40 h-12 md:h-[52px]" src="../assets/logo-BNCDj_dh.svg" alt="Logo" />
      </router-link>
    </div>

    <!-- Links Section -->
    <div class="hidden lg:flex justify-center space-x-8 text-sm font-medium">
      <router-link to="/" class="text-sm font-medium"
        :class="{ 'border-b-2 border-blue-500 text-center': isActive('/') }">
        HOME
      </router-link>
      <router-link to="/doctors" class="text-sm font-medium"
        :class="{ 'border-b-2 border-blue-500': isActive('/doctors') }">
        ALL DOCTORS
      </router-link>
      <router-link to="/about" class="text-sm font-medium"
        :class="{ 'border-b-2 border-blue-500': isActive('/about') }">
        ABOUT
      </router-link>
      <router-link to="/contact" class="text-sm font-medium"
        :class="{ 'border-b-2 border-blue-500': isActive('/contact') }">
        CONTACT
      </router-link>
      <a href="#" class="border rounded-3xl py-1 px-4">Admin Panel</a>
    </div>

    <!-- Action Buttons -->
    <div class="flex justify-end items-center space-x-4">
      <button v-if="!isLoggedIn"
        class="hidden px-6 py-3 text-sm font-normal text-white bg-blue-600 rounded-3xl md:block" @click="goToRegister">
        Create Account
      </button>

      <div v-else class="relative inline-block text-left">
        <button @click="isOpen = !isOpen"
          class="inline-flex justify-center w-full rounded-full p-6 border  border-gray-300 shadow-sm   text-sm font-semibold text-white">
          <!-- <img src="../assets/doc10.png" alt="Profile"
            class="rounded-full border h-auto w-auto border-gray-300 shadow-lg" /> -->
        </button>
        <div v-if="isOpen"
          class="absolute right-0 mt-2 w-52 origin-top-right rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
          <div class="p-4 bg-gray-100 text-gray-700">
            <router-link to="/profile" class="w-full text-left px-2 py-1 text-black" @click="isOpen = false">
              Profile
            </router-link>
            <button class="w-full text-left px-2 py-1 text-black" @click="goToProfile">
              My Appointments
            </button>
            <button class="w-full text-left px-2 py-1 text-black" @click="logout">
              Logout
            </button>
          </div>
        </div>
      </div>

      <!-- Hamburger Menu for Mobile -->
      <div class="relative lg:hidden">
        <button @click="toggleMenu" class="focus:outline-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
          </svg>
        </button>
        <!-- Dropdown Menu -->
        <div v-if="menuOpen" class="absolute right-0 z-10 mt-2 bg-white border rounded-lg shadow-lg">
          <router-link to="/" class="block px-4 py-2 text-sm font-medium hover:bg-gray-100">
            HOME
          </router-link>
          <router-link to="/doctors" class="block px-4 py-2 hover:bg-gray-100">
            ALL DOCTORS
          </router-link>
          <router-link to="/about" class="block px-4 py-2 hover:bg-gray-100">
            ABOUT
          </router-link>
          <router-link to="/contact" class="block px-4 py-2 hover:bg-gray-100">
            CONTACT
          </router-link>
          <a href="#" class="block px-4 py-2 text-sm hover:bg-gray-100">Admin Panel</a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

const isOpen = ref(false);  
const menuOpen = ref(false);  
const isLoggedIn = ref(false); 

const router = useRouter();
const route = useRoute();

// Check if user is logged in
onMounted(() => {
  isLoggedIn.value = !!sessionStorage.getItem("user");
});

// Handle navigation
const goToRegister = () => router.push("/register");
const goToProfile = () => router.push("/profile");

// Logout action
const logout = () => {
  sessionStorage.removeItem("user");
  isLoggedIn.value = false;
  router.push("/");
};

// Highlight active link
const isActive = (path) => route.path === path;

// Toggle mobile menu visibility
const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
};
</script>

<style>
nav a {
  transition: border-color 0.2s, color 0.2s;
}
</style>
