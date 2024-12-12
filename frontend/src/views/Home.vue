<template>
  <div class="w-full ">
    <div class="bg-blue-500  h-auto flex items-center rounded-lg mt-10 mx-20">
      <div class="container mx-auto px-6 md:px-12 lg:px-16">
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
              class="bg-white text-gray-500  text-sm font-semibold py-3 px-6 rounded-3xl shadow-lg hover:bg-blue-100 transition">
              Book appointment →
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
    <div class="">
      <Doctors />
    </div>

    <div class="bg-blue-500  h-96 flex items-center rounded-lg mt-10 mx-20 ">
      <div class="container mx-auto px-6 md:px-12 lg:px-16 ">
        <h1 class="text-4xl md:text-5xl font-bold text-white pb-4">
          Book Appointment <br>
          With 100+ Trusted Doctors
        </h1>
        <a href="#" class="bg-white text-gray-500  text-sm font-semibold py-3 px-6 rounded-3xl shadow-lg ">
          Create Account
        </a>
      </div>
      <div class="lg:w-1/2   flex justify-center  ">
        <img class="w-auto max-w-md lg:max-w-full h-80" src="../assets/appointment_female.png" alt="Doctors" />
      </div>
    </div>
    
  </div>

</template>

<script setup>
import Speciality from './Speciality.vue';
import Doctors from './Doctors.vue';
</script>
