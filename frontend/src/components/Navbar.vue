<template>
  <nav
    class="grid-cols-3 w-full fixed top-0  bg-white z-20 px-4 md:px-8 lg:px-20 h-20 flex justify-between items-center border-b shadow-sm">
    <!-- Logo Section fixed top-0 -->
    <div class="flex items-center">
      <router-link to="/:city_name" class="text-2xl font-bold">
        <img class="w-32 md:w-40 h-12 md:h-[52px]" src="../assets/askapollo-logo.png" alt="Logo" />
      </router-link>
    </div>
    <div :class="{
      'hidden lg:flex': !isMobileMenuOpen,
      'flex flex-col bg-white fixed top-20 left-0 w-full h-screen p-8 space-y-4': isMobileMenuOpen,
    }" class="justify-center items-center space-x-8 text-sm font-medium">
      <router-link to="/:city_name" class="text-sm font-medium text-[#224855]"
        :class="{ 'border-b-2 border-[#367892] text-center hover:text-yellow-500': isActive('/') }">
        HOME
      </router-link>
      <router-link to="/doctors" class="text-sm font-medium hover:text-yellow-500 text-[#224855]"
        :class="{ 'border-b-2 border-[#367892]': isActive('/doctors') }">
        ALL DOCTORS
      </router-link>
      <router-link to="/about" class="text-sm font-medium hover:text-yellow-500 text-[#224855]"
        :class="{ 'border-b-2 border-[#367892]': isActive('/about') }">
        ABOUT
      </router-link>
      <!-- <a href="#" class="border rounded-3xl py-1 px-4">Admin Panel</a> -->

      <div @click="citydata()">
        <button
          class="w-28 h-8 flex justify-center items-center gap-2 rounded-sm text-[10px] border border-[#224855] text-[#224855] bg-transparent outline-none"
          @click="togglecity">
          <span>
            <img class="" src="../assets/target.svg" />
          </span>
          {{ selectedCity ? selectedCity : 'SELECT CITY' }}
          <span><i class="fa fa-caret-down" aria-hidden="true"></i></span>
        </button>
        <div v-if="selectcity" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
          <div class="bg-white p-6 rounded-lg shadow-lg max-w-4xl w-full">
            <h2 class="text-sm font-semibold mb-2 text-[#224855]">Popular cities</h2>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-8 gap-2">
              <div v-for="(city, index) in resultcity" :key="index" class="flex flex-col items-center">
                <div
                  class="w-24 h-20 flex justify-center items-center rounded p-4 mt-2 border-white border-2 delay-100 transition-all hover:border-[#224855] hover:border-2"
                  :class="{ 'bg-[#fde7ac] border-yellow-500': selectedCity === city.town_name, 'bg-[#f1f7f7]': selectedCity !== city.town_name }"
                  @click="selectCity(city)">
                  <img class="w-full h-full object-cover" src="../assets/ahmedabad.svg" alt="city.name[0]" />
                </div>
                <p class="mt-2 text-center text-[#c4c2c] text-[12px] font-semibold">{{ city.town_name }}</p>
              </div>
            </div>
            <div class="mt-4 flex justify-end">
              <button class="px-4 py-2 bg-[#224855] text-white rounded hover:bg-[#3a7b91]" @click="togglecity">
                X
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="flex gap-2 items-center justify-center cursor-pointer " @click="toggleModal">
        <img class="w-6 h-6 " src="../assets/chat.png" />
        <p class="text-[#484b48] text-[12px] hover:text-yellow-500">Need Help?</p>
      </div>
      <div v-if="isModalOpen" class="fixed mt-16 flex items-center justify-center pl-[26rem]">
        <router-link @click="toggleModal" to="/contact"
          class="px-8 py-1 rounded-sm text-[10px] border border-[#224855]   outline-none bg-[#224855] text-white transition-all">
          CONTACT
        </router-link>
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="flex justify-end items-center space-x-4">
      <router-link v-if="!isLoggedIn" to="/register"
        class="hidden px-2 py-3 text-sm font-medium text-[#224855] hover:text-yellow-500 md:block">
        Register
      </router-link>

      <router-link v-if="!isLoggedIn" to="/login"
        class="flex items-center gap-2 px-6 py-2  rounded-sm text-[10px] border border-[#224855] text-[#224855] bg-transparent hover:bg-[#224855] hover:text-white transition-all duration-200">
        <span>Login</span>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"
          stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="M5.121 17.804A13.937 13.937 0 0112 15.75c2.425 0 4.703.574 6.879 1.595M15 10a3 3 0 11-6 0 3 3 0 016 0zM12 14.25c-2.925 0-5.564.929-7.879 2.554A8.999 8.999 0 1012 3a8.999 8.999 0 000 18z" />
        </svg>
      </router-link>


      <div v-else class="relative inline-block text-left">
        <Dropdown :options="[
          {
            label: 'Profile',
            onClick: () => {
              router.push('/profile')
            },
          },
          {
            label: 'My Appointment',
            onClick: () => {
              router.push('/my-appointment')
            }
          },
          {
            label: 'Log Out',
            onClick: () => {
              handleLogout()
            },
          },
        ]">
          <div
            class="inline-flex w-full justify-center gap-x-1.5 rounded-full bg-white p-1 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
            <img v-if="user_image" :src="user_image" alt="Profile" class="h-12 w-12 object-cover rounded-full" />
            <div v-else class="h-12 w-12 flex items-center justify-center bg-gray-200 rounded-full">
              <span class="text-lg font-semibold text-gray-700"> {{ name ? name[0].toUpperCase() : "?" }}</span>
            </div>

          </div>
        </Dropdown>

      </div>
    </div>
    <button @click="toggleMobileMenu" class="lg:hidden text-gray-700" aria-label="Toggle Mobile Menu">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 256 256" class="h-6 w-6">
        <path fill="currentColor"
          d="M200 136a8 8 0 0 1-8 8H64a8 8 0 0 1 0-16h128a8 8 0 0 1 8 8m32-56H24a8 8 0 0 0 0 16h208a8 8 0 0 0 0-16m-80 96h-48a8 8 0 0 0 0 16h48a8 8 0 0 0 0-16" />
      </svg>
    </button>
    <div v-if="isMobileMenu" class="fixed top-20 left-0 w-full h-screen flex  justify-end">
      <div class="bg-white p-6 w-11/12 h-screen max-w-md  shadow-lg" @click.stop>
        <ul class="space-y-2 text-gray-700">
          <li>
            <router-link to="/" class="block py-2 px-4 hover:bg-gray-100 rounded" @click="isMobileMenu = false">
              Home
            </router-link>
          </li>
          <li>
            <router-link to="/about" class="block py-2 px-4 hover:bg-gray-100 rounded" @click="isMobileMenu = false">
              About
            </router-link>
          </li>
          <li>
            <router-link to="/contact" class="block py-2 px-4 hover:bg-gray-100 rounded" @click="isMobileMenu = false">
              Contact
            </router-link>
          </li>
        </ul>

      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { isLoggedIn, logout } from "../auth";
