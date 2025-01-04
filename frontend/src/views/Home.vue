<template>
  <div class="w-full">
    <!-- Hero Section -->
    <div class="bg-blue-500 h-auto flex flex-col lg:flex-row items-center rounded-lg mt-10 mx-4 sm:mx-6 md:mx-10 lg:mx-20">
      <div class="container mx-auto px-4 sm:px-6 md:px-8 py-6">
        <div class="flex flex-col lg:flex-row items-center">
          <div class="lg:w-1/2 text-center lg:text-left pb-8 lg:pb-0">
            <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold text-white pb-4">
              Book Appointment <br />
              With Trusted Doctors
            </h1>
            <div class="flex flex-col sm:flex-row items-center sm:items-start space-y-4 sm:space-y-0 sm:space-x-4 pb-6">
              <div class="flex -space-x-4">
                <img class="w-8 sm:w-10 h-8 sm:h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 1" />
                <img class="w-8 sm:w-10 h-8 sm:h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 2" />
                <img class="w-8 sm:w-10 h-8 sm:h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 3" />
              </div>
              <p class="text-white text-sm sm:text-base px-4">
                Simply browse through our extensive list of trusted doctors, schedule your appointment hassle-free.
              </p>
            </div>
            <a href="#"
              class="inline-flex items-center bg-white text-gray-500 text-sm font-semibold py-2 px-4 sm:py-3 sm:px-6 rounded-3xl shadow-lg hover:scale-105 transition-all">
              Book appointment
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ml-2" viewBox="0 0 24 24">
                <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                  stroke-miterlimit="10" stroke-width="1.5" d="m14 16l4-4m0 0l-4-4m4 4H6" />
              </svg>
            </a>
          </div>
          <div class="lg:w-1/2 flex justify-center mt-6 lg:mt-0">
            <img class="w-full max-w-sm md:max-w-md lg:max-w-full" src="../assets/header_img-DhAi3lLA.png" alt="Doctors" />
          </div>
        </div>
      </div>
    </div>

    <!-- Speciality Section -->
    <div>
      <Speciality />
    </div>

    <!-- Top Doctors Section -->
    <div class="mx-4 sm:mx-6 md:mx-10 lg:mx-20 pt-10">
      <div class="text-center">
        <h2 class="text-xl sm:text-2xl md:text-3xl font-bold text-gray-800">Top Doctors to Book</h2>
        <p class="text-gray-800 mt-2">Simply browse through our extensive list of trusted doctors.</p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 sm:gap-6 pt-10">
        <All_doctors />
      </div>
      <div class="flex justify-center items-center pt-5">
        <router-link to="/doctors" class="px-8 py-2 rounded-3xl border bg-gray-50 text-gray-800 text-sm sm:text-base">
          More
        </router-link>
      </div>
    </div>

    <!-- CTA Section -->
    <div class="bg-blue-500 h-auto flex flex-col lg:flex-row items-center rounded-lg mt-10 mx-4 sm:mx-6 lg:mx-20 p-6">
      <div class="lg:w-1/2 text-center lg:text-left mb-6 lg:mb-0 px-4">
        <h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold text-white pb-4">
          Book Appointment <br> With 100+ Trusted Doctors
        </h1>
        <router-link to="/register"
          class="inline-block cursor-pointer bg-white py-2 sm:py-3 px-4 sm:px-6 rounded-3xl text-gray-500 font-semibold hover:scale-105 transition-all">
          Create Account
        </router-link>
      </div>
      <div class="lg:w-1/2 flex justify-center">
        <img class="w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg object-contain rounded-lg"
          src="../assets/appointment_female.png" alt="Doctors" />
      </div>
    </div>

    <!-- Footer -->
    <div class="mt-20">
      <Footer />
    </div>
  </div>
</template>

<script setup>
import Speciality from './Speciality.vue';
import All_doctors from './All_doctors.vue';
import Footer from '../components/Footer.vue';
</script>
