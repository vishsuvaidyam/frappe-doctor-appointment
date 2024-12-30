<template>
  <nav
    class="grid-cols-3 w-full fixed top-0 bg-white z-20 px-4 md:px-8 lg:px-20 h-20 flex justify-between items-center  border-b shadow-sm">
    <div class="flex items-center">
      <router-link to="/" class="text-2xl font-bold">
        <img class="w-32 md:w-40 h-12 md:h-[52px]" src="../assets/logo-BNCDj_dh.svg" alt="Logo" />
      </router-link>
    </div>

    <!-- Links Section -->
    <div class="hidden lg:flex justify-center items-center space-x-8 text-sm font-medium">
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
      <!-- <div
        class="inline-flex w-full justify-center gap-x-1.5 rounded-full bg-white p-1 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
        <img v-if="auth?.cookie?.user_image" class="w-10 h-10 object-cover rounded-full" :src="auth?.cookie?.user_image"
          alt="">
        <p class="w-10 h-10 flex items-center justify-center text-xl font-normal text-gray-600" v-else>{{
          auth?.cookie?.full_name?.split('')[0] }}</p>
      </div> -->

      <router-link v-if="!isLoggedIn" to="/register" class="hidden px-2 py-3 text-sm font-medium text-black md:block">
        Register
      </router-link>
      <router-link v-if="!isLoggedIn" to="/login"
        class=" px-6 py-2 text-sm font-normal text-white bg-blue-500 hover:bg-blue-600 md:block rounded text-center">
        Login
      </router-link>
      <div v-else class="relative inline-block text-left">
        <button @click="isOpen = !isOpen"
          class="inline-flex w-full justify-center gap-x-1.5 rounded-full bg-white p-1 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
          <img v-if="userImage" :src="userImage" alt="Profile" class="h-12 w-12 object-cover rounded-full" />
          <div v-else class="h-12 w-12 flex items-center justify-center bg-gray-200 rounded-full">
            <span class="text-lg font-semibold text-gray-700">{{ full_name }}</span>
          </div>
        </button>
        <div v-if="isOpen"
          class="absolute right-0 mt-2 w-52 origin-top-right rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
          <div class="p-4 bg-gray-100 text-gray-700">
            <router-link to="/profile" class="w-full text-left px-2 py-1 text-black">
              Profile
            </router-link>
            <button class="w-full text-left px-2 py-1 text-black" @click="handleLogout">
              Logout
            </button>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { isLoggedIn, logout } from "../auth";

const isOpen = ref(false);
const router = useRouter();
const route = useRoute();
const userImage = ref(null);
const full_name = ref()


onMounted(() => {
  // Retrieve the user data from sessionStorage
  const storedData = sessionStorage.getItem("user");
  if (storedData) {
    const userData = JSON.parse(storedData);
    userImage.value = userData?.user_image;
    full_name.value = userData?.full_name; 

    // console.log( userData, "===================");
  }
});


const handleLogout = () => {
  logout();
  isOpen.value = false;
  router.push("/");
};

const isActive = (path) => route.path === path;
</script>

<style>
nav a {
  transition: border-color 0.2s, color 0.2s;
}
</style>
