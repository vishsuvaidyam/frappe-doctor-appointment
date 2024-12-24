<template>
  <div class="w-full ">
    <div class="bg-blue-500  h-auto flex items-center rounded-lg mt-10 mx-20">
      <div class="container mx-auto px-6 md:px-12 lg:px-16 md:py-6">
        <div class="flex flex-col lg:flex-row items-center">
          <div class="lg:w-1/2 text-center lg:text-left pb-8 lg:pb-0">
            <h1 class="text-4xl md:text-5xl font-bold text-white pb-4">
              Book Appointment <br />
              With Trusted Doctors
            </h1>

            <div class="flex items-center space-x-4 pb-6">
              <div class="flex -space-x-4 ">
                <img class="w-10 h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 1" />
                <img class="w-10 h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 2" />
                <img class="w-10 h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 3" />
                <p class="text-white text-sm px-12">
                  Simply browse through our extensive list of trusted doctors,
                  schedule your appointment hassle-free.
                </p>
              </div>
            </div>
            <a href="#"
              class="inline-flex items-center bg-white text-gray-500 text-sm font-semibold py-3 px-6 rounded-3xl shadow-lg hover:scale-105 transition-all">
              Book appointment
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ml-2" viewBox="0 0 24 24">
                <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                  stroke-miterlimit="10" stroke-width="1.5" d="m14 16l4-4m0 0l-4-4m4 4H6" />
              </svg>
            </a>


          </div>
          <div class="lg:w-1/2 flex justify-center">
            <img class="w-full max-w-md lg:max-w-full" src="../assets/header_img-DhAi3lLA.png" alt="Doctors" />
          </div>
        </div>
      </div>
    </div>
    <div>
      <Speciality />
    </div>
    <div class="mx-20 pt-10">
      <div class="text-center">
        <h2 class="text-2xl font-bold text-gray-800">Top Doctors to Book</h2>
        <p class="text-gray-800 mt-2">Simply browse through our extensive list of trusted doctors.</p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 w-full pt-10  ">
        <All_doctors />
      </div>
      <div class="flex justify-center items-center pt-5">
        <router-link to="/doctors" class=" px-10 py-2 rounded-3xl border  bg-gray-50">
          More
        </router-link>
      </div>
    </div>

    <div class="bg-blue-500 h-auto flex flex-col lg:flex-row items-center rounded-lg mt-10 mx-4 lg:mx-20 p-6">
      <!-- Text Section -->
      <div class="lg:w-1/2 text-center lg:text-left mb-6 lg:mb-0 px-4">
        <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold text-white pb-4 ml-8">
          Book Appointment <br>
          With 100+ Trusted Doctors
        </h1>
        <router-link to="/register"
          class="inline-block cursor-pointer bg-white  py-3 px-6 rounded-3xl ml-8 hover:scale-105 transition-all">
          Create Account
        </router-link>
      </div>

      <!-- Image Section -->
      <div class="lg:w-1/2 flex justify-center">
        <img class="w-full max-w-xs md:max-w-md lg:max-w-lg object-contain rounded-lg"
          src="../assets/appointment_female.png" alt="Doctors" />
      </div>
    </div>



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