import { Dropdown, } from 'frappe-ui'
import axios from "axios";

const isOpen = ref(false);
const isMobileMenu = ref(false)
const isMobileMenuOpen = ref(false);
const router = useRouter();
const route = useRoute();
const name = ref(null);
const user_image = ref(null);
const isModalOpen = ref(false);
const selectcity = ref(false)
const resultcity = ref({})
const selectedCity = ref(null)

const toggleModal = () => {
  isModalOpen.value = !isModalOpen.value;
};

const togglecity = () => {
  selectcity.value = !selectcity.value;
};


const fetchUserProfile = async () => {
  try {
    const response = await axios.get("/api/method/appointments_management.controllers.api.profile");

    if (response.data.message.code === 200) {
      const user = response.data.message.user;
      // console.log(user);
      user_image.value = user.user_image;
      name.value = user.name;

    } else {
      console.error("Failed to fetch profile:", response.data.message);
    }
  } catch (error) {
    console.error("Error fetching profile:", error);
  }
};

const handleLogout = async () => {
  try {
    const response = await axios.get(
      "/api/method/appointments_management.controllers.api.logout"
    );
    const result = response.data;
    console.log(result);
  } catch (error) {

  }
  logout();
  isOpen.value = false;
  router.push("/");
};


const citydata = async () => { 
  try {
    const response = await axios.get("/api/method/appointments_management.controllers.api.city_data");
    resultcity.value = response.data.message;
    console.log(resultcity.value);
  } catch (error) {
    console.error('Error fetching city data:', error);
  }
};


const selectCity = async (city) => {
  selectedCity.value = city.town_name;
  router.push({ name: "Home", params: { city_name: city.town_name } });
  sessionStorage.setItem('city_name', city.town_name );

  togglecity();
};


const isActive = (path) => route.path === path;

// Method to toggle mobile menu
const toggleMobileMenu = () => {
  isMobileMenu.value = !isMobileMenu.value;
};

onMounted(() => {
  fetchUserProfile();
});
</script>

<style>
nav a {
  transition: border-color 0.2s, color 0.2s;
}
</style>
