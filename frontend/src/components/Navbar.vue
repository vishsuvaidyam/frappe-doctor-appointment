<template>
  <nav
    class="grid-cols-3 w-full fixed top-0 bg-white z-20 px-4 md:px-8 lg:px-20 h-20 flex justify-between items-center border-b shadow-sm">
    <!-- Logo Section -->
    <div class="flex items-center">
      <router-link to="/" class="text-2xl font-bold">
        <img class="w-32 md:w-40 h-12 md:h-[52px]" src="../assets/logo-BNCDj_dh.svg" alt="Logo" />
      </router-link>
    </div>
    <div :class="{
      'hidden lg:flex': !isMobileMenuOpen,
      'flex flex-col bg-white fixed top-20 left-0 w-full h-screen p-8 space-y-4': isMobileMenuOpen,
    }" class="justify-center items-center space-x-8 text-sm font-medium">
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
      <router-link v-if="!isLoggedIn" to="/register" class="hidden px-2 py-3 text-sm font-medium text-black md:block">
        Register
      </router-link>
      <router-link v-if="!isLoggedIn" to="/login"
        class="px-6 py-2 text-sm font-normal text-white bg-blue-500 hover:bg-blue-600 md:block rounded text-center">
        Login
      </router-link>
      <div v-else class="relative inline-block text-left">
        <button @click="isOpen = !isOpen"
          class="inline-flex w-full justify-center gap-x-1.5 rounded-full bg-white p-1 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
          <img v-if="userImage" :src="userImage" alt="Profile" class="h-12 w-12 object-cover rounded-full" />
          <div v-else class="h-12 w-12 flex items-center justify-center bg-gray-200 rounded-full">
            <span class="text-lg font-semibold text-gray-700">{{ full_name[0]}}</span>
          </div>
        </button>
        <div v-if="isOpen"
          class="absolute right-0 mt-2 w-52 origin-top-right rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
          <div class="p-4 bg-gray-100 text-gray-700 space-y-2">
            <router-link to="/profile"
              class="flex items-center w-full px-3 py-2 text-left text-black rounded-md hover:bg-gray-200 transition">
              <i class="fas fa-user mr-2"></i> Profile
            </router-link>
            <router-link to="/my-appointment"
              class="flex items-center w-full px-3 py-2 text-left text-black rounded-md hover:bg-gray-200 transition">
              <i class="fas fa-calendar-alt mr-2"></i> My Appointment
            </router-link>
            <button
              class="flex items-center w-full px-3 py-2 text-left text-black rounded-md hover:bg-red-100 hover:text-red-600 transition"
              @click="handleLogout">
              <i class="fas fa-sign-out-alt mr-2"></i> Logout
            </button>
          </div>
        </div>
      </div>
    </div>
    <button @click="toggleMobileMenu" class="lg:hidden text-gray-700" aria-label="Toggle Mobile Menu">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 256 256" class="h-6 w-6">
        <path fill="currentColor"
          d="M200 136a8 8 0 0 1-8 8H64a8 8 0 0 1 0-16h128a8 8 0 0 1 8 8m32-56H24a8 8 0 0 0 0 16h208a8 8 0 0 0 0-16m-80 96h-48a8 8 0 0 0 0 16h48a8 8 0 0 0 0-16" />
      </svg>
    </button>
    <div v-if="isMobileMenu"
      class="fixed top-20 left-0 w-full h-screen flex  justify-end">
      <div class="bg-white p-6 w-11/12 h-screen max-w-md  shadow-lg" @click.stop>
        <ul class="space-y-2 text-gray-700">
          <li>
            <router-link to="/" class="block py-2 px-4 hover:bg-gray-100 rounded" @click="isMobileMenu = false">
              Home
            </router-link>
          </li>
          <li>
            <router-link to="/about" class="block py-2 px-4 hover:bg-gray-100 rounded"
              @click="isMobileMenu = false">
              About
            </router-link>
          </li>
          <li>
            <router-link to="/contact" class="block py-2 px-4 hover:bg-gray-100 rounded"
              @click="isMobileMenu = false">
              Contact
            </router-link>
          </li>
        </ul>

      </div>
    </div>
  </nav>
</template>

<script setup>
import { onMounted, ref,watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import { isLoggedIn, logout } from "../auth";

const isOpen = ref(false);
const isMobileMenu=ref(false)
const isMobileMenuOpen = ref(false);  
const router = useRouter();
const route = useRoute();
const userImage = ref(null);
const full_name = ref('')


onMounted(() => {
  const storedData = sessionStorage.getItem("user");
  if (storedData) {
    const userData = JSON.parse(storedData);
    userImage.value = userData?.user_image;
    full_name.value = userData?.full_name;
  }
});

const handleLogout = () => {
  logout();
  isOpen.value = false;
  router.push("/");
};

watch(() => route.fullPath, () => {
  isOpen.value = false;
});

const isActive = (path) => route.path === path;

// Method to toggle mobile menu
const toggleMobileMenu = () => {
  isMobileMenu.value = !isMobileMenu.value;
};

</script>

<style>
nav a {
  transition: border-color 0.2s, color 0.2s;
}
</style>
